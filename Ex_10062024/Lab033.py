# Program to calculate the area of the circle
# input --> radius of the circle
# output --> area of the circle
# datatypes
# input --> int or float - float
# output - float
# formula or logic --> pi*r*r
# pi = 3.14

import math
radius = float(input("Enter the radius of the circle: "))
radius = float(radius)
area = math.pi * radius ** 2
print(math.pi)
print("The area of the circle is:", area)
area2 = math.pi*(math.pow(radius, 2))
print("The area of the circle is:", area2)
