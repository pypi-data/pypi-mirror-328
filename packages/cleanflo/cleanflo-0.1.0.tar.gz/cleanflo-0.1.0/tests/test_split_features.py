import pandas as pd
from conversion import convert_data_types
from feature_split import split_features

# Sample test DataFrame
data = {
    "Age": [25, 30, 22, 40, 29, None, 45, 50, None, 27],
    "Salary": [50000, 60000, 70000, 80000, None, 75000, 90000, None, 72000, 58000],
    "Department": ["HR", "Finance", "IT", "IT", "Finance", "IT", "Sales", "HR", "IT", "Marketing"],
    "Review": ["Great product!", "Worst experience!!!", "Would buy again.", "Just okay.", None, "Fantastic experience.", "Not good 😡", "Nice deal.", "Loved it!", "Superb."],
}

df_test = pd.DataFrame(data)

# Apply type conversion first
df_converted = convert_data_types(df_test)

# Apply feature splitting
df_numeric, df_categorical = split_features(df_converted)

# Print results
print("\n✅ Numeric Features:")
print(df_numeric)

print("\n✅ Categorical Features:")
print(df_categorical)
