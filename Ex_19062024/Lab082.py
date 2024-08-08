# List
# Collection of items
# Dupplicte is allowed

my_list = [1,2,3]
my_list1 = [1,True, False, "harini", 12.34]

# Indexing
print("Element at index 0: ", my_list[0])

# Changing element value
my_list[1] = 6
print("List after changing the element at index 1: \n", my_list)

# Append value
my_list.append(25)
print("List after appending : \n", my_list)

# Extend
my_list.extend([5,6])
print("List after extending the list : \n", my_list)

# Insert
my_list.insert(1, 'a')
print("List after inserting the list : \n", my_list)

# Remove
my_list.remove('a')
print("List after removing 'a' : \n", my_list)

# Copy List
my_copy_list = my_list.copy()
print(my_copy_list)

# Clear List
my_list.clear()
print("Initial List : \n", my_list)

print("Index of 3 in the list: ", my_list)

# Sorting
my_copy_list.sort()
print(my_copy_list)

# Reversing
my_copy_list.reverse()
print(my_copy_list)

# Print each element
print(my_copy_list[0])
print(my_copy_list[1])
print(my_copy_list[2])
print(my_copy_list[3])
print(my_copy_list[4])
