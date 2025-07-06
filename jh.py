# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load the dataset and check the spread
def check_and_visualize_spread(data):
    # Check for null values in the dataset
    print("Null values in each column:")
    print(data.isnull().sum())
    
    # Describe the dataset to get basic statistics
    print("\nBasic statistics of the dataset:")
    print(data.describe())
    
    # Create histograms for each numeric feature
    print("\nCreating histograms for each numeric feature...")
    numeric_cols = data.select_dtypes(include=['number']).columns  # Get numeric columns
    data[numeric_cols].hist(bins=30, figsize=(15, 10), layout=(3, 3))
    plt.suptitle('Histogram of Numeric Features', fontsize=16)
    plt.show()
    
    # Create boxplots for each numeric feature
    print("\nCreating boxplots for each numeric feature...")
    for col in numeric_cols:
        plt.figure(figsize=(6, 4))
        sns.boxplot(data=data, x=col)
        plt.title(f'Boxplot of {col}', fontsize=14)
        plt.show()
    
    # Create pairplots to see pairwise relationships
    print("\nCreating pairplots to visualize relationships between features...")
    sns.pairplot(data[numeric_cols])
    plt.suptitle('Pairplot of Numeric Features', fontsize=16)
    plt.show()
    
    # Check correlation heatmap for the numeric features
    print("\nCreating correlation heatmap...")
    corr = data[numeric_cols].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Heatmap', fontsize=16)
    plt.show()

# Example usage
# Assuming 'data' is a pandas DataFrame containing your dataset
# data = pd.read_csv('path_to_your_dataset.csv')
# check_and_visualize_spread(data)
