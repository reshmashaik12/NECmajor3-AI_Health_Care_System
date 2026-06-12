import pandas as pd

def clean_dataframe(df):

    df = df.copy()

    df.drop_duplicates(
        inplace=True
    )

    df.fillna(
        0,
        inplace=True
    )

    return df


def split_features_target(
    df,
    target_column
):

    X = df.drop(
        target_column,
        axis=1
    )

    y = df[target_column]

    return X, y