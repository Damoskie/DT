def longest_consecutive_ones(n):
    # Convert the number to its binary representation and remove the '0b' prefix
    binary_rep = bin(n)[2:]
    
    # Initialize variables to track the longest sequence of 1's
    max_count = 0
    current_count = 0
    
    # Iterate over each character in the binary representation
    for bit in binary_rep:
        if bit == '1':
            # If the bit is '1', increment the current sequence count
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            # Reset current count if bit is '0'
            current_count = 0
            
    return max_count

# Test the function
number = int(input("Enter a number: "))
print("Longest consecutive 1's:", longest_consecutive_ones(number))
