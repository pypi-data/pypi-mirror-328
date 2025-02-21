import pandas as pd
from conversion import convert_data_types
from feature_split import split_features
from missing_values import handle_missing_values

# Sample test DataFrame with missing values
data = {
    "Age": [25, 30, 22, 40, None, 35, None, 50, 29, None],
    "Salary": [50000, 60000, None, 80000, 70000, None, 90000, None, 72000, 58000],
    "Department": ["HR", "Finance", "IT", "IT", None, "IT", "Sales", "HR", "IT", "Marketing"],
    "Review": ["Great product!", "Worst experience!!!", "Would buy again.", None, "Fantastic experience.", "Just okay.", "Not good 😡", "Nice deal.", "Loved it!", "Superb."]
}

df_test = pd.DataFrame(data)

# Convert data types first
df_converted = convert_data_types(df_test)

# Split numeric & categorical
df_numeric, df_categorical = split_features(df_converted)

# Apply missing value handling (Default: Median)
df_numeric_filled, df_categorical_filled = handle_missing_values(df_numeric, df_categorical, numeric_strategy="median")

# Print results
print("\n✅ Numeric Features After Handling Missing Values:")
print(df_numeric_filled)

print("\n✅ Categorical Features After Handling Missing Values:")
print(df_categorical_filled)
