# Factorial
import math

num = int(input("Enter a number: \n"))
# 5! = 5*4*3*2*1 = 120

result = math.factorial(num)
print(result)

factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i

print(factorial)

fact = 1

while num > 0:
    fact = fact * num
    num = num - 1

print(fact)

