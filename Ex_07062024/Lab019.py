# Format String
print(2*4)
num = 25
print(f'The number is {num}')
print("The number is {}".format(num*2))
print("The number is", num*3)

num = 7
print(f"{num}*1={num}")
print(f"{num}*2={num*2}")
print(f"{num}*3={num*3}")
print(f"{num}*10={num*10}")
print(f"{num}*7={num*7}")
print(f"{num}*8={num*8}")
print(f"{num}*9={num*9}")
print(f"{num}*4={num*4}")

b = 1
print(f"{b}*1={b}")
print("b*3=b")
print("4*{}={}".format(b, b*4))
# Here we used empty curly braces to represent the user entered value in a string
print("5*{}={},{}".format(b, b*5, 3))
print("6*{}={}".format(b, b*6))
print("7*{}={}".format(b, b*7))
