import pandas as pd
from cleanflo.text_cleaning import clean_text

# Sample DataFrame for testing
data = {
    "Review": [
        "Great product! 😊", 
        "Worst experience!!!", 
        "Would buy again. #Awesome", 
        "Just okay. 123", 
        "Fantastic experience.",
        "Not good 😡", 
        "Nice deal. $$$", 
        "Loved it! 10/10", 
        "Average product. 🤔", 
        "Terrible service."
    ]
}
df = pd.DataFrame(data)

print("\n✅ No Text Cleaning Applied (Original DataFrame):")
print(df)

# 1️⃣ Lowercasing All Text
df_lower = clean_text(df, columns=["Review"], lowercase=True)
print("\n✅ Lowercasing Applied:")
print(df_lower)

# 2️⃣ Removing Special Characters
df_specials = clean_text(df, columns=["Review"], remove_special_chars=True)
print("\n✅ Special Characters Removed:")
print(df_specials)

# 3️⃣ Removing Numbers
df_numbers = clean_text(df, columns=["Review"], remove_numbers=True)
print("\n✅ Numbers Removed:")
print(df_numbers)

# 4️⃣ Removing Stopwords
df_stopwords = clean_text(df, columns=["Review"], remove_stopwords=True)
print("\n✅ Stopwords Removed:")
print(df_stopwords)

# 5️⃣ Removing Emojis


# 6️⃣ Applying All Cleaning Steps Together
df_all = clean_text(df, columns=["Review"], lowercase=True, remove_special_chars=True, remove_numbers=True, remove_stopwords=True)
print("\n✅ All Cleaning Steps Applied:")
print(df_all)

# 7️⃣ Error Handling (Passing Non-Text Column)
try:
    df_invalid = clean_text(df, columns=["Invalid_Column"], lowercase=True)
except ValueError as e:
    print("\n⚠️ Error:", e)
