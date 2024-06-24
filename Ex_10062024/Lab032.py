# Ternary operator
def ternary_operator(x, y, z):
    """
    Returns the maximum of three numbers using a ternary operator.
    """
    return x if x > y and x > z else y if y > z else z


x = 100
y = 200
# x > y --> False, y > z --> True

Hari_marks = 99
Pavi_marks = 100

print("Hari" if Hari_marks > Pavi_marks else "Pavi")

if Hari_marks > Pavi_marks:
    print("Hari is the Highest!")
else:
    print("Pavi is the Highest!")
