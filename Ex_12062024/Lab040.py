# Multiple condition checking
x = 10
y = 20
z = 30
t = 40
result1 = (x > y)
print(result1) # False
result2 = (z < t)
print(result2) # True
result3 = result1 and result2
print(result3) # False
result4 = result1 or result2
print(result4) # True
