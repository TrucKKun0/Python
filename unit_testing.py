
def add(x,y):
    """Adds two numbers together."""
    return x + y
def subtract(x,y):
    """Subtracts the second number from the first."""
    return x - y
def multiply(x,y):
    """Multiplies two numbers together."""
    return x * y
def divide(x,y):
    """Divides the first number by the second. Raises ValueError if dividing by zero."""
   
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
