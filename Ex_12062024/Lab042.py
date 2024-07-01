# Multiple conditions
# Problem to find the maximum number among three given numbers

# Function to find the maximum of three numbers
num1 = int(input("Enter the first number: \n"))
num2 = int(input("Enter the second number: \n"))
num3 = int(input("Enter the third number: \n"))

if num1 >= num2 and num1 >= num3:
    print(num1, "is the greatest")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is the greatest")
else:
    print(num3, "is the greatest")

# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2 > num1 and num2 > num3:
#     print(num2)
# else:
#     print(num3)
