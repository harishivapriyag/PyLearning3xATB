# For loop
# 0 to 99 will be printed
for counter in range(0, 100):
    print(counter)

# 0 to 100 will be printed with even numbers only
# 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50,
# 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98
for counter in range(0, 101, 2):
    print(counter)

# 0 to 100 will be printed with odd numbers only
# 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51,
# 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99
for counter in range(1, 101, 2):
    print(counter)

# 5's table will be printed
for harini in range(0, 101, 5):
    print(harini)

# break statement
for counter in range(1, 10):
    print(counter)
    if counter == 5:
        break

print("Outside the loop")
