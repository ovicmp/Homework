def uppercase(function):
    def wrapper(*args):
        func = function(*args)
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


def safe_addition(fnc):
    # a,b are the first and second numbers for addition

    def inner(a, b):
        print("Adding the two numbers, a + b: ", a, "and", b)
        if isinstance(b, float):
            print("b is type float, please use int")
        elif isinstance(a, float):
            print("a is type float, please use int")
            return

        return fnc(a, b)

    return inner


def safe_divide(func):
    def wrapper(a, b):
        try:
            function = func(a, b)
            return function
        except ZeroDivisionError:
            return 'Zero division error'
    return wrapper


print_registry = []


def register(func):
    global print_registry

    def wrapper(*args):
        value = func(*args)
        print_registry.append(func.__name__)
        return value

    return wrapper
