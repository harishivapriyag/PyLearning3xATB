def allowed_to_enter_python_class(name):
    match name:
        case "Harini":
            print("Harini is allowed!!")
        case "Hari":
            print("Hari is allowed!!")
        case "Priya":
            print("Priya is allowed!!")
        case _:
            print("You are not allowed!")


allowed_to_enter_python_class("Harini")
