# open a file using "with"
# Kaili Takara
# October 21, 2026

with open("names.txdt", "r") as file_object:
    print(type(file_object))

print("file is closed:", file_object.closed)