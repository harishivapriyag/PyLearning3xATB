def find_odd_even(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


find_odd_even(8)

f_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
print(f_even_odd(4))
