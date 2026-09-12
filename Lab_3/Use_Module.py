# Use_Module.py
# Kaili Takara
# Date: Sept 11, 2026
# This script imports functions from HandyMath.py,
# gets two numbers from the user, and prints several
# formatted math results using f-strings.

from HandyMath import midpoint, squareroot, maximum, minimum

# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate and display the midpoint
mid = midpoint(num1, num2)
print(f"The midpoint of {num1} and {num2} is {mid}.")

# Calculate the square root of the square of one number
# This shows the square root of num1 squared, using the module function.
sq_root_of_square = squareroot(num1 ** 2)
print(f"The square root of {num1} squared is {sq_root_of_square}.")

# Raise one number to the exponent of the other
power_result = num1 ** num2
print(f"{num1} raised to the exponent {num2} is {power_result}.")

# Display the maximum and minimum values
max_num = maximum(num1, num2)
min_num = minimum(num1, num2)
print(f"The maximum of the two numbers is {max_num}.")
print(f"The minimum of the two numbers is {min_num}.")
