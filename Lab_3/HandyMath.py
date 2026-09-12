# HandyMath.py
# Kaili Takara
# Date: Sept 11, 2026

# Returns the value halfway between two numbers
def midpoint(num1, num2):
    return (num1 + num2) / 2

# Returns the square root of a number
def squareroot(number):
    return number ** 0.5

# Returns the absolute value of a number
def absolute_value(number):
    if number < 0:
        return -number
    return number

# Returns the larger of two numbers
def max(num1, num2):
    if num1 >= num2:
        return num1
    return num2

# Returns the smaller of two numbers
def min(num1, num2):
    if num1 <= num2:
        return num1
    return num2

# Backward-compatible aliases

def maximum(num1, num2):
    return max(num1, num2)


def minimum(num1, num2):
    return min(num1, num2)


# Returns a formatted string describing the result of applying a function to x and y
# Example: function_name can be a function object such as min, max, or lambda x, y: x ** y
# It uses __name__ to get the function's identifier for display.
def function_result(x, y, func):
    result = func(x, y)
    return f"The function {func.__name__} x,y = {result}"
