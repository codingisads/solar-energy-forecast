import pandas as pd
import pvlib

from src.config import ELEVATION, LATITUDE, LONGITUDE


def get_sun_positioned_dataframe(df):
    sun_position_data =get_sun_position(df.index + pd.Timedelta(minutes=30)) #We add +30 minutes because the timestamp of the data is the beginning of the hour, but pvlib calculates the sun position at the middle of the hour
    sun_position_data.index = df.index #Otherwise, the index of sun_position_data is the timestamp of the middle of the hour, not the beginning of the hour
    result = pd.concat([df, sun_position_data], axis = 1)
    return result

def get_sun_position(timestamp):

    return pvlib.solarposition.get_solarposition(time=timestamp, latitude=LATITUDE, longitude=LONGITUDE, altitude=ELEVATION)

