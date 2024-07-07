# Api automation, 'match case' will be used
name = input("Enter the name : \n")
match name:
    case "Harini":
        print("You are Harini")
    case "Priya":
        print("You are Priya")
    case "Shiva":
        print("You are Shiva")
    case _:
        print("No idea")
