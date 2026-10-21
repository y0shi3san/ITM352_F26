# open file and read its contents
# Kaili Takara
# October 21, 2026

with open("names.txt", "r") as file_object:
    contents = file_object.read()
    print(contents)
    contents_list = contents.split(',')
    print(f"Number of names: {len(contents_list)}")
for name in contents_list:
    print(name)
