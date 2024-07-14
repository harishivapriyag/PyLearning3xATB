# Write a program to find a Factorial of a given number
# Factorial
# n = 5
#
# # 5! -->5*4*3*2*1 -> 120
#
# # 3! -> 3*2*1 -> 6
#
# # 4! -> 4*3*2*1 -> 24
# 1 #using for loop
n = int(input("Enter a number: \n"))
fact = 1
for i in range(1, n + 1):
    fact = fact * i

print(fact)
print("The factorial of", n, "is", fact)

# 2 # using while loop
num = int(input("Enter a number: \n"))
f = 1
while num > 0:
    f = f * num
    num = num - 1

print(f)
print("The factorial of", num, "is", f)

# 3 # Input number
number = int(input("Enter a number:"))

# Initialize factorial to 1 (since factorial of 0 is 1)
factorial = 1

# Check if the number is negative, zero, or positive
if number < 0:
    print("Factorial does not exist for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    # Use a while loop to calculate the factorial
    i = 1
    while i <= number:
        factorial *= i
        i += 1

# Print the result
print(f"The factorial of {number} is {factorial}.")

# 4 # Using while loop
Num = int(input("Enter number: "))
Fact = 1
while Num > 0:
    Fact = Fact * Num
    Num = Num - 1

print(Fact)

# 5 # Using for loop
Num2 = int(input("Enter number: "))
Fact1 = 1
for i in range(1, Num2 + 1):
    Fact1 = Fact1 * i
    print(i, end=' ')
    if i < Num2:
        print("*", end=' ')

print("\nFactorial: ", Fact1)

# 6 # Input number
number = int(input("Enter a number:"))

# Initialize factorial to 1 (since factorial of 0 is 1)
factorial = 1

# Check if the number is negative, zero, or positive
if number < 0:
    print("Factorial does not exist for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    # Use a for loop to calculate the factorial
    for i in range(1, number + 1):
        factorial *= i

# Print the result
print(f"The factorial of {number} is {factorial}.")
