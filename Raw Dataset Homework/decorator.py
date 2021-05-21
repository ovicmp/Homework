def uppercase(function):
    def wrapper(*args):
        func = function(*args)
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


def register(func):
    def wrapper(*args):
        print_registry = ["@register", "@uppercase", "@safe_addition"]
        print(print_registry)
        value = func(*args)
        return value
    return wrapper


def safe_addition(fnc):
    # a,b are the first and second numbers for addition

    def inner(a, b):
        print("Adding the two numbers,a + b: ", a, "and", b)
        if isinstance(b, float):
            print("b is float, please use int")
        elif isinstance(a, float):
            print("a is float, please use int")
            return

        return fnc(a, b)
    return inner

