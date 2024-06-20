# String
# Bunch of characters together
# Anything between single quotes is a string in python

print('Hello World')
print("Hello World")
name = 'Hari'
print(name)
name = "Hari"
print(name)
name = " " "Hari's full name is Hari Shivapriya. She is a Testing Engineer" " "
print(name)
print(type(name))
# raw String
dir = r'C:\/nomedir\some dir'
print(dir)
first_name = "Hari"
last_name = "Shivapriya"
full_name = first_name + " " + last_name
print(full_name)
print(type(full_name))
print(first_name + "" + last_name)
print(first_name, last_name)
print(type(first_name), type(last_name))
print("Hello, " + first_name + " " + last_name)
print(f'Your fullname is {first_name} {last_name}')
# String formatting
print("Hello, {} {}".format(first_name, last_name))
