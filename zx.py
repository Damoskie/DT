import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
# You can replace this with pd.read_csv('your_file.csv')
df = sns.load_dataset("iris")  # Example dataset

# Display basic information
print("Dataset Overview:")
print(df.head())
print("\nSummary Statistics:")
print(df.describe())

# 1. Pair Plot - Great for seeing distributions and pairwise relationships
sns.pairplot(df, hue=df.select_dtypes(include='object').columns[0] if df.select_dtypes(include='object').shape[1] > 0 else None)
plt.suptitle("Pairplot of Features", y=1.02)
plt.show()

# 2. Correlation Heatmap - Good for checking correlation between numerical variables
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# 3. Box Plots - For distribution and outliers across categories
categorical_cols = df.select_dtypes(include='object').columns
numerical_cols = df.select_dtypes(include='number').columns

if not categorical_cols.empty:
    for num_col in numerical_cols:
        plt.figure(figsize=(8, 4))
        sns.boxplot(x=categorical_cols[0], y=num_col, data=df)
        plt.title(f"Box Plot of {num_col} by {categorical_cols[0]}")
        plt.show()

# 4. Violin Plots - Combines boxplot and KDE
if not categorical_cols.empty:
    for num_col in numerical_cols:
        plt.figure(figsize=(8, 4))
        sns.violinplot(x=categorical_cols[0], y=num_col, data=df)
        plt.title(f"Violin Plot of {num_col} by {categorical_cols[0]}")
        plt.show()

# 5. Custom Scatter Plots (example with first two numerical columns)
if len(numerical_cols) >= 2:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=numerical_cols[0], y=numerical_cols[1], hue=categorical_cols[0] if not categorical_cols.empty else None, data=df)
    plt.title(f"Scatter Plot: {numerical_cols[0]} vs {numerical_cols[1]}")
    plt.show()
