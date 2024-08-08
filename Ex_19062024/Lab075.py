def outer_function():
    var1 = 20

    def inner_function():
        print(var1)

    inner_function()

    def inner_function1():
        print(var1)

    inner_function1()

    def inner_function2():
        var2 = 25
        print(var2)

    inner_function2()


outer_function()
