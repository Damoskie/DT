import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset (using Seaborn's built-in iris dataset for demonstration)
df = sns.load_dataset('iris')

# Data Exploration: Preview the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Summary of the dataset
print("\nSummary of the dataset:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Data Operations with Numpy & Pandas
# Compute mean and median of numerical columns using Numpy and Pandas
mean = df.mean()
median = df.median()

print("\nMean of the dataset:")
print(mean)
print("\nMedian of the dataset:")
print(median)

# Standard deviation
std_dev = df.std()
print("\nStandard Deviation of the dataset:")
print(std_dev)

# Correlation matrix (for numerical columns)
correlation = df.corr()
print("\nCorrelation Matrix:")
print(correlation)

# Visualization using Seaborn and Matplotlib

# 1. Histogram of the numerical features
plt.figure(figsize=(10, 6))
sns.histplot(df['sepal_length'], kde=True, bins=15)
plt.title('Histogram of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# 2. Pairplot (scatter plot matrix)
sns.pairplot(df, hue='species')
plt.suptitle('Pairplot of Iris Dataset', y=1.02)
plt.show()

# 3. Boxplot to visualize distribution of Sepal Length by Species
plt.figure(figsize=(8, 6))
sns.boxplot(x='species', y='sepal_length', data=df)
plt.title('Boxplot of Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Sepal Length')
plt.show()

# 4. Heatmap of the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# 5. Scatter plot between Sepal Length and Sepal Width
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=df)
plt.title('Scatter Plot of Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()

