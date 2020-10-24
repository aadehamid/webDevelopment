# %%
def add(x, y):
    """Add Function"""
    if (type(x) or type(y)) not in [int, float]:
        raise TypeError("The inputs must be of type int or floats.")
    return x + y
# %%


def subtract(x, y):
    """Subtract Function"""
    if (type(x) or type(y)) not in [int, float]:
        raise TypeError("The inputs must be of type int or floats.")
    return (x - y)


def multiply(x, y):
    """Multiply Function"""
    if (type(x) or type(y)) not in [int, float]:
        raise TypeError(
            "The inputs must be of type int or floats. Please, change your input.")
    return x * y


def divide(x, y):
    """Divide Function in this container"""
    if (type(x) or type(y)) not in [int, float]:
        raise TypeError("The inputs must be of type int or floats.")
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

# %%
