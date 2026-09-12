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
def maximum(num1, num2):
    if num1 >= num2:
        return num1
    return num2

# Returns the smaller of two numbers
def minimum(num1, num2):
    if num1 <= num2:
        return num1
    return num2
