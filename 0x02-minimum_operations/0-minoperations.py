#!/usr/bin/python3


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n 'H' characters.

    Args:
    - n (int): The target number of 'H' characters.

    Returns:
    - int: The minimum number of operations required.
    """
    # Base case: if n is less than or equal to 1, no operations needed
    if n <= 1:
        return 0

    # Initialize the total number of operations
    operations = 0
    # Initialize the divisor to check for prime factorization
    divisor = 2

    # Loop until n becomes 1
    while n > 1:
        # Check if the current divisor is a factor of n
        while n % divisor == 0:
            # Add the divisor to the total number of operations
            operations += divisor
            # Update n by dividing it by the divisor
            n //= divisor
        # Move to the next divisor
        divisor += 1

    # Return the total number of operations
    return operations

# Run the following code only if this script is executed, not imported
if __name__ == "__main__":
    # Test cases
    n1 = 4
    n2 = 12

    # Calculate and print the results for the test cases
    result1 = minOperations(n1)
    result2 = minOperations(n2)

    print("Min # of operations to reach {} char: {}".format(n1, result1))
    print("Min # of operations to reach {} char: {}".format(n2, result2))
