"""Python lists: a beginner-friendly introduction.

A list stores multiple values in one ordered, changeable collection. Lists are
useful when a program needs to keep track of related items, such as student
names, shopping items, or scores.
"""


# Create a list with square brackets. Lists can contain strings, numbers, or
# values of different types.
student_names = ["Maya", "Noah", "Zoe"]
scores = [88, 94, 76, 100]
mixed_list = ["Python", 3, True]
empty_list = []

print("Student names:", student_names)
print("Scores:", scores)
print("An empty list:", empty_list)


# Access elements by position. Python starts counting at index 0.
print("First student:", student_names[0])
print("Second student:", student_names[1])
print("Last score:", scores[-1])

# A slice accesses a range of elements. The ending index is not included.
print("First two scores:", scores[0:2])


# Add items to a list.
student_names.append("Liam")  # Add one item to the end.
student_names.insert(1, "Ava")  # Add an item at a specific index.
student_names.extend(["Eli", "Mia"])  # Add several items at once.
print("After adding names:", student_names)


# Remove items from a list.
student_names.remove("Noah")  # Remove the first matching value.
removed_name = student_names.pop()  # Remove and return the last item.
del student_names[0]  # Remove the item at index 0.
print("Removed name:", removed_name)
print("After removing names:", student_names)


# Practical example: manage a shopping list.
shopping_list = ["bread", "apples", "milk"]
shopping_list.append("eggs")
shopping_list.remove("bread")

print("Shopping list:", shopping_list)
print("I still need:", len(shopping_list), "items")

# Lists are useful with loops because a program can process every item.
for item in shopping_list:
	print("Buy:", item)


# Indexing and slicing lists.
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Positive indexing starts at 0 from the beginning of the list.
print("Index 0:", days[0])
print("Index 2:", days[2])

# Negative indexing starts at -1 from the end of the list.
print("Index -1:", days[-1])
print("Index -2:", days[-2])

# Slicing uses [start:stop]. The start is included, but stop is excluded.
print("First three days:", days[0:3])
print("Middle days:", days[2:5])

# Leaving out start or stop means "from the beginning" or "through the end."
print("First four days:", days[:4])
print("Last three days:", days[-3:])
print("Days after Tuesday:", days[2:])

# A third value sets the step: [start:stop:step].
print("Every other day:", days[::2])
print("Every other day starting Tuesday:", days[1::2])

# A negative step moves backward through the list.
print("Days in reverse:", days[::-1])
print("Last three days in reverse:", days[-1:-4:-1])


# Indexing returns one element. Slicing returns a new list.
weekend = days[-2:]
print("Weekend list:", weekend)
weekend[0] = "Saturday morning"
print("Updated weekend list:", weekend)
print("Original days list:", days)


# Indexing and slicing practice:
# 1. Print the fourth item using a positive index.
# 2. Print the fourth item from the end using a negative index.
# 3. Slice out Wednesday through Friday.
# 4. Create a list containing only Monday, Wednesday, and Friday.
# 5. Create a reversed copy of days using a slice.


# Important list methods and the len() function.
# len() is a built-in function, not technically a list method.
practice_numbers = [5, 2, 9, 1, 7]
print("Starting numbers:", practice_numbers)

practice_numbers.append(6)
print("append(6):", practice_numbers)

practice_numbers.insert(0, 10)
print("insert(0, 10):", practice_numbers)

practice_numbers.remove(2)
print("remove(2):", practice_numbers)

last_number = practice_numbers.pop()
print("pop() removed:", last_number)
print("After pop():", practice_numbers)

practice_numbers.sort()
print("sort():", practice_numbers)

practice_numbers.reverse()
print("reverse():", practice_numbers)

print("len():", len(practice_numbers), "items")


# Practice challenges:
# 1. Add 12 to practice_numbers.
# 2. Insert 8 at index 2.
# 3. Remove the number 5.
# 4. Pop an item and print the item that was removed.
# 5. Sort the list from smallest to largest.
# 6. Reverse the list and print its length.


# Strings are sequences of characters. They can be created with single or
# double quotation marks.
first_name = "Ava"
greeting = 'Hello'
print("String values:", first_name, greeting)

# Concatenation joins strings with the + operator.
full_greeting = greeting + ", " + first_name + "!"
print("Concatenation:", full_greeting)

# Repetition repeats a string with the * operator.
separator = "-" * 20
print("Repetition:", separator)


# Common string methods return a new string; they do not change the original.
message = "  Python is fun!  "
print("Original message:", repr(message))
print("upper():", message.upper())
print("lower():", message.lower())
print("strip():", message.strip())

# split() breaks a string into a list of smaller strings.
sentence = "Python lists are useful"
words = sentence.split()
print("split():", words)

# split() can also use a specific separator.
csv_line = "Maya,Noah,Zoe"
names_from_text = csv_line.split(",")
print("Names from text:", names_from_text)


# String practice:
# 1. Create a string containing your favorite food.
# 2. Concatenate it with the sentence "I like ____."
# 3. Repeat a short word three times.
# 4. Convert a string to uppercase and lowercase.
# 5. Strip extra spaces from "  practice  ".
# 6. Split "red blue green" into a list of three words.


# String formatting inserts values into a larger string.
product = "notebook"
quantity = 3
price = 4.5

# 1. Old-style formatting uses % placeholders.
old_style = "Product: %s | Quantity: %d | Price: $%.2f" % (product, quantity, price)
print("Old-style formatting:", old_style)

