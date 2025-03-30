def find_substrings(s):
    substrings = []
    
    # Loop through the string to get substrings of all lengths
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    
    return substrings

# Example usage
input_string = "abc"
substrings = find_substrings(input_string)

print("All substrings of the string:", input_string)
print(substrings)
