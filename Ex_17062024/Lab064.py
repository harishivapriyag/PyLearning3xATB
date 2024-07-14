# *args means the 'n' number of arguments

print("Hari", "Shiva", "Priya", "Harini", sep="\n")


def sum(a=1, b=1, c=1):
    return a + b + c


result = sum(2, 5, 7)
print(result)
r1 = sum(5)
print(r1)
r2 = sum(a=10, b=52, c=63)
print(r2)
r3 = sum(a=4, b=9)
print(r3)
r4 = sum(c=6, b=31, a=55)
print(r4)
print(r1, r2, r3, r4, result)
