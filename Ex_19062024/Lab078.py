def sum_two(a, b):
    return a + b


o_p = sum_two(1, 9)
print(o_p)

o = lambda a, b: a + b
print(o(5, 8))


# Lambda expression is not possible in this below case
def sum(x, y):
    x = x + y
    y = x - y
    return x


sum(6, 2)
