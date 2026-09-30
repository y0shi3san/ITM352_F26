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

# Test with several lists and their expected categories.
test_cases = [
    [[], "fewer than 5 elements"],
    [[1, "two", 3], "fewer than 5 elements"],
    [[1, 2, 3, 4, 5], "between 5 and 10 elements"],
    [["a", "b", "c", "d", "e", "f", "g"], "between 5 and 10 elements"],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "between 5 and 10 elements"],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], "more than 10 elements"],
    [[True, False, "hi", 42, 3.14, "test", 7, 8, 9, 10, 11, 12], "more than 10 elements"]
]

for items, expected in test_cases:
    if len(items) < 5:
        result = "fewer than 5 elements"
    elif 5 <= len(items) <= 10:
        result = "between 5 and 10 elements"
    else:
        result = "more than 10 elements"

    assert result == expected
    print(f"{items} -> {result}")