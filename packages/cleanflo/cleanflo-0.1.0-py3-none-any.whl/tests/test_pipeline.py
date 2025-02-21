import pandas as pd
from cleanflo.cleanflo_pipeline import cleanflo_pipeline

def test_pipeline():
    """Test the full pipeline with different scenarios."""
    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
        "Country": ["USA", "UK", "India", "Canada", "Germany"],
        "Age": [25, 30, None, 40, 22],
        "Salary": [50000, 60000, 70000, None, 80000],
        "MoneySpentInIMAX": [100, 200, None, 400, 500],
        "Movie Review": ["Great movie! 😊", "Worst experience!!!", "Would watch again.", "Just okay.", "Fantastic experience."],
    })
    
    print("\n✅ Original DataFrame:")
    print(df.head())
    
    # Full processing
    df_full = cleanflo_pipeline(
    df,
    handle_missing=True,
    outlier_method="z-score",
    outlier_columns=["Salary", "MoneySpentInIMAX"],
    scale_method="minmax",  # ✅ Corrected parameter name
    scale_columns=["Salary", "MoneySpentInIMAX"],
    text_clean_columns=["Movie Review"],
    encode_columns=["Country"],
    encode_method="one_hot",
)

    
    print("\n✅ Full Processing (All Steps Applied):")
    print(df_full.head())
    
    # Testing handling missing values only
    df_missing_values = cleanflo_pipeline(df, handle_missing=True, missing_strategy="median")
    print("\n✅ Missing Values Handled:")
    print(df_missing_values.head())
    
    # Testing Outlier Handling only
    df_outliers = cleanflo_pipeline(df, outlier_columns=["Age", "Salary"], outlier_method="z-score", outlier_threshold=2.0)
    print("\n✅ Outlier Handling (Z-score Applied):")
    print(df_outliers.head())
    
    # Testing Scaling only
    df_scaled = cleanflo_pipeline(df, scale_columns=["Salary"], scale_method="minmax")
    print("\n✅ Min-Max Scaling Applied (Only Salary):")
    print(df_scaled.head())
    
    # Testing Encoding only
    df_encoded = cleanflo_pipeline(df, encode_columns=["Country"], encode_method="label")
    print("\n✅ Label Encoding Applied (Only Country Column):")
    print(df_encoded.head())
    
    # Testing Invalid Column Case
    try:
        df_invalid = cleanflo_pipeline(df, encode_columns=["Invalid_Column"], encode_method="one_hot")
    except ValueError as e:
        print("\n⚠️ Error:", e)

if __name__ == "__main__":
    test_pipeline()
