def print_argument(*args):
    print("Hello!")
    for i in args:
        print(i, end=" ")


# ["Hari", "Shiva", "Priya", "Harini"] - *args is similar to 'List'

print_argument("Hari", "Shiva", "Priya", "Harini")

a = ["Hari", "Shiva", "Priya", "Harini"]
for i in a:
    print(i, "\n")
