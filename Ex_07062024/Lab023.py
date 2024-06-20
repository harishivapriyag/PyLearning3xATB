# List
# List in Python is a collection of items which can be of different data types.
# List is mutable, which means items can be added, removed, or modified in-place.
# List elements are enclosed in square brackets [].
# List elements can be of any data type, including other lists.

# Creating a list
# Empty list
l = []
# This is a list of integers
l = [1, 2, 3, 4, 5]
print(l)

shopping_list = ["apple", "banana", "cherry", "milk"]
print(shopping_list)
print(type(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])
print(shopping_list[1:3])
print(len(shopping_list))
shopping_list.append("mango")
print(shopping_list)
shopping_list.remove("banana")
print(shopping_list)
shopping_list.pop(2)
print(shopping_list)
shopping_list.insert(2, "jackfruit")
print(shopping_list)
shopping_list.extend(["orange", "grapes"])
print(shopping_list)
shopping_list.sort()
print(shopping_list)
print(shopping_list.index("mango"))
shopping_list.reverse()
print(shopping_list)

# Different data types in a list
lst = [1, 2.5, "Hello", [4, 5], (6, 7)]
print(lst)
print(type(lst))
print(lst[2])
print(lst[-1])
print(lst[3][1])
print(lst[4][0])