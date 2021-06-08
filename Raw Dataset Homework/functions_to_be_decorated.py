# from decorator import uppercase
# from decorator import register
# from decorator import safe_addition
from decorator import *


@uppercase
@register
def greet(name):
    return f"Greetings {name}!"


@register
def say_hello(name):
    return f"Hello {name}!"


@register
def say_goodbye(name):
    return f"Goodbye {name}!"


@safe_addition
def addition(a, b):
    print(a + b)


@safe_divide
def divide(a, b):
    return a / b


def __main__():
    print(greet("world"))
    say_hello('name')
    say_goodbye('name')
    print(f'@register used on functions:  {print_registry}')
    addition(0, 2)
    print(f'Divide a / b {divide(22, 2)}')
    print(f'Divide a / b {divide(26, 0)}')


__main__()
