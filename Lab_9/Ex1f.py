# open names.txt and read its contents
# append a new name at the end of the file
# Kaili Takara
# October 21, 2026

with open("names.txt", "a") as file_object:
    contents_list = file_object.readlines()
    print(contents_list)

with open("names.txt", "a") as file_object:
    print("Appending a new name to the file...")
    file_object.write("John Doe\n")

    