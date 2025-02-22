from functools import wraps
from itertools import pairwise
from typing import Any

import pandas as pd


def timestamp_to_int(timestamp: pd.Timestamp) -> int:
    return int(timestamp.timestamp() * 1000)


def preprocess_dict(
    data: dict,
    int_datetime_columns: set = None,
    str_datetime_columns: set = None,
    str_float_columns: set = None,
) -> dict:
    for key, value in data.items():
        if int_datetime_columns and (key in int_datetime_columns):
            data[key] = pd.Timestamp(value, unit="ms")
        elif str_datetime_columns and (key in str_datetime_columns):
            data[key] = pd.Timestamp(value)
        elif str_float_columns and (key in str_float_columns):
            data[key] = float(value)
    return data


def calculate_intervals(
    start_date: pd.Timestamp,
    end_date: pd.Timestamp,
    timeframe: str = "1h",
) -> int:
    return int((end_date - start_date) / pd.Timedelta(timeframe))


def expand_dict_columns(data: pd.DataFrame) -> pd.DataFrame:
    data = data.reset_index(drop=True)
    dict_columns = [
        x for x in data.columns if all(data[x].apply(lambda y: isinstance(y, dict)))
    ]
    columns_list = [data.drop(columns=dict_columns).copy()]
    for dict_column in dict_columns:
        exploded_column = pd.json_normalize(data[dict_column])
        exploded_column.columns = [
            f"{dict_column}.{x}" for x in exploded_column.columns
        ]
        columns_list.append(exploded_column.copy())
    return pd.concat(columns_list, axis=1)


def now() -> pd.Timestamp:
    return pd.Timestamp.now(tz="UTC")


def print_markdown(message: Any) -> None:
    if isinstance(message, pd.DataFrame):
        print(message.to_markdown(index=False))
    else:
        print(message)


def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = now()
        result = func(*args, **kwargs)
        end_time = now()
        elapsed_time = end_time - start_time
        print(f"{end_time}: Function {func.__name__} executed in {elapsed_time}.")
        return result

    return wrapper
