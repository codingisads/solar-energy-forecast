import pandas as pd


def load_raw_irradiance_data(filepath):

    raw_data = pd.read_csv(filepath, sep=',', encoding='utf-8', parse_dates=['time'], date_format='%Y%m%d:%H%M', skiprows=10, skipfooter=12, engine='python')

    return raw_data


def load_raw_cloudiness_data(filepath):

    raw_data = pd.read_csv(filepath, sep=',', encoding='utf-8', parse_dates=['valid_time'], date_format='%Y-%m-%d %H:%M:%S')

    return raw_data