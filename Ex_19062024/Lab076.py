# List is a collection of items

numbers = [1, 2, 3, 4]


def do_something(numbers):
    numbers.append(7)
    numbers[0] = 100
    return numbers


l = do_something(numbers)
print(l)

h_list = [1, 7, 29, 1999, 25, 15]


def do_anything(harini_list):
    harini_list.append(9)
    harini_list[0] = 31
    return harini_list


h_list.append(27)
b = do_anything(h_list)
print(b)
