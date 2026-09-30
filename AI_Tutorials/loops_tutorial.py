"""Python loops: a beginner-friendly introduction.

A for loop repeats once for each item in a sequence or a known number of
times. A while loop repeats as long as a condition is true, making it useful
when repetition depends on user input or another changing condition.
"""

import random


# range(5) produces the numbers 0 through 4. The stop value, 5, is not included.
for number in range(5):
	print("Number:", number)


# range(start, stop) starts at the first value and stops before the second.
for number in range(1, 6):
	print("Counting from 1 to 5:", number)


# range(start, stop, step) changes the count by step each time.
for number in range(0, 10, 2):
	print("Counting by twos:", number)


# A negative step counts backward. The stop value is still excluded.
for number in range(5, 0, -1):
	print("Counting backward:", number)


# range() can also create a sequence of numbers to store in a list.
number_sequence = list(range(1, 6))
print("Number sequence:", number_sequence)


# A for loop can process each value in a list.
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
	print("Fruit:", fruit)


# Strings are sequences of characters, so a loop can visit each character.
word = "Python"
for character in word:
	print("Character:", character)


# Practice: count from 1 to 10. Use 11 as the stop because it is excluded.
print("Practice: count from 1 to 10")
for number in range(1, 11):
	print(number)


# Practice: count backward from 10 to 1.
print("Practice: count backward")
for number in range(10, 0, -1):
	print(number)


# Practice: count by twos from 2 to 10.
print("Practice: count by twos")
for number in range(2, 11, 2):
	print(number)


# continue skips the rest of this iteration and moves to the next number.
print("Skip even numbers with continue")
for number in range(1, 11):
	if number % 2 == 0:
		continue
	print(number)


# Lists: loop over values when you only need each item.
students = ["Maya", "Noah", "Zoe"]
for student in students:
	print("Student:", student)


# Use enumerate() when you need both each list item's position and its value.
# start=1 makes the displayed positions begin at 1 instead of 0.
for position, student in enumerate(students, start=1):
	print(position, student)


# break exits the loop as soon as the requested student is found.
print("Find Noah with break")
for student in students:
	print("Checking:", student)
	if student == "Noah":
		print("Found Noah")
		break


# Strings: loop over characters when each character matters.
word = "hello"
for character in word:
	print("Letter:", character)


# Use split() to loop over words in a sentence instead of individual letters.
sentence = "Python loops are useful"
for word in sentence.split():
	print("Word:", word)


# Dictionaries: a basic loop visits keys. Use this when you need the keys.
grades = {"Maya": 92, "Noah": 85, "Zoe": 98}
for student in grades:
	print("Student name:", student)


# Use .values() when you only need the dictionary values.
for grade in grades.values():
	print("Grade:", grade)


# Use .items() when you need each key and its associated value.
for student, grade in grades.items():
	print(student, "earned", grade)


# Practice: process a list of students by printing each name.
practice_students = ["Ava", "Liam", "Eli"]
for student in practice_students:
	print("Welcome,", student)


# Practice: process each word in a sentence.
practice_sentence = "We are learning Python loops"
for word in practice_sentence.split():
	print(word)


# Practice: process each student's name and grade in a dictionary.
practice_grades = {"Ava": 90, "Liam": 87, "Eli": 95}
for student, grade in practice_grades.items():
	print(student, "has a grade of", grade)


# Use a while loop when the number of repetitions depends on a condition.
def count_until_five():
	count = 1
	while count <= 5:
		print("Count:", count)
		count += 1


# Use a while loop to keep asking until the user enters the expected response.
def ask_until_yes():
	answer = ""
	while answer.lower() != "yes":
		answer = input("Would you like to continue? Type yes: ")


# Use while True for indefinite iteration, and break when it is time to stop.
def command_loop():
	while True:
		command = input("Enter a command, or type quit to stop: ")
		if command.lower() == "quit":
			break
		print("You entered:", command)


# Practice game: keep asking until the player guesses the randomly chosen number.
def guessing_game():
	secret_number = random.randint(1, 10)
	print("Guess the number from 1 to 10!")

	while True:
		try:
			guess = int(input("Your guess: "))
		except ValueError:
			print("Please enter a whole number.")
			continue

		if guess < secret_number:
			print("Too low. Try again.")
		elif guess > secret_number:
			print("Too high. Try again.")
		else:
			print("You guessed it!")
			break


# Nested loops are useful for grids: the inner loop visits each column
# for every row.
print("Grid coordinates:")
for row in range(1, 4):
	for column in range(1, 4):
		print(f"({row}, {column})", end=" ")
	print()


# Practice: build a multiplication table. Each row uses the inner loop
# to multiply its row number by every column number.
print("Multiplication table from 1 to 10:")
for row in range(1, 11):
	for column in range(1, 11):
		print(f"{row * column:4}", end="")
	print()


# A list comprehension builds a new list in one expression.
# Pattern: [expression for item in iterable if condition]

# This regular loop collects odd numbers, similar to the earlier continue example.
odd_numbers_by_loop = []
for number in range(1, 11):
	if number % 2 == 0:
		continue
	odd_numbers_by_loop.append(number)

# Equivalent comprehension: keep each number only when the condition is true.
odd_numbers = [number for number in range(1, 11) if number % 2 != 0]
print("Odd numbers from loop:", odd_numbers_by_loop)
print("Odd numbers from comprehension:", odd_numbers)


# A regular loop can also transform each student name into a welcome message.
welcome_messages_by_loop = []
for student in practice_students:
	welcome_messages_by_loop.append(f"Welcome, {student}")

# Equivalent comprehension: the expression formats each student name.
welcome_messages = [f"Welcome, {student}" for student in practice_students]
print("Welcome messages:", welcome_messages)


# Comprehensions are best for building lists simply; use a regular loop for
# printing, input, or logic that would be difficult to read in one expression.


# enumerate() gives each item together with its index. Use start=1 for
# human-friendly numbering; without it, indexes start at 0.
print("Enumerate students:")
for index, student in enumerate(practice_students):
	print(index, student)


# zip() pairs items from multiple iterables. It stops when the shortest ends.
subjects = ["Math", "English", "Science"]
subject_scores = [88, 94, 91]
print("Paired subjects and scores:")
for subject, score in zip(subjects, subject_scores):
	print(subject, score)


# reversed() iterates from the end to the beginning without changing the list.
print("Students in reverse order:")
for student in reversed(practice_students):
	print(student)
print("Original student list:", practice_students)


# Use indexes when you need to update items in the original list.
# If you only need both the index and value, enumerate() is usually clearer.
practice_scores = [75, 82, 90]
for index in range(len(practice_scores)):
	practice_scores[index] += 5
print("Scores after adding 5 points:", practice_scores)


if __name__ == "__main__":
	guessing_game()

prices = [5.99, 3.50, 12.75, 8.00]

total = 0

for price in prices:
    total += price

print("Total cost:", total)
