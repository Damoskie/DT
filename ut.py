import numpy as np

# Create an array
arr = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(arr)

# Reshape the array
reshaped_arr = arr.reshape((5, 1))
print("\nReshaped Array (5x1):")
print(reshaped_arr)

# Basic arithmetic operations
print("\nArray + 5:")
print(arr + 5)

print("\nArray * 2:")
print(arr * 2)

# Aggregate functions
print("\nSum of array elements:", np.sum(arr))
print("Mean of array:", np.mean(arr))
print("Max element:", np.max(arr))
print("Min element:", np.min(arr))

# Indexing and slicing
print("\nFirst element:", arr[0])
print("Last 3 elements:", arr[-3:])

# Logical operations
print("\nElements greater than 25:")
print(arr[arr > 25])

# Sorting
unsorted_arr = np.array([30, 10, 50, 20, 40])
sorted_arr = np.sort(unsorted_arr)
print("\nUnsorted array:")
print(unsorted_arr)
print("Sorted array:")
print(sorted_arr)
