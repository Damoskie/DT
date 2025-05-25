import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load your dataset (replace with your dataset path)
# For example, if you're using seaborn's built-in dataset:
# df = sns.load_dataset('tips')

# If you have a CSV file:
# df = pd.read_csv('your_dataset.csv')

# Display the first few rows of the dataset to understand its structure
print(df.head())

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# 1. Distribution of a single variable (Histogram)
def plot_distribution(df, column):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True, bins=30)
    plt.title(f'Distribution of {column}')
    plt.show()

# 2. Pairplot (Pairwise relationships in the dataset)
def plot_pairplot(df):
    plt.figure(figsize=(10, 6))
    sns.pairplot(df)
    plt.show()

# 3. Heatmap for correlation between numeric variables
def plot_heatmap(df):
    plt.figure(figsize=(12, 8))
    corr = df.corr()  # Calculate the correlation matrix
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=1)
    plt.title('Correlation Heatmap')
    plt.show()

# 4. Boxplot (For showing distributions and detecting outliers)
def plot_boxplot(df, column, by=None):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=by, y=column, data=df)
    plt.title(f'Boxplot of {column} by {by}')
    plt.show()

# 5. Scatterplot (Visualizing the relationship between two variables)
def plot_scatter(df, x_column, y_column):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df[x_column], y=df[y_column])
    plt.title(f'Scatterplot: {x_column} vs {y_column}')
    plt.show()

# 6. Violin Plot (Distribution of data and comparisons between categories)
def plot_violin(df, column, by):
    plt.figure(figsize=(10, 6))
    sns.violinplot(x=by, y=column, data=df)
    plt.title(f'Violin plot of {column} by {by}')
    plt.show()

# Example usage of the functions
# 1. Plot distribution for a column (e.g., 'total_bill' if you are using the 'tips' dataset)
plot_distribution(df, 'total_bill')

# 2. Plot pairplot
plot_pairplot(df)

# 3. Plot correlation heatmap
plot_heatmap(df)

# 4. Plot boxplot
plot_boxplot(df, 'total_bill', by='sex')

# 5. Plot scatterplot
plot_scatter(df, 'total_bill', 'tip')

# 6. Plot violin plot
plot_violin(df, 'total_bill', by='sex')
