# 1. Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
#
#
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
#
# Use an if-else statement to make this determination.
#
#
# Input = 2024
#
# Output = Leap year
year = int(input("Enter a year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(year, "is a Leap year")
#         else:
#             print(year, "is not a leap year")
#     else:
#         print(year, "is a Leap year")
#         # print("Leap year")
# else:
#     print(year, "is not a leap year")

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap year")
else:
    print(year, "is not a leap year")
