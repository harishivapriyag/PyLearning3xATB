# Take the 2 int numbers from the user and add the numbers
# Here, we use the input() function
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
# '+' used for concatenation of string
# result = num1+num2 - so it's displaying the string not the number
# type conversion --str -->int -> ? int()
# '+' - int --> sum operation (addition)
# '+' - str --> concatenation
# int to str --> str()
# str to int --> int()
result = int(num1) + int(num2)
print(result)
print(type(num1))
print(type(num2))
print(type(result))
print("The sum of " + num1 + " and " + num2 + " is " + str(result) + ".")
print(type(int(num1)))
print(type(int(num2)))
print(type(str(result)))
