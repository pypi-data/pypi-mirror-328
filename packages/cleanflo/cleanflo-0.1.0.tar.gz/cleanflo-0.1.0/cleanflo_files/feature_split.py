import pandas as pd

def split_features(df):
    """
    Splits DataFrame into numeric and categorical features.

    Parameters:
    df (pd.DataFrame): Input DataFrame.

    Returns:
    tuple: (numeric_features_df, categorical_features_df)
    """
    # Ensure data types are correct before splitting
    df = df.copy()

    # Select only numeric and categorical features
    numeric_features = df.select_dtypes(include=["int", "float"])
    categorical_features = df.select_dtypes(include=["category"])

    return numeric_features, categorical_features
