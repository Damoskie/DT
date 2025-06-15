import matplotlib.pyplot as plt

# Sample data: Categories and their respective counts
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [15, 30, 45, 10]

# Creating the bar chart
plt.bar(categories, values, color=['blue', 'green', 'orange', 'red'])

# Adding titles and labels
plt.title('Bar Chart of Categories')
plt.xlabel('Categories')
plt.ylabel('Values')

# Display the plot
plt.show()
