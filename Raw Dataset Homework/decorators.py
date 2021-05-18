import decorator


@decorator.uppercase
def hello(name):
    print("Hello", name)


@decorator.uppercase
def greet(name):
    return "Greetings {}!".format(name)


print(greet("world"))
