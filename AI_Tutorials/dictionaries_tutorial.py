"""Python dictionaries: a beginner-friendly introduction.

A dictionary stores information as key-value pairs. It is useful when each
value has a meaningful label, such as a student's name, a product's price, or
an account setting.
"""


# Create a dictionary with curly braces. Each key is connected to a value with
# a colon, and pairs are separated by commas.
student = {
	"name": "Maya",
	"major": "Information Technology",
	"year": 2,
}
empty_dictionary = {}

print("Student:", student)
print("Empty dictionary:", empty_dictionary)


# Access a value by putting its key inside square brackets.
print("Student name:", student["name"])
print("Student major:", student["major"])

# The get() method safely looks up a key and can provide a default value.
print("Student year:", student.get("year"))
print("Student email:", student.get("email", "No email on file"))


# Add a new key-value pair by assigning a value to a new key.
student["email"] = "maya@example.com"
student["courses"] = ["ITM 352", "English 101"]
print("After adding information:", student)

# Assigning to an existing key updates its value.
student["year"] = 3
print("After updating year:", student)


# Practical example: track inventory by product name.
inventory = {
	"notebooks": 12,
	"pens": 25,
	"backpacks": 4,
}

inventory["notebooks"] += 3  # Add three notebooks to the current stock.
inventory["pencils"] = 18  # Add a product that was not there before.

print("Notebook stock:", inventory["notebooks"])
print("Pencil stock:", inventory.get("pencils", 0))
print("Inventory:", inventory)


# Dictionaries can contain different value types, including lists and other
# dictionaries. Keys should be unique; assigning the same key replaces its old
# value.
contact = {
	"name": "Noah",
	"phone_numbers": ["555-0100", "555-0101"],
	"address": {"city": "Honolulu", "zip_code": "96813"},
}
print("Contact name:", contact["name"])
print("First phone number:", contact["phone_numbers"][0])
print("Contact city:", contact["address"]["city"])


# Check whether a key exists before accessing it directly.
if "email" in student:
	print("Email found:", student["email"])

if "phone" not in student:
	print("No phone number on file")


# Dictionary practice:
# 1. Create a dictionary for a book with title, author, and page_count keys.
# 2. Print the book's title using its key.
# 3. Add a published_year key.
# 4. Update the page_count value.
# 5. Use get() to look up a missing genre key with "Unknown" as the default.


# Essential dictionary operations.
operations_demo = {
	"name": "Maya",
	"points": 85,
	"status": "active",
}

# Add a new item with a new key.
operations_demo["major"] = "Information Technology"
print("After adding major:", operations_demo)

# Update a value by assigning a new value to an existing key.
operations_demo["points"] = 92
print("After updating points:", operations_demo)

# Check whether a key exists with in or not in.
print("Has status key:", "status" in operations_demo)
print("Has email key:", "email" in operations_demo)

# Remove an item with del when its key is known.
del operations_demo["status"]
print("After del:", operations_demo)

# pop() removes a key and returns its value.
removed_major = operations_demo.pop("major")
print("Removed major:", removed_major)
print("After pop():", operations_demo)

# popitem() removes and returns the most recently added key-value pair.
removed_pair = operations_demo.popitem()
print("Removed pair:", removed_pair)
print("After popitem():", operations_demo)

# keys(), values(), and items() provide all keys, values, or pairs.
inventory_keys = list(inventory.keys())
inventory_values = list(inventory.values())
inventory_items = list(inventory.items())
print("Inventory keys:", inventory_keys)
print("Inventory values:", inventory_values)
print("Inventory items:", inventory_items)

# These views are especially useful in a loop.
for product_name, stock_count in inventory.items():
	print(f"{product_name}: {stock_count} in stock")

# clear() removes every item from a dictionary.
temporary_dictionary = {"one": 1, "two": 2}
temporary_dictionary.clear()
print("After clear():", temporary_dictionary)


# Dictionary operations practice:
# 1. Add a price key to operations_demo.
# 2. Update the points value to 100.
# 3. Check whether the name key exists.
# 4. Remove the points key with pop() and print its returned value.
# 5. Print all keys and values in inventory.


