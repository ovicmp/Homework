from decorator import uppercase
from decorator import register
from decorator import safe_addition
import traceback


@safe_addition
def addition(a, b):
    print(a + b)


@register
def list_append_function():
    print("print_registry")


@uppercase
def greet(name):
    return f"Greetings {name}!"


def __main__():
    print(greet("world"))
    list_append_function()
    addition(0, 2.2)


__main__()

