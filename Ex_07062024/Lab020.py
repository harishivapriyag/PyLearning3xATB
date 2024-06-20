# In built functions in Python
# Functions are a way to organize the code and reuse it
# Functions are defined using the def keyword
# def my_function():
#     print("Hello from a function")

# Functions are used to perform a specific task
# Functions can take parameters as input
# Functions can return values
# Functions can be nested (one function inside another function)
# Examples of python built-in functions:
# print(), type(), input(), int(), str(), float(), len(), range(), etc.
name = "Harini"
print(name)
print(type(name))
print(len(name))
print(id(name))

name = "hari shivapriya"
name = name.lower()
print(name)

name = name.upper()
print(name)

name = name.capitalize()
print(name)

name = name.title()
print(name)
print(name.isalpha())

c = name.count("a")
print(c)
print(name[7])
print(name[0:7])
# IndexError: string index out of range
# print(name[18])
# TypeError: 'str' object does not support item assignment
# name [7]  = "b"
