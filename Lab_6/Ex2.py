# Making a list with if-statments using all if, eilf, and else.
# Kaili Takara
# September 27, 2026

# Create a list with a variety of values
my_list = [1, "apple", 3.5, True, "banana"]

# Check the length of the list
if len(my_list) < 5:
    print("The list has fewer than 5 elements.")
elif 5 <= len(my_list) <= 10:
    print("The list has between 5 and 10 elements (inclusive).")
else:
    print("The list has more than 10 elements.")

# Test with several different lengths
test_lists = [
    [],                          # 0 elements
    [1, "two", 3],              # 3 elements
    [1, 2, 3, 4, 5],            # 5 elements
    ["a", "b", "c", "d", "e", "f", "g"],   # 7 elements
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],      # 10 elements
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],  # 11 elements
    [True, False, "hi", 42, 3.14, "test", 7, 8, 9, 10, 11, 12]  # 12 elements
]

for items in test_lists:
    if len(items) < 5:
        print(f"{items} -> fewer than 5 elements")
    elif 5 <= len(items) <= 10:
        print(f"{items} -> between 5 and 10 elements")
    else:
        print(f"{items} -> more than 10 elements")