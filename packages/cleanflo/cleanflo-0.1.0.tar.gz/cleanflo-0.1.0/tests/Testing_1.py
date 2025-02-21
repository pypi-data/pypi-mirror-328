import pandas as pd
from cleanflo import cleanflo_pipeline

# 🔹 Load the CSV File
df = pd.read_csv("C:/Users/admin/OneDrive/Desktop/cleanflo/tests/test_titatnicspaceship_1.csv")  # Replace with actual file name

# 🔹 Process the Data Using cleanflo_pipeline
df_cleaned = cleanflo_pipeline(
    df,
    handle_missing=True,  # Handle missing values
    outlier_columns=None,  # Handle outliers in all numeric columns
    outlier_method="modified_z-score",  # Default method
    scale_columns=["ShoppingMall"],  # Scale the "ShoppingMall" column
    scale_method="standard",  # Standard Scaling
    encode_columns=["VIP"],  # Encode "VIP" column
    encode_method="one_hot"  # One-Hot Encoding
)

# 🔹 Save or Print the Processed Data
print("✅ Processed DataFrame:")
print(df_cleaned.head())
df_cleaned.to_csv("processed_file.csv", index=False)
print("Unique values in VIP_1.0:", df_cleaned["VIP_1.0"].unique())
print("ShoppingMall values after scaling:")
print(df_cleaned["ShoppingMall"].head())
