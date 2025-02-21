import re
import pandas as pd
from nltk.corpus import stopwords
import nltk

# Download stopwords if not already downloaded
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(df, columns, lowercase=True, remove_special_chars=True, remove_numbers=True, remove_stopwords=False):
    df_cleaned = df.copy()

    for col in columns:
        if col not in df_cleaned.columns:
            raise ValueError(f"Column '{col}' not found in DataFrame.")

        df_cleaned[col] = df_cleaned[col].astype(str)  # Ensure text format

        if lowercase:
            df_cleaned[col] = df_cleaned[col].str.lower()

        if remove_special_chars:
            df_cleaned[col] = df_cleaned[col].apply(lambda x: re.sub(r"[^a-zA-Z0-9\s]", "", x))  # Remove special characters

        if remove_numbers:
            df_cleaned[col] = df_cleaned[col].apply(lambda x: re.sub(r"\d+", "", x))  # Remove numbers

        if remove_stopwords:
            df_cleaned[col] = df_cleaned[col].apply(lambda x: " ".join([word for word in x.split() if word not in stop_words]))  # Remove stopwords

        #if remove_emoji_flag:  # ✅ Fix: Ensure function is called properly
         #  df_cleaned[col] = df_cleaned[col].apply(remove_emoji_flag)  # Apply function directly

    return df_cleaned

