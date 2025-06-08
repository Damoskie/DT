import pandas as pd

# Load your dataset (replace 'your_dataset.csv' with the actual path)
df = pd.read_csv('your_dataset.csv')

# Step 1: Identify null values
print("Null values in each column:")
print(df.isnull().sum())

# Step 2: Report percentage of nulls
print("\nPercentage of missing values in each column:")
print(df.isnull().mean() * 100)

# Step 3: Handling null values

# Option A: Drop rows with any null values
df_dropped = df.dropna()
print("\nShape after dropping rows with nulls:", df_dropped.shape)

# Option B: Fill nulls with default values (mean for numeric, mode for categorical)
df_filled = df.copy()
for col in df.columns:
    if df[col].dtype in ['float64', 'int64']:
        df_filled[col].fillna(df[col].mean(), inplace=True)
    else:
        df_filled[col].fillna(df[col].mode()[0], inplace=True)
print("\nNulls filled with mean/mode.")

# Option C: Add a missing flag column for each column with nulls (optional)
df_flagged = df.copy()
for col in df.columns:
    if df[col].isnull().any():
        df_flagged[f'{col}_was_missing'] = df[col].isnull()

# Save the processed dataset if needed
# df_filled.to_csv('processed_dataset.csv', index=False)

# Choose which processed DataFrame to use for further analysis
# e.g., df = df_filled