# 2. The .format() method uses {} placeholders.
format_method = "Product: {} | Quantity: {} | Price: ${:.2f}".format(
	product, quantity, price
)
print(".format() method:", format_method)

# .format() can use named placeholders, which makes the template clearer.
named_format = "{item} costs ${cost:.2f} each.".format(item=product, cost=price)
print("Named .format():", named_format)

# 3. F-strings place expressions inside braces after an f prefix.
f_string = f"Product: {product} | Quantity: {quantity} | Price: ${price:.2f}"
print("F-string:", f_string)

# F-strings can evaluate expressions directly.
total = quantity * price
print(f"Receipt: {quantity} {product}s cost ${total:.2f} total.")


# Formatting practice:
# 1. Create a name and age variable and format them using an f-string.
# 2. Format a decimal with exactly two digits after the decimal point.
# 3. Rewrite the receipt above using .format().
# 4. Rewrite the receipt above using old-style % formatting.


# Advanced string operations.
announcement = "Python makes text processing practical"

# find() returns the starting index of a substring, or -1 if it is not found.
python_position = announcement.find("Python")
missing_position = announcement.find("Java")
print("Position of Python:", python_position)
print("Position of Java:", missing_position)

# replace() returns a new string with matching text changed.
updated_announcement = announcement.replace("practical", "powerful")
print("Replaced text:", updated_announcement)
print("Original text:", announcement)

# String-property methods return True or False for the entire string.
user_id = "352"
user_name = "Takara"
mixed_value = "352A"
print("user_id is digits:", user_id.isdigit())
print("user_name is alphabetic:", user_name.isalpha())
print("mixed_value is digits:", mixed_value.isdigit())
print("mixed_value is alphabetic:", mixed_value.isalpha())

# Slicing strings uses the same [start:stop:step] pattern as list slicing.
course_code = "ITM352"
print("First three characters:", course_code[:3])
print("Last three characters:", course_code[-3:])
print("Characters at even indexes:", course_code[::2])
print("Reversed string:", course_code[::-1])


# Advanced string practice:
# 1. Find the position of "text" in "Practice makes text skills stronger".
# 2. Replace "bad" with "good" in "This is a bad example".
# 3. Test whether "12345" is made only of digits.
# 4. Test whether "Python" is made only of alphabetic characters.
# 5. Slice the first five characters from "Programming".
# 6. Reverse the string "exercise" with a slice.


# Lists and strings often work together to process text.
# split() converts a string into a list of strings.
sentence_text = "Python lists and strings"
sentence_words = sentence_text.split()
print("Words from sentence:", sentence_words)

# split() can use a separator such as a comma.
classmates_text = "Maya,Noah,Zoe"
classmates = classmates_text.split(",")
print("Classmates list:", classmates)

# list() converts a string into a list of individual characters.
course_name = "Python"
course_characters = list(course_name)
print("Characters in course name:", course_characters)

# join() combines a list of strings into one string.
joined_sentence = " ".join(sentence_words)
print("Joined sentence:", joined_sentence)

csv_output = ", ".join(classmates)
print("Comma-separated classmates:", csv_output)

# Practical example: clean a list of names and create a display string.
messy_names = ["  maya", "NOAH  ", " zoe "]
clean_names = []
for name in messy_names:
	clean_names.append(name.strip().title())

name_display = " | ".join(clean_names)
print("Clean names:", clean_names)
print("Name display:", name_display)


# Lists and strings practice:
# 1. Convert "red,green,blue" into a list using split().
# 2. Join that list into the string "red - green - blue".
# 3. Convert your first name into a list of characters.
# 4. Clean ["  apple ", " banana", "ORANGE "] and capitalize each item.


# Tuples are ordered collections, like lists, but they cannot be changed after
# they are created. Tuples usually use parentheses.
colors_list = ["red", "green", "blue"]
colors_tuple = ("red", "green", "blue")

print("List:", colors_list)
print("Tuple:", colors_tuple)
print("First tuple item:", colors_tuple[0])

# Lists are mutable, so an item can be replaced.
colors_list[0] = "yellow"
print("Changed list:", colors_list)

# Tuples are immutable, so this would raise a TypeError:
# colors_tuple[0] = "yellow"

# A one-item tuple needs a trailing comma.
one_item_tuple = ("Python",)
not_a_tuple = ("Python")
print("One-item tuple:", one_item_tuple)
print("Without comma, this is a:", type(not_a_tuple).__name__)


# Practical example: coordinates are a fixed pair of values.
location = (21.3, -157.8)
latitude, longitude = location
print("Location:", location)
print("Latitude:", latitude)
print("Longitude:", longitude)

# Tuples are useful for data that belongs together and should not change.
student_record = ("Maya", 352, "A")
student_name, student_id, grade = student_record
print(f"Student {student_name} has ID {student_id} and grade {grade}.")


# Use a list when items may need to be added, removed, or reordered.
todo_items = ["study", "practice", "review"]
todo_items.append("submit")
print("Changeable to-do list:", todo_items)

# Use a tuple when the collection represents a fixed record or fixed values.
days_in_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Fixed days:", days_in_week)


# Tuple practice:
# 1. Create a tuple containing the names of three cities.
# 2. Access the second city by index.
# 3. Unpack ("Ada", 36) into a name and an age variable.
# 4. Explain why a shopping list should usually be a list instead of a tuple.
