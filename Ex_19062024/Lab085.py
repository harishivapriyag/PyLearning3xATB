# Tuple
# Collection of items
# (1,2,3,4)

my_list = [1, 2, 3, 4, 5]
print(id(my_list))
my_list[0] = 31
print(my_list)
print(id(my_list))

# tuple objects cannot be changed, and they are immutable in nature
my_tuple = (1, 2, 3, 4, 5)
# my_tuple[1] = 99
# TypeError: 'tuple' object does not support item assignment
print(my_tuple)
