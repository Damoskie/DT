# Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Dataset (Adjust the file path accordingly)
df = pd.read_csv("your_dataset.csv")  # or pd.read_excel("your_dataset.xlsx")

# 1. Data Overview
print("First 5 rows of the dataset:")
print(df.head())

# Checking for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Data types and basic stats
print("\nData Types and Summary Stats:")
print(df.info())
print(df.describe())

# 2. Univariate Analysis - Distribution of numerical features
# Histograms
df.hist(figsize=(12, 10), bins=20)
plt.suptitle("Histograms of Numerical Features")
plt.show()

# Boxplots to detect outliers
numeric_cols = df.select_dtypes(include=np.number).columns
for col in numeric_cols:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()

# 3. Bivariate Analysis - Relationships between variables
# Correlation heatmap for numerical features
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# Pairplot for a subset of numerical features
sns.pairplot(df[numeric_cols], kind="scatter")
plt.suptitle("Pairplot of Numerical Features")
plt.show()

# 4. Categorical Data Visualization (If applicable)
categorical_cols = df.select_dtypes(include=["object"]).columns
for col in categorical_cols:
    plt.figure(figsize=(8, 5))
    sns.countplot(x=df[col], palette="Set2")
    plt.title(f"Countplot of {col}")
    plt.xticks(rotation=45)
    plt.show()

# 5. Correlation Matrix with Heatmap (for deeper insights into relationships)
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()

# 6. Pairplots (for a few important features based on correlation/interest)
sns.pairplot(df[['column1', 'column2', 'column3']])
plt.show()

# If your dataset contains a target variable (e.g., in supervised learning tasks):
# Visualizing Target Variable Distribution (if it's numerical)
if "target_column" in df.columns:  # Replace target_column with your actual column name
    plt.figure(figsize=(6, 4))
    sns.histplot(df['target_column'], kde=True, color='blue')
    plt.title('Target Variable Distribution')
    plt.show()

# 7. Custom Visualizations: You can create any specific plots based on analysis
# Example: Visualize relationship between two specific features
sns.scatterplot(x=df['column1'], y=df['column2'])
plt.title("Scatterplot of column1 vs column2")
plt.show()
