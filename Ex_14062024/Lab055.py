browser = input("Enter the browser name : \n")
# browser = 'chrome'
browser = browser.lower()
match browser:
    case "chrome":
        print("Execute the code of the chrome browser")
    case "edge":
        print("Execute the code of the edge browser")
    case "firefox":
        print("Execute the code of the firefox browser")
    case _:
        print("No idea")
