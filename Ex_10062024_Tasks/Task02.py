# 1. Develop a Python script that calculates the square and cube of a given number.
# num = 2 sq - 4, c = 8
num = 2
sq = num ** 2
c = num ** 3
print(f'The Square of {num} is {sq}.')
print('The Cube of', num, 'is', c)

# 2. Create a program that takes two numbers as input and prints whether the first number is greater than,
# less than, or equal to the second number.
num1 = float(input("Enter the first number : \n"))
num2 = float(input("Enter the second number : \n"))
if num1 > num2:
    print(f'{num1} is greater than {num2}')
    print('The first number is greater than the second number.')
elif num1 < num2:
    print(f'{num1} is less than {num2}')
    print('The first number is less than the second number.')
else:
    print(f'{num1} is equal to {num2}')
    print('The first number is equal to the second number.')
