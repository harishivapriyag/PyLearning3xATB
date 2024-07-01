# Write a program that calculates and displays the letter
# Given numeric score (E.g. A, B, C, D, F)
# Based on the following scale
# A : 90 - 100
# B : 80 - 89
# C : 70 - 79
# D : 60 - 69
# F : 0 - 59
# score = 99
# output = A
# step 1 : logic building
# Input --> score
# type --> int
score = int(input("Enter the score: \n"))
# output --> str (A, B, C, D, F)
# To write rough logic and convert it into code
# if score >= 90 and score <= 100:
#     print("A")
# elif score >= 80 and score <= 89:
#     print("B")
# elif score >= 70 and score <= 79:
#     print("C")
# elif score >= 60 and score <= 69:
#     print("D")
# else:
#     print("F")
# step 2 : Refactoring the code
if score >= 90 and score <= 100:
    print("Your Grade is 'A' ")
    print(score)
elif score >= 80 and score <= 89:
    print("Your Grade is 'B' ")
    print(score)
elif score >= 70 and score <= 79:
    print("Your Grade is 'C' ")
    print(score)
elif score >= 60 and score <= 69:
    print("Your Grade is 'D' ")
    print(score)
elif score >= 0 and score <= 59:
    print("Your Grade is 'F' ")
    print(score)
else:
    print("Invalid score")
    print(score)