# Important dictionary methods.
product = {
	"name": "notebook",
	"price": 4.50,
	"quantity": 12,
}

# get() returns a value without raising an error for a missing key.
print("Product name:", product.get("name"))
print("Product color:", product.get("color", "Not specified"))

# update() adds several key-value pairs or changes existing values.
product.update({"price": 5.00, "category": "school supplies"})
print("After update():", product)

# keys() returns the dictionary's keys.
print("Product keys:", list(product.keys()))

# values() returns the dictionary's values.
print("Product values:", list(product.values()))

# items() returns key-value pairs, which are useful in loops.
for key, value in product.items():
	print(f"{key}: {value}")

# pop() removes a key and returns its value.
removed_quantity = product.pop("quantity")
print("Removed quantity:", removed_quantity)
print("After pop():", product)

# clear() removes every key-value pair from a dictionary.
product.clear()
print("After clear():", product)


# Dictionary methods practice:
# 1. Use get() to read a missing email key with "None" as the default.
# 2. Use update() to add color and brand keys to a dictionary.
# 3. Print all keys, values, and items from that dictionary.
# 4. Use pop() to remove one key and print the returned value.
# 5. Use clear() to empty the dictionary.


# Looping through dictionaries.
grades = {
	"Maya": 92,
	"Noah": 85,
	"Zoe": 98,
}

# Looping over a dictionary directly visits each key.
print("Student names:")
for student_name in grades:
	print(student_name)

# keys() makes it explicit that the loop uses the keys.
print("Grade keys:")
for student_name in grades.keys():
	print(student_name)

# values() visits only the values.
print("Grades:")
for grade in grades.values():
	print(grade)

# items() visits both the key and its value. Unpacking gives each part a name.
print("Student grades:")
for student_name, grade in grades.items():
	print(f"{student_name}: {grade}")

# A loop can calculate a result from dictionary values.
total_points = 0
for grade in grades.values():
	total_points += grade

average_grade = total_points / len(grades)
print("Average grade:", average_grade)


# Dictionary loop practice:
# 1. Loop through grades and print each student with "passed" or "needs review".
# 2. Loop through grades.values() and count grades of 90 or higher.
# 3. Loop through grades.items() and print the highest grade.


# Nested dictionaries and lists.
# A nested dictionary stores one dictionary as a value inside another.
student_directory = {
	"Maya": {
		"major": "Information Technology",
		"year": 3,
		"courses": ["ITM 352", "English 101"],
	},
	"Noah": {
		"major": "Business",
		"year": 2,
		"courses": ["Accounting 201", "Economics 101"],
	},
}

print("Student directory:", student_directory)

# Use one key at a time to reach a value inside the nested structure.
print("Maya's major:", student_directory["Maya"]["major"])
print("Noah's first course:", student_directory["Noah"]["courses"][0])

# Update a value inside a nested dictionary.
student_directory["Maya"]["year"] = 4
print("Maya's updated year:", student_directory["Maya"]["year"])

# Add an item to a list stored inside a dictionary.
student_directory["Maya"]["courses"].append("Database Systems")
print("Maya's courses:", student_directory["Maya"]["courses"])

# Add a new nested record.
student_directory["Zoe"] = {
	"major": "Computer Science",
	"year": 1,
	"courses": ["Programming 101"],
}
print("Number of students:", len(student_directory))

# Loop through nested dictionaries and their lists.
for student_name, student_info in student_directory.items():
	print(f"{student_name} studies {student_info['major']}.")
	for course in student_info["courses"]:
		print("  Course:", course)


# Practical example: a course catalog with nested dictionaries and lists.
course_catalog = {
	"ITM 352": {
		"title": "Web Application Development",
		"instructor": "Dr. Kaili",
		"topics": ["Python", "HTML", "CSS"],
	},
	"ITM 360": {
		"title": "Database Design",
		"instructor": "Dr. Lee",
		"topics": ["SQL", "Tables", "Queries"],
	},
}

