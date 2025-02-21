# 🚀 cleanflo: A Lightweight Data Cleaning Library

*cleanflo* is a Python package designed to *automate data cleaning* tasks such as:
- Handling missing values ✅
- Detecting and treating outliers ✅
- Feature scaling (Standardization, Min-Max, Log Scaling) ✅
- Encoding categorical features (One-Hot, Label Encoding) ✅
- Text cleaning (lowercasing, removing special characters, stopwords) ✅

## 📌 1. Installation
To install cleanflo, use:
```sh
pip install cleanflo

## 📌 2. Quick Start
import pandas as pd
from cleanflo import cleanflo_pipeline

# Sample DataFrame
df = pd.DataFrame({
    "Age": [25, 30, None, 40, 50],
    "Salary": [50000, 60000, 70000, None, 90000],
    "Department": ["HR", "Finance", "IT", "IT", "Sales"],
    "Review": ["Great product!", "Worst experience!!!", "Just okay.", "Loved it!", "Nice deal."]
})

# Apply the full cleaning pipeline
df_cleaned = cleanflo_pipeline(
    df,
    handle_missing=True,
    outlier_columns=["Age", "Salary"],
    scale_columns=["Salary"],
    encode_columns=["Department"],
    text_clean_columns=["Review"]
)

print(df_cleaned)