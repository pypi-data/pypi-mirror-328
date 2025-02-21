import pandas as pd

def handle_missing_values(df_numeric, df_categorical, numeric_strategy="median"):
    """
    Handles missing values separately for numeric and categorical features.

    Parameters:
    - df_numeric (pd.DataFrame): Numeric features DataFrame.
    - df_categorical (pd.DataFrame): Categorical features DataFrame.
    - numeric_strategy (str): "mean" or "median" (default: "median").

    Returns:
    - tuple: (df_numeric, df_categorical) after handling missing values.
    """

    # ✅ Handle Missing Values for Numeric Features
    if numeric_strategy == "mean":
        df_numeric.fillna(df_numeric.mean(), inplace=True)
    elif numeric_strategy == "median":
        df_numeric.fillna(df_numeric.median(), inplace=True)
    else:
        raise ValueError("Invalid numeric_strategy. Choose 'mean' or 'median'.")

    # ✅ Handle Missing Values for Categorical Features (Always Fill with Mode)
    #for col in df_categorical.columns:
     #   df_categorical[col].fillna(df_categorical[col].mode()[0], inplace=True)

    df_categorical = df_categorical.apply(lambda col: col.fillna(col.mode()[0]), axis=0)

    return df_numeric, df_categorical
