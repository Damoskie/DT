import pandas as pd

# Function to load the dataset
def load_data(file_path):
    try:
        # Read the dataset
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Function to identify variable types
def identify_variable_types(data):
    return data.dtypes

# Function to calculate statistical measures for specified features
def calculate_statistics(data, features):
    stats = {}
    
    for feature in features:
        if feature in data.columns:
            feature_data = data[feature]
            stats[feature] = {
                "mean": feature_data.mean(),
                "median": feature_data.median(),
                "mode": feature_data.mode()[0]  # Mode returns a series, so we pick the first value
            }
        else:
            stats[feature] = "Feature not found in dataset"
    
    return stats

# Example usage
def main():
    # Specify the path to your dataset
    file_path = 'your_dataset.csv'
    
    # Load the data
    data = load_data(file_path)
    
    if data is not None:
        # Identify the types of variables
        var_types = identify_variable_types(data)
        print("Variable Types:")
        print(var_types)
        
        # Specify the features you want to analyze
        features_to_analyze = ['feature1', 'feature2', 'feature3']  # Replace with actual feature names
        
        # Calculate statistical measures
        stats = calculate_statistics(data, features_to_analyze)
        print("\nStatistical Measures:")
        print(stats)

# Run the main function
if __name__ == '__main__':
    main()
