# Fibonacci series
# 0,0+1, 0+1+1,

# n = 7

# 0, 1, 2, 3, 5, 8, 13


# Input number of terms
num_terms = int(input("Enter the number of terms: \n"))

# First two terms of the Fibonacci sequence
a, b = 0, 1

# Initialize the counter
count = 0

# Check if the number of terms is valid
if num_terms <= 0:
    print("Please enter a positive integer.")
elif num_terms == 1:
    print(f"Fibonacci sequence up to {num_terms} term:")
    print(a)
else:
    print(f"Fibonacci sequence up to {num_terms} terms:")
    while count < num_terms:
        print(a, end=' ')
        nth = a + b
        # Update values
        a = b
        b = nth
        count += 1
