list1 = [1, 2, 3, 4, 5]
print(list1)
temp_list = []
print(temp_list)
for i in list1:
    temp = i * 2
    temp_list.append(temp)
print(temp_list)

list1 = [1, 2, 3, 4, 5]
print(list1)
temp_list = []
print(temp_list)
for i in list1:
    temp_list.append(i * 2)
print(temp_list)


def double_item(num):
    return num * 2


d = double_item(8)
print(d)

# Map()
# Takes each item from the list
# Executes a function on it
# Returns the same number of elements of the given list.

list2 = [1, 2, 3, 4, 5]

# def double(number):
#     return number **   2

double = lambda number: number ** 2

db = list(map(double, list2))
print(db)

db = list(map(lambda number: number ** 2, list2))
print(db)

print(list(map(lambda number: number ** 2, [10, 20, 30, 40, 50])))
