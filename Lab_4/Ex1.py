#Ask the user to enter their first name, middle intial, and last name, in a string.
# Kaili Takara
# Date: Sept 16, 2026

first = input("Enter your first name: ")
middle_inital = input("Enter your middle initial: ")
last = input("Enter your last name: ")

full_name = first + " " + middle_inital + ". " + last
print ("Your full name is: " + full_name)

print(f"Your full name using F-string is: {first} {middle_inital}. {last}")

print("Your full name using percent formating is: %s %s. %s" % (first, middle_inital, last))

print("Your full name using format method is: {} {}. {}".format(first, middle_inital, last))

print("your full name using list joins is: " + " ".join([first, middle_inital + ".", last]))