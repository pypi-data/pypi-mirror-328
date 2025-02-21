import pandas as pd
from cleanflo.feature_encoding import encode_features

# Sample DataFrame
data = {
    "Department": ["HR", "Finance", "IT", "Sales", "IT", "HR", "Marketing", "Finance", "IT", "HR"],
    "Review": ["Great", "Worst", "Okay", "Good", "Bad", "Excellent", "Poor", "Fair", "Nice", "Average"],
    "Age": [25, 30, 22, 40, 29, 35, 45, 50, 23, 27],  # Numeric column (should not be encoded)
}

df = pd.DataFrame(data)

print("\n✅ No Encoding Applied (Original DataFrame):")
print(df)

# 1️⃣ Test: One-Hot Encoding (All Categorical Columns)
df_one_hot_all = encode_features(df, method="one_hot")
print("\n✅ One-Hot Encoding (All Categorical Columns):")
print(df_one_hot_all)

# 2️⃣ Test: One-Hot Encoding (Only 'Department' Column)
df_one_hot_department = encode_features(df, columns=["Department"], method="one_hot")
print("\n✅ One-Hot Encoding (Only 'Department' Column):")
print(df_one_hot_department)

# 3️⃣ Test: Label Encoding (All Categorical Columns)
df_label_all = encode_features(df, method="label")
print("\n✅ Label Encoding (All Categorical Columns):")
print(df_label_all)

# 4️⃣ Test: Label Encoding (Only 'Review' Column)
df_label_review = encode_features(df, columns=["Review"], method="label")
print("\n✅ Label Encoding (Only 'Review' Column):")
print(df_label_review)

# 5️⃣ Test: Invalid Column Error (Passing Numeric Column)
try:
    df_invalid_column = encode_features(df, columns=["Age"], method="one_hot")
except TypeError as e:
    print(f"⚠️ Error: {e}")


# 6️⃣ Test: Invalid Encoding Method Error
try:
    df_invalid_method = encode_features(df, method="wrong_method")
except ValueError as e:
    print("\n⚠️ Error:", e)
