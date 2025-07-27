def probability_all_sixes(num_rolls):
    """
    Calculate the probability of getting a six on every die roll.

    Args:
    num_rolls (int): Number of times the die is rolled.

    Returns:
    float: Probability of getting a six on every roll.
    """
    if num_rolls < 1:
        return 0.0

    probability_single_roll = 1 / 6
    total_probability = probability_single_roll ** num_rolls
    return total_probability

# Example usage
rolls = int(input("Enter the number of rolls: "))
prob = probability_all_sixes(rolls)

print(f"The probability of getting a six on all {rolls} rolls is: {prob:.10f}")
