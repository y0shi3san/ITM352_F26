# open a file using "with"
# Kaili Takara
# October 21, 2026

with open("names.txt", "r") as file_object:
    print(type(file_object))

print("File is closed:", file_object.closed)