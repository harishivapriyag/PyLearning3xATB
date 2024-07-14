def f1(a, b, c):
    print(a, b, c)
    return a + b + c
    print("This code will be executed!")


print("End!!")

result = f1(3, 4, 2)
print(result)
result1 = f1(a=5, b=6, c=9)
print(result1)
result2 = f1(c=12, a=45, b=16)
print(result2)
print(f1(31, 1, 1999))
