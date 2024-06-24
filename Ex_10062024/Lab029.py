# Arithmetic Operators
# This function takes two numbers as input and returns their sum, difference, product, and quotient.
# +, -, *, /, % are the arithmetic operators
a = 10
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(87 % 10)
print(87//10)
print(a**2)
r = pow(3, 2)
print(r)

def arithmetic_operators(a, b):
    """
    Performs basic arithmetic operations on two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        tuple: A tuple containing the sum, difference, product, and quotient of the two numbers.
    """
    sum_result = a + b
    diff_result = a - b
    product_result = a * b
    quotient_result = a / b if b != 0 else None

    return sum_result, diff_result, product_result, quotient_result
# def arithmetic_operators(a, b):
#     """
#     Performs basic arithmetic operations on two numbers
#     """
#
#     sum = a + b
#     diff = a - b
#     product = a * b
#     quotient = a / b
#
#     return sum, diff, product, quotient
