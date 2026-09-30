# This program prompts the user to enter a weight in pounds and thens
# converts it to kilograms and displays the result in one line of code
# Kaili Takara
# Sept. 4, 2026

#print("The weight in Kilograms is: ",float(input("Enter weight in pounds:"))*0.453592)

KG_TO_POUNDS = 0.453592
weight_in_pounds = input("Enter weight in pounds:")
weight_in_pounds_float = float(weight_in_pounds)
weight_in_kilograms = weight_in_pounds_float * KG_TO_POUNDS

print("The weight you entered:", weight_in_pounds_float)

