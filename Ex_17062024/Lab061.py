# Functions are block of code which can be executed and reused
# Define
# Call

# Built-in Functions are created by python contributors

result = max(5, 6, 8, 7, 12)
print(result)


# User defined functions
# May return something --> Has Return type
# May not return anything ---> Has no return type
# Have parameters / arguments
# not have parameters / arguments
# Default arguments


def say_hello():
    print("Hello!")


say_hello()


# Argument with no return type
def say_hello_arg(name):
    print("Hello!", name)


say_hello_arg("Harini")
say_hello_arg("Hari")
say_hello_arg("Priya")
say_hello_arg("Shiva")


# Default argument with no return type
def say_hello_default_arg(name="Priya"):
    print("Hi!", name)


say_hello_default_arg()
say_hello_default_arg("Harini")
say_hello_default_arg(name="Shiva")


# Argument with Return type

def sum_num_arg_ret(a, b):
    return a + b


result = sum_num_arg_ret(4, 7)
result1 = sum_num_arg_ret(a=54, b=87)
result2 = sum_num_arg_ret(b=10, a=25)
print(result)
print(result1)
print(result2)
