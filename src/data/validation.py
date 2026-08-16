import pandas as pd


def has_missing_rows(data, time_column):
    """
    Returns True if there are missing rows in the data based on the time column.
    """
    total_rows = len(data)
    total_hours = int((data[time_column].max() - data[time_column].min() + pd.Timedelta(hours=1)) / pd.Timedelta(hours=1))
    return total_hours - total_rows != 0


def get_duplicate_rows(data, time_column):
    """
    Returns the duplicate rows in the data based on the time column.
    """
    return data[data[time_column].duplicated(keep=False)]


def has_timestamp_gaps(data, time_column):    
    """
    Returns True if there are timestamp gaps in the data based on the sorted time column.
    """
    data = data.sort_values(by=time_column)
    time_diffs = data[time_column].diff()
    gap_rows = data[(time_diffs != pd.Timedelta(hours=1)) & (time_diffs.notna())]
    return not gap_rows.empty