import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

def encode_features(df, columns=None, method="one_hot"):
    """
    Encodes categorical features in a DataFrame.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.
    - columns (list, optional): List of categorical columns to encode. If None, detects all categorical columns.
    - method (str, optional): Encoding method ("one_hot" or "label"). Default is "one_hot".

    Returns:
    - pd.DataFrame: Encoded DataFrame.
    """
    df = df.copy()

    # Detect categorical columns if none are specified
    if columns is None:
        columns = df.select_dtypes(include=["category", "object"]).columns.tolist()

    if not columns:
        print("⚠️ No categorical columns found for encoding.")
        return df

    for col in columns:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in DataFrame.")

        if df[col].dtype not in ["object", "category"]:
            raise TypeError(f"Column '{col}' is not categorical and cannot be encoded.")

        if method == "one_hot":
            # One-Hot Encoding
            encoder = OneHotEncoder(sparse_output=False, drop="first")

            encoded = encoder.fit_transform(df[[col]])
            encoded_df = pd.DataFrame(encoded, columns=[f"{col}_{val}" for val in encoder.categories_[0][1:]])

            df = df.drop(columns=[col])
            df = pd.concat([df, encoded_df], axis=1)

        elif method == "label":
            # Label Encoding
            encoder = LabelEncoder()
            df[col] = encoder.fit_transform(df[col])

        else:
            raise ValueError("Invalid method. Choose 'one_hot' or 'label'.")

    return df
