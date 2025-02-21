import numpy as np
import pandas as pd


def date_time_column_to_int(data: pd.Series) -> int:
    return (data.astype(int) / 1e6).astype(int)


def preprocess_dataframe(
    data: pd.DataFrame,
    int_datetime_columns: set = None,
    str_datetime_columns: set = None,
    numeric_columns: set = None,
    str_bool_columns: set = None,
) -> pd.DataFrame:
    if int_datetime_columns:
        datetime_columns_to_convert = [
            x for x in data.columns if x in int_datetime_columns
        ]
        data[datetime_columns_to_convert] = (
            data[datetime_columns_to_convert]
            .apply(pd.to_numeric)
            .apply(pd.to_datetime, unit="ms")
            .apply(lambda x: x.dt.tz_localize("UTC"))
        )
    if str_datetime_columns:
        datetime_columns_to_convert = [
            x for x in data.columns if x in str_datetime_columns
        ]
        data[datetime_columns_to_convert] = (
            data[datetime_columns_to_convert]
            .apply(pd.to_datetime)
            .apply(lambda x: x.dt.tz_localize("UTC"))
        )
    if numeric_columns:
        numeric_columns_to_convert = [x for x in data.columns if x in numeric_columns]
        data[numeric_columns_to_convert] = data[numeric_columns_to_convert].apply(
            pd.to_numeric
        )
    if str_bool_columns:
        bool_columns_to_convert = [x for x in data.columns if x in str_bool_columns]
        data[bool_columns_to_convert] = data[bool_columns_to_convert].astype(bool)
    return data


def create_buy_and_sell_orders(
    orders: pd.DataFrame, sides: tuple = ("BUY", "SELL")
) -> pd.DataFrame:
    dfs = []
    data = orders.copy()
    for side in sides:
        data["side"] = side
        dfs.append(data.copy())
    return pd.concat(dfs)


def floor_series(data: pd.Series, digits: int = 0) -> pd.Series:
    return np.floor(data * 10**digits) / 10**digits


def ceil_series(data: pd.Series, digits: int = 0) -> pd.Series:
    return np.ceil(data * 10**digits) / 10**digits
