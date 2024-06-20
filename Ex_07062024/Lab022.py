value = None
# This will assign the value None to the variable 'value'
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
# value = value + 10
# This will raise a TypeError because None is not a numeric type
# To handle this, we can use a conditional statement to check if the value is None

value = None
if value is None:
    print("Value is None")

# None is a special value in Python that represents the absence of a value or a null value.
# It is used in conditional statements, loops, and other contexts where a value is expected but not necessarily present.

# Example usage of None
def some_function():
    # This function doesn't return any value
    pass

#   In this case, we don't need to check if the return value is None because there is no return value
result = some_function()
if result is None:
    print("Function returned None")

# None means nothing.
# This is NoneType of DataType
# None is not '0'
# None is not a 'False'
# None is not an empty string
# None is not a default value

Name = None
print(Name)
print(type(Name))
print(id(Name))
Name = "Hari"
print(Name)
print(type(Name))
print(id(Name))
