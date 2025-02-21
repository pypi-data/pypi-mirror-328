import pandas as pd
from cleanflo.outliers import handle_outliers

# Sample test DataFrame
df = pd.DataFrame({
    "Age": [25, 30, 22, 40, 100, 28, 32, 27, 150, 29],
    "Salary": [50000, 60000, 70000, 80000, 120000, 55000, 65000, 58000, 250000, 72000],
    "Department": ["HR", "Finance", "IT", "IT", "Sales", "HR", "Marketing", "IT", "Finance", "HR"]
})

print("✅ No Outlier Handling:")
print(df)

# 1️⃣ Default Modified Z-score (All Numeric Columns)
df_modified_all = handle_outliers(df.copy())
print("\n✅ Modified Z-score (All Numeric Columns):")
print(df_modified_all)

# 2️⃣ Default Z-score (All Numeric Columns)
df_zscore_all = handle_outliers(df.copy(), method="z-score")
print("\n✅ Z-score (All Numeric Columns):")
print(df_zscore_all)

# 3️⃣ Modified Z-score (Only Age Column)
df_modified_age = handle_outliers(df.copy(), columns=["Age"], method="modified_z-score")
print("\n✅ Modified Z-score (Only Age Column):")
print(df_modified_age)

# 4️⃣ Z-score (Only Salary Column)
df_zscore_salary = handle_outliers(df.copy(), columns=["Salary"], method="z-score")
print("\n✅ Z-score (Only Salary Column):")
print(df_zscore_salary)

# 5️⃣ Custom Threshold for Modified Z-score
df_custom_threshold = handle_outliers(df.copy(), method="modified_z-score", threshold=1.5)
print("\n✅ Modified Z-score with Custom Threshold (1.5):")
print(df_custom_threshold)

# 6️⃣ Custom Threshold for Z-score
df_custom_threshold_zscore = handle_outliers(df.copy(), method="z-score", threshold=3.0)
print("\n✅ Z-score with Custom Threshold (3.0):")
print(df_custom_threshold_zscore)

# 7️⃣ Invalid Column Name (Should Raise an Error)
try:
    df_invalid = handle_outliers(df.copy(), columns=["Invalid_Column"])
except ValueError as e:
    print("\n⚠️ Error:", e)

# 8️⃣ Invalid Method Name (Should Raise an Error)
try:
    df_invalid_method = handle_outliers(df.copy(), method="invalid_method")
except ValueError as e:
    print("\n⚠️ Error:", e)

# 9️⃣ Invalid Threshold Value (Should Raise an Error)
try:
    df_invalid_threshold = handle_outliers(df.copy(), method="z-score", threshold=-1)
except ValueError as e:
    print("\n⚠️ Error:", e)
