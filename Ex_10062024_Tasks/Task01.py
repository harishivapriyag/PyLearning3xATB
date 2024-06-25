# 1. Explain the difference between the = operator and the == operator in Python.
# In Python, the = operator and the == operator serve very different purposes
# Assignment Operator (=):
# Purpose: The = operator is used to assign a value to a variable.
# Function: It takes the value on the right-hand side and assigns it to the variable on the left-hand side.
# Example:
# Assigns the value 10 to the variable x
x = 7
# Assigns the string "Alice" to the variable name
name = "Harini"

# Equality Operator (==):
# Purpose: The == operator is used to compare two values for equality.
# Function: It evaluates to True if the values on both sides of the operator are equal, and False otherwise.
# Example:
a = 5
b = 5
c = 10
# The == operator is used to check if two values are equal.
print(a == b)  # True, because a and b are both 5
print(a == c)  # False, because a is 5 and c is 10
# Detailed Examples

x = 7  # Assigning a value to the variable x
if x == 7:  # Checking if x is equal to 7
    print("x is equal to 7")

name = "Harini"  # Assigning a string value to the variable name
if name == "Harini":  # Checking if the variable name has the value "Harini"
    print("Name is Harini")
    print(name)

# 2. What does the ** operator do in Python, and how is it used?
# The ** operator is used for exponentiation in Python.
# It takes two operands and raises the first operand to the power of the second operand.
# It raises the number on the left to the power of the number on the right.
# It works with both integers and floating-point numbers.
# It supports positive, negative, and fractional exponents.
# This operator is useful for performing power calculations, such as squaring or cubing a number,
# or raising a number to any other exponent.
# Example:
base = 2
exponent = 3
result = base ** exponent  # This will evaluate to 8 (2^3)
print("The result is :\n",result)  # Output: 8

# 3. What does the ^ operator do in Python, and in what context is it commonly used?
# The ^ operator is used for bitwise XOR operation in Python.
# It performs a bitwise exclusive OR operation on the two operands.
# This operator is commonly used in error handling, data encryption/decryption, and other bitwise operations.
# The XOR operator compares each bit of its operands.
# If the corresponding bits are the same, the result is 0. If the bits are different, the result is 1.
# Example:
a = 0b1100  # Binary representation of 12
b = 0b1010  # Binary representation of 10
result = a ^ b  # Performs bitwise XOR operation on 12 (1100) and 10 (1010)
print(bin(result))  # Output: 0b110
print(int(result)) # Output : 6
# The output is 0b110 because the XOR operation compares the binary representations of 12 and 10,
# and the result is 0b110 (6 in decimal). This is because the bits are different at the 3rd position,
# and the result is 1 where the bits are different, and 0 where they are the same.
# Another Example
num1 = 5  # binary: 0101
num2 = 9  # binary: 1001
ans = num1 ^ num2  # bitwise XOR operation  # binary: 0b1100 which is 12
print(ans)  # Output: 12
print(bin(ans))  # Output: 0b1100
