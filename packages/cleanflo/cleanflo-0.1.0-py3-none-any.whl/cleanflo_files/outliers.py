import numpy as np
import pandas as pd

def handle_outliers(df, columns=None, method="modified_z-score", threshold=2.0):
    """
    Detect and handle outliers in specified numeric columns.
    Parameters:
        df (pd.DataFrame): Input DataFrame.
        columns (list, optional): List of numeric columns to apply outlier detection. Default is all numeric columns.
        method (str, optional): "modified_z-score" (default) or "z-score".
        threshold (float, optional): Threshold for outlier detection. Default is 2.0.
    Returns:
        pd.DataFrame: DataFrame with outliers replaced by the median of the respective column.
    """
    df = df.copy()  # Avoid modifying the original DataFrame

    if columns is None:
        columns = df.select_dtypes(include=["number"]).columns.tolist()

    for col in columns:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in DataFrame.")

        if df[col].dtype not in [np.float64, np.int64]:
            raise ValueError(f"Column '{col}' is not numeric and cannot be processed.")

        median_value = df[col].median()

        if method == "z-score":
            mean_value = df[col].mean()
            std_dev = df[col].std()
            if std_dev == 0:
                continue
            z_scores = (df[col] - mean_value) / std_dev
            outliers = np.abs(z_scores) > threshold

        elif method == "modified_z-score":
            median_absolute_deviation = np.median(np.abs(df[col] - median_value))
            if median_absolute_deviation == 0:
                continue
            modified_z_scores = 0.6745 * (df[col] - median_value) / median_absolute_deviation
            outliers = np.abs(modified_z_scores) > threshold

        else:
            raise ValueError("Invalid method. Choose 'z-score' or 'modified_z-score'.")

        df.loc[outliers, col] = median_value.astype(df[col].dtype)
  # Replace outliers with median

    return df
