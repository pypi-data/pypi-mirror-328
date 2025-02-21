import pandas as pd
from cleanflo.feature_scaling import apply_scaling

# Sample test DataFrame
df = pd.DataFrame({
    "Age": [25, 30, 22, 40, 100, 28, 32, 27, 150, 29],
    "Salary": [50000, 60000, 70000, 80000, 120000, 55000, 65000, 58000, 250000, 72000],
    "Department": ["HR", "Finance", "IT", "IT", "Sales", "HR", "Marketing", "IT", "Finance", "HR"]
})

print("\n✅ No Scaling Applied:")
print(df)

print("\n✅ Standard Scaling:")
df_standard = apply_scaling(df, method="standard")
print(df_standard)

print("\n✅ Min-Max Scaling:")
df_minmax = apply_scaling(df, method="minmax")
print(df_minmax)

print("\n✅ Log Scaling (c=1):")
df_log = apply_scaling(df, method="log", c=1)
print(df_log)

print("\n✅ Min-Max Scaling (Only Age Column):")
df_minmax_age = apply_scaling(df, method="minmax", columns=["Age"])
print(df_minmax_age)

print("\n✅ Log Scaling (Only Salary Column, c=10):")
df_log_salary = apply_scaling(df, method="log", columns=["Salary"], c=10)
print(df_log_salary)

print("\n⚠️ Invalid Column Error (Passing non-numeric column):")
try:
    df_invalid = apply_scaling(df, columns=["Department"])
except ValueError as e:
    print("⚠️ Error:", e)

print("\n⚠️ Invalid Method Error (Passing wrong method):")
try:
    df_invalid_method = apply_scaling(df, method="wrong_method")
except ValueError as e:
    print("⚠️ Error:", e)
