import pandas as pd

from src.config import RANGE_MAX_DATE, RANGE_MIN_DATE, SECONDS_PER_HOUR, TIMEZONE_STR


def clean_irradiance_data(irradiance_data):
    
    irradiance_data = align_timezones(irradiance_data, TIMEZONE_STR)
    irradiance_data = align_timestamps_minutes(irradiance_data, 30)
    time_limited_data = limit_date_range(irradiance_data, TIMEZONE_STR)
    cleaned_irradiance_data = time_limited_data.drop(columns=['Int'])
    return cleaned_irradiance_data


def clean_cloudiness_data(cloudiness_data):
    cloudiness_data = cloudiness_data.rename({'valid_time': 'time'}, axis=1)

    cloudiness_data = align_timezones(cloudiness_data, TIMEZONE_STR)
    cloudiness_data = align_timestamps_minutes(cloudiness_data, 60)
    time_limited_data = limit_date_range(cloudiness_data, TIMEZONE_STR)
    cloudiness_data = time_limited_data.drop(columns=['latitude', 'longitude', 'sst', 'cbh', 't2m'])

    cloudiness_data['ssrd'] = cloudiness_data['ssrd'].clip(lower=0)

    cloudiness_data['ssrd'] = cloudiness_data['ssrd'] / SECONDS_PER_HOUR # Transform from J/m² to W/m²

    return cloudiness_data


def cross_datasets(irradiance_data, cloudiness_data):
    return irradiance_data.merge(cloudiness_data, on='time', how='inner')


def limit_date_range(df,tz):
    return df[(df['time'] >= pd.Timestamp(RANGE_MIN_DATE, tz=tz)) & (df['time'] <= pd.Timestamp(RANGE_MAX_DATE, tz=tz))]


def align_timezones(df, target_tz):
    align_dataframe = df.copy()
    align_dataframe['time'] = align_dataframe['time'].dt.tz_localize('UTC')
    align_dataframe['time'] = align_dataframe["time"].dt.tz_convert(target_tz)
    return align_dataframe


def align_timestamps_minutes(df, time):
    align_dataframe = df.copy()
    align_dataframe['time'] = align_dataframe['time'] - pd.Timedelta(minutes=time)
    
    return align_dataframe


