# Ex8.py
# Kaili Takara
# Date: Sept 11, 2026
# This file demonstrates a generic temperature conversion function that
# takes another conversion function as an argument.

# Base conversion functions

def c_to_f(celsius):
    return (celsius * 9 / 5) + 32


def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def c_to_k(celsius):
    return celsius + 273.15


def k_to_c(kelvin):
    return kelvin - 273.15


# Convenience conversion functions

def f_to_k(fahrenheit):
    return c_to_k(f_to_c(fahrenheit))


def k_to_f(kelvin):
    return c_to_f(k_to_c(kelvin))


# Generic conversion function
# It accepts a conversion function, then applies it to a value.
def convert_temperature(value, conversion_function):
    return conversion_function(value)


# Example usage
print("Celsius to Fahrenheit:", convert_temperature(0, c_to_f))
print("Fahrenheit to Celsius:", convert_temperature(32, f_to_c))
print("Celsius to Kelvin:", convert_temperature(0, c_to_k))
print("Kelvin to Celsius:", convert_temperature(273.15, k_to_c))

# Optional convenience examples
print("Fahrenheit to Kelvin:", convert_temperature(32, f_to_k))
print("Kelvin to Fahrenheit:", convert_temperature(273.15, k_to_f))

# Assessment:
# Pros of this design:
# - One reusable function can handle many conversions.
# - The code is more flexible because the conversion logic is passed in.
# - It is easy to add new conversion functions later.
#
# Cons of this design:
# - It is a little more abstract than writing a separate converter for each case.
# - The function call can be less obvious to someone reading the code for the first time.
# - Some of the extra helper functions are optional and may feel redundant.
#
# When this implementation is preferable:
# - When you want one general-purpose wrapper for multiple conversions.
# - When the conversion logic may grow over time.
# - When you want a consistent pattern for calling different conversion functions.
#
# Were all individual conversion functions necessary?
# - The four base functions (c_to_f, f_to_c, c_to_k, k_to_c) are necessary because
#   they contain the actual formulas.
# - The two convenience functions (f_to_k, k_to_f) are optional because they can be
#   built from the base conversions, but they can improve readability.
#
# Design lesson:
# - Generic functions are powerful, but they should be used when they make the code
#   clearer and more reusable.
# - Simple, direct functions are often better when the program is small and the
#   logic is easy to read.
