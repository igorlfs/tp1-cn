import pandas as pd
from numpy import ndarray
from sklearn.preprocessing import normalize


# Inspired by https://stackoverflow.com/questions/26414913/normalize-columns-of-a-dataframe
def split_df_data_label(df: pd.DataFrame) -> tuple[pd.DataFrame, ndarray, int]:
    """Split a dataframe into `data` and `label`, where the `data` is normalized.

    Assumes `label` is the last column.
    For the `data`, use max normalization for each column.
    """
    df_norm = pd.DataFrame()
    for column in df.columns[:-1]:
        norm = normalize(pd.DataFrame(df[column]), norm="max", axis=0).flatten()  # pyright: ignore[reportAttributeAccessIssue]
        df_norm[column] = norm
    return df_norm, df[df.columns[-1]].to_numpy(), len(df[df.columns[-1]].unique())