course = course_catalog["ITM 352"]
print("Course title:", course["title"])
print("Course topics:", ", ".join(course["topics"]))


# Nested dictionary practice:
# 1. Create a nested dictionary for two books, including title and author.
# 2. Add a list of genres to one book.
# 3. Access the second genre from that list.
# 4. Update one book's author.
# 5. Loop through the books and print each title.


# Real-world uses for dictionaries.

# 1. Counting items: use each item as a key and its count as the value.
votes = ["blue", "red", "blue", "green", "red", "blue"]
vote_counts = {}
for color in votes:
	vote_counts[color] = vote_counts.get(color, 0) + 1

print("Vote counts:", vote_counts)

# 2. Grouping data: use a category as a key and a list as its value.
students_by_major = {}
student_records = [
	("Maya", "Information Technology"),
	("Noah", "Business"),
	("Zoe", "Information Technology"),
]

for student_name, major in student_records:
	students_by_major.setdefault(major, []).append(student_name)

print("Students by major:", students_by_major)

# 3. Configuration settings: store named options in one easy-to-read object.
settings = {
	"language": "English",
	"items_per_page": 25,
	"notifications_enabled": True,
}

if settings["notifications_enabled"]:
	print("Notifications are enabled.")
print("Items per page:", settings.get("items_per_page", 10))

# 4. Data lookup: use a unique ID as a key for fast access to a record.
employees = {
	"E100": {"name": "Maya", "department": "Technology"},
	"E101": {"name": "Noah", "department": "Finance"},
}

employee_id = "E101"
employee = employees.get(employee_id)
if employee is not None:
	print(f"Employee {employee_id}: {employee['name']} ({employee['department']})")
else:
	print("Employee not found")


# Real-world dictionary practice:
# 1. Count the words in ["cat", "dog", "cat", "bird", "dog", "cat"].
# 2. Group three products by category using a dictionary of lists.
# 3. Create settings for theme, font_size, and autosave.
# 4. Create a lookup dictionary that maps product IDs to names and prices.


# Choosing between lists, tuples, and dictionaries.
#
# List: ordered and changeable. Use it for a collection that may grow, shrink,
# or be reordered. Its disadvantage is that values are accessed by position,
# so you need to know the correct index.
shopping_cart = ["notebook", "pens", "notebook"]
shopping_cart.append("backpack")
print("Changing shopping cart:", shopping_cart)

# Tuple: ordered and unchangeable. Use it for a fixed group of related values,
# such as coordinates or a record that should not be modified. Its disadvantage
# is that changing the data requires creating a new tuple.
coordinates = (21.3, -157.8)
latitude, longitude = coordinates
print(f"Fixed coordinates: latitude={latitude}, longitude={longitude}")

# Dictionary: labeled, changeable key-value pairs. Use it when values need
# meaningful labels or fast lookup by a key. Its disadvantages are extra
# memory compared with a simple sequence and the need for unique keys.
user_profile = {
	"name": "Maya",
	"email": "maya@example.com",
	"role": "student",
}
print("Profile email:", user_profile["email"])
user_profile["role"] = "mentor"
print("Updated profile:", user_profile)

# The same information looks different in each structure.
list_record = ["Maya", "mentor", 3]
tuple_record = ("Maya", "mentor", 3)
dictionary_record = {"name": "Maya", "role": "mentor", "year": 3}

print("List record, position 0:", list_record[0])
print("Tuple record, position 0:", tuple_record[0])
print("Dictionary record, name:", dictionary_record["name"])


# Quick decision guide:
# - Choose a list for an ordered collection that changes.
# - Choose a tuple for a fixed ordered collection or record.
# - Choose a dictionary for labeled values and key-based lookup.


# Comparison practice:
# 1. Choose a list, tuple, or dictionary for a changing playlist and explain why.
# 2. Choose a list, tuple, or dictionary for a fixed RGB color value.
# 3. Choose a list, tuple, or dictionary for employee records looked up by ID.
# 4. Rewrite one example using a different structure and describe the tradeoff.
