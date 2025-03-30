def reverse_bits(n):
    # Initialize result
    result = 0
    # Calculate number of bits in the given number
    num_bits = n.bit_length()

    # Traverse through all bits of n
    for i in range(num_bits):
        # Shift the result to the left by 1
        result <<= 1
        # Get the last bit of n and add it to result
        result |= (n & 1)
        # Shift n to the right by 1
        n >>= 1
    
    return result

# Example usage:
num = int(input("Enter a number: "))
reversed_num = reverse_bits(num)
print(f"The number after reversing its bits is: {reversed_num}")
