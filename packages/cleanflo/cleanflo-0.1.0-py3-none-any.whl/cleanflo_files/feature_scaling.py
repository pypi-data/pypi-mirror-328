import numpy as np
import pandas as pd

def apply_scaling(df, method="standard", columns=None, c=1):
    """
    Applies feature scaling to numeric columns.

    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - method (str): Scaling method - "standard" (default), "minmax", "log".
    - columns (list): List of numeric columns to apply scaling to. If None, all numeric columns are used.
    - c (float): Constant for log scaling (default=1).

    Returns:
    - pd.DataFrame: Scaled DataFrame.
    """
    df = df.copy()

    # Select numeric columns
    if columns is None:
        columns = df.select_dtypes(include=["number"]).columns.tolist()

    for col in columns:
        if col not in df.columns or not np.issubdtype(df[col].dtype, np.number):
            raise ValueError(f"Column '{col}' is not numeric and cannot be scaled.")

    # Apply scaling
    if method == "standard":
        df[columns] = (df[columns] - df[columns].mean()) / df[columns].std()

    elif method == "minmax":
        df[columns] = (df[columns] - df[columns].min()) / (df[columns].max() - df[columns].min())

    elif method == "log":
        df[columns] = np.log(df[columns] + c)

    else:
        raise ValueError("Invalid method. Choose 'standard', 'minmax', or 'log'.")

    return df
