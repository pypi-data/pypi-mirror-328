import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry

OPENMETEO_URL = "https://api.open-meteo.com/v1/forecast"

class Openmeteo:

    def __init__(self) -> None:
        self.__setup()

    def __setup(self) -> None:
        cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
        retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
        self.client = openmeteo_requests.Client(session = retry_session)

    def forecast(self, params: dict) -> pd.DataFrame:

        if not (params['hourly'] or params['minutely_15']):
            return None

        responses = self.client.weather_api(OPENMETEO_URL, params=params)
        response = responses[0]

        if params['minutely_15']:
            minutely_15 = response.Minutely15()
            fifteen = {
                "date_time": pd.date_range(
                    start = pd.to_datetime(minutely_15.Time(), unit = "s", utc = True),
                    end = pd.to_datetime(minutely_15.TimeEnd(), unit = "s", utc = True),
                    freq = pd.Timedelta(seconds = minutely_15.Interval()),
                    inclusive = "right"
            )}

            for i, variable_name in enumerate(params['minutely_15']):
                fifteen[variable_name] = minutely_15.Variables(i).ValuesAsNumpy()

            fifteen_df = pd.DataFrame(fifteen)

        if params['hourly']:
            hourly = response.Hourly()
            one_hour = {
                "date_time": pd.date_range(
                    start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
                    end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
                    freq = pd.Timedelta(seconds = hourly.Interval()),
                    inclusive = "right"
            )}

            for i, variable_name in enumerate(params['hourly']):
                one_hour[variable_name] = hourly.Variables(i).ValuesAsNumpy()

            one_hour_df = self.__interpolate_1hour_to_15min(pd.DataFrame(one_hour))

        if params['minutely_15'] and params['hourly']:
            df = pd.merge(fifteen_df, one_hour_df, on='date_time')
        elif params['minutely_15']:
            df = fifteen_df
        elif params['hourly']:
            df = one_hour_df

        df['date_time'] = df['date_time'] \
            .dt.tz_convert(params['timezone']) \
            .dt.tz_localize(None)

        return df

    def __interpolate_1hour_to_15min(self, one_hour: pd.DataFrame) -> pd.DataFrame:
        one_hour = one_hour.set_index('date_time')
        fifteen = one_hour.resample('15min').interpolate(method='linear')
        fifteen = fifteen.reset_index()

        return fifteen

    def bangbo_forecast(self, params: dict) -> pd.DataFrame:

        all_params = params | {
            "latitude": 13.4916354486428,
            "longitude": 100.85609829815238,
            "timezone": "Asia/Bangkok",
            "tilt": 13
        }

        return self.forecast(all_params)

    def svb_forecast(self, params: dict) -> pd.DataFrame:

        all_params = params | {
            "latitude": 13.682354854382313,
            "longitude": 100.74670116685681,
            "timezone": "Asia/Bangkok",
            "tilt": 13
        }

        return self.forecast(all_params)
