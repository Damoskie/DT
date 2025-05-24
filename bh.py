import pandas as pd
import matplotlib.pyplot as plt

def visualize_database(csv_file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Display basic info
    print("Data Overview:")
    print(df.head())
    print("\nData Types:")
    print(df.dtypes)

    # Plot histograms for numerical columns
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    for col in num_cols:
        plt.figure(figsize=(8, 5))
        df[col].hist(bins=30, edgecolor='black')
        plt.title(f'Histogram of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.grid(False)
        plt.tight_layout()
        plt.show()

    # Bar plots for categorical columns
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    for col in cat_cols:
        plt.figure(figsize=(10, 5))
        df[col].value_counts().plot(kind='bar')
        plt.title(f'Bar Chart of {col}')
        plt.xlabel(col)
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # Correlation matrix heatmap
    if len(num_cols) > 1:
        import seaborn as sns
        corr = df[num_cols].corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Matrix')
        plt.tight_layout()
        plt.show()

    # Scatter plots between numerical pairs (limited to first 2 for simplicity)
    if len(num_cols) >= 2:
        plt.figure(figsize=(8, 6))
        plt.scatter(df[num_cols[0]], df[num_cols[1]], alpha=0.5)
        plt.title(f'Scatter Plot: {num_cols[0]} vs {num_cols[1]}')
        plt.xlabel(num_cols[0])
        plt.ylabel(num_cols[1])
        plt.tight_layout()
        plt.show()

# Example usage:
# visualize_database('your_data.csv')
