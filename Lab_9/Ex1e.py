# Read the entire file and print the number of names
# Kaili Takara
# October 21, 2026

with open("names.txt", "r") as file_object:
    names = file_object.readlines()
    print(f"Number of names: {len(names)}")
    for name in names:
        print(name.strip())
        