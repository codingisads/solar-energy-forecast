from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_ROOT / 'data' / 'raw'
PROCESSED_DATA_DIR = PROJECT_ROOT / 'data' / 'processed'

"""
File name constants
"""

PVGIS_DATA_FILENAME = 'irradiance_pvgis_timeseries_dataset_2005_2023.csv'
COPERNICUS_DATA_FILENAME = 'cloudiness_copernicus_reanalysis-era5-single-levels-timeseries.csv'

TIMEZONE_STR = 'Europe/Madrid'
RANGE_MIN_DATE = '2006-01-01 00:00:00'
RANGE_MAX_DATE = '2023-12-31 23:59:59'

SECONDS_PER_HOUR = 3600.0