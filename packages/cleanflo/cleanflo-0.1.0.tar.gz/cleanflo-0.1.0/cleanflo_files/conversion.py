import pandas as pd

def convert_data_types(df):
    """
    Convert DataFrame columns to appropriate data types:
    - Numeric columns → int or float
    - Categorical columns → category

    Parameters:
    df (pd.DataFrame): Input DataFrame.

    Returns:
    pd.DataFrame: DataFrame with correct data types.
    """
    df = df.copy()  # Ensure original DataFrame is not modified

    # Identify numeric columns
    numeric_cols = df.select_dtypes(include=["int", "float"]).columns

    # Convert categorical columns
    categorical_cols = df.select_dtypes(include=["object"]).columns

    # Convert numeric columns properly
    for col in numeric_cols:
        if pd.api.types.is_float_dtype(df[col]):
            df[col] = df[col].astype(float)
        else:
            df[col] = df[col].astype(int)

    # Convert categorical columns properly
    for col in categorical_cols:
        df[col] = df[col].astype("category")

    return df
