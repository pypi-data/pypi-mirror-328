import pandas as pd
from .conversion import convert_data_types
from .feature_split import split_features
from .missing_values import handle_missing_values
from .outliers import handle_outliers
from .feature_scaling import apply_scaling
from .feature_encoding import encode_features
from .text_cleaning import clean_text


def cleanflo_pipeline(
    df,
    handle_missing=True,
    missing_strategy="median",  # Default strategy for missing values
    outlier_columns=None,
    outlier_method="modified_zscore",
    outlier_threshold=3.5,
    scale_columns=None,
    scale_method="standard",
    scale_c=1.0,
    encode_columns=None,
    encode_method="one_hot",
    text_clean_columns=None,
    text_lowercase=True,
    text_remove_special_chars=True,  # ✅ FIXED: Corrected from `remove_special`
    text_remove_numbers=True,
    text_remove_stopwords=True,
):
    """
    Processes a DataFrame through a series of data cleaning and preprocessing steps.

    Parameters:
    - df (DataFrame): The input DataFrame
    - handle_missing (bool): Whether to handle missing values
    - missing_strategy (str): Strategy to handle missing values ('mean', 'median', 'mode')
    - outlier_columns (list): Columns to apply outlier handling
    - outlier_method (str): Method for outlier detection ('zscore', 'modified_zscore')
    - outlier_threshold (float): Threshold for outlier detection
    - scale_columns (list): Columns to apply feature scaling
    - scale_method (str): Method for feature scaling ('standard', 'minmax', 'log')
    - scale_c (float): Constant for log scaling
    - encode_columns (list): Columns to apply encoding
    - encode_method (str): Encoding method ('one_hot', 'label')
    - text_clean_columns (list): Columns to apply text cleaning
    - text_lowercase (bool): Convert text to lowercase
    - text_remove_special_chars (bool): Remove special characters
    - text_remove_numbers (bool): Remove numbers
    - text_remove_stopwords (bool): Remove stopwords

    Returns:
    - DataFrame: Processed DataFrame
    """

    # ✅ Step 1: Convert Data Types
    df = convert_data_types(df)

    # ✅ Step 2: Split Numeric & Categorical Features
    df_numeric, df_categorical = split_features(df)

    # ✅ Step 3: Handle Missing Values
    if handle_missing:
        df_numeric, df_categorical = handle_missing_values(df_numeric, df_categorical, numeric_strategy=missing_strategy)

    # ✅ Step 4: Numeric Processing (Outliers → Scaling)
    if outlier_columns or scale_columns:
        if outlier_columns:
            df_numeric = handle_outliers(df_numeric, columns=outlier_columns, method=outlier_method, threshold=outlier_threshold)
        if scale_columns:
            df_numeric = apply_scaling(df_numeric, method=scale_method, columns=scale_columns, c=scale_c)

    # ✅ Step 5: Categorical Processing (Text Cleaning → Encoding)
    if text_clean_columns or encode_columns:
        if text_clean_columns:
            df_categorical = clean_text(
                df_categorical,
                columns=text_clean_columns,
                lowercase=text_lowercase,
                remove_special_chars=text_remove_special_chars,  # ✅ FIXED: Corrected parameter name
                remove_numbers=text_remove_numbers,
                remove_stopwords=text_remove_stopwords,
            )
        if encode_columns:
            df_categorical = encode_features(df_categorical, columns=encode_columns, method=encode_method)

    # ✅ Step 6: Merge Processed Data Back Together
    df_final = pd.concat([df_numeric, df_categorical], axis=1)

    return df_final
