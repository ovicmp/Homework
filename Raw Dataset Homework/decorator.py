def uppercase(fcn):
    def wrapper():
        original = fcn
        modified = str(fcn).upper()
        return modified
    return wrapper()
