# Take an input from  the user and print it to the console.

# Prompt the user to enter some text
user_input = input("Enter some text: ")
print(user_input)
print(type(user_input))

'''
Output:
Enter some text: Hello, World!
Hello, World!
<class 'str'>
'''
user_name = input("Enter your username: ")
print("Hello,", user_name)
'''
Output:
Enter your username: harini
Hello, harini
'''

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Hello, ", first_name, last_name)
'''
Output:
Enter your first name: Hari
Enter your last name: Shivapriya
Hello, Hari Shivapriya
'''
print("Your first name is ", first_name, "Your last name is ", last_name)
# Your first name is  Hari Your last name is  Shivapriya
