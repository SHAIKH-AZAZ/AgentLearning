def explain_a_plus_b_whole_square(a, b):
"""
This function demonstrates the mathematical identity (a + b)^2 = a^2 + 2ab + b^2
using Python code for given values of a and b.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        None: Prints the results of both calculations.
    """

    print(f"Given a = {a} and b = {b}\n")

    # Method 1: Calculate (a + b) whole square directly
    result_direct = (a + b) * (a + b)
    # Alternatively: result_direct = (a + b)**2
    print(f"Calculating (a + b)^2 directly:")
    print(f"({a} + {b})^2 = ({a + b})^2 = {result_direct}")
    print("-" * 30)

    # Method 2: Calculate using the expanded form a^2 + 2ab + b^2
    a_squared = a * a
    b_squared = b * b
    two_ab = 2 * a * b
    result_expanded = a_squared + two_ab + b_squared

    print(f"Calculating a^2 + 2ab + b^2:")
    print(f"{a}^2 + 2 * {a} * {b} + {b}^2 = {a_squared} + {two_ab} + {b_squared} = {result_expanded}")
    print("-" * 30)

    # Verify if both results are equal
    if result_direct == result_expanded:
        print(f"As you can see, both results are equal: {result_direct} == {result_expanded}")
        print("This demonstrates that (a + b)^2 is indeed equal to a^2 + 2ab + b^2.")
    else:
        print(f"There was an unexpected difference: {result_direct} != {result_expanded}")

# Example usage:

# Let's take a = 5 and b = 3

explain_a_plus_b_whole_square(5, 3)

print("\n" + "=" \* 50 + "\n")

# Another example with different numbers

explain_a_plus_b_whole_square(10, 2)

print("\n" + "=" \* 50 + "\n")

# Example with negative number

explain_a_plus_b_whole_square(7, -3)
