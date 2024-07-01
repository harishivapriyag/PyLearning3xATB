# Conditions and Loop
# age > 18 # allowed to vote
# age < 18 # not allowed to vote
# harini --> age is above 18 --> allow to vote
# harini --> age is less than 18 --> not allow to vote
# If, else syntax
# # if condition :
#      code to be executed if condition is true
# # else :
#      code to be executed if condition is false
# Write a program to get user input and let the user know whether able to vote
# Take a user input
age = int(input("Enter your age : \n"))
if age > 18:
    print("Allowed to vote")
    print("Please vote")
else:
    print("Not allowed to vote")
    print("Please come back in {0} years".format(18 - age))
