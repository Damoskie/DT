import pandas as pd

# Sample DataFrame creation
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'James'],
    'Age': [28, 22, 34, 42, 29],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'New York'],
    'Salary': [70000, 80000, 120000, 95000, 110000]
}

# Create a pandas DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# 1. Filter data where Age is greater than 30
filtered_df = df[df['Age'] > 30]
print("\nFiltered DataFrame (Age > 30):")
print(filtered_df)

# 2. Add a new column 'Salary Increase' (10% increase)
df['Salary Increase'] = df['Salary'] * 1.1
print("\nDataFrame with Salary Increase:")
print(df)

# 3. Group data by 'City' and calculate average salary
city_group = df.groupby('City')['Salary'].mean().reset_index()
print("\nAverage Salary by City:")
print(city_group)

# 4. Sort the DataFrame by 'Salary' in descending order
sorted_df = df.sort_values(by='Salary', ascending=False)
print("\nSorted DataFrame by Salary (Descending):")
print(sorted_df)

# 5. Drop the 'Salary Increase' column
df.drop('Salary Increase', axis=1, inplace=True)
print("\nDataFrame after dropping 'Salary Increase' column:")
print(df)
