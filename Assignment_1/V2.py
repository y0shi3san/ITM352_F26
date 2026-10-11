# Generate an inteactive quiz the include requirements 5 and 8
# 5.Allow the user to choose a category for their questions
# 8.Create a separate application that interactively asks for questions and answers and stores them in the proper JSON format. [You may use File I/O]
# Kaili Takara
# October 10, 2026

from string import ascii_lowercase
import random
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "Questions.json")

with open(json_path, "r", encoding="utf-8") as question_file:
    questions = json.load(question_file)



NUM_QUESTIONS_PER_QUIZ = 5

def choose_category(categories):
    category_names = list(categories)

    print("Choose a question category:")
    for number, category_name in enumerate(category_names, start=1):
        print(f"{number}. {category_name}")

    while True:
        selection = input("Enter a category number or name: ").strip()
        if selection.isdigit() and 1 <= int(selection) <= len(category_names):
            return category_names[int(selection) - 1]

        for category_name in category_names:
            if selection.casefold() == category_name.casefold():
                return category_name

        print("Invalid category. Please choose one from the list.")


def prepare_questions(data, category_name, num_questions):
    category_questions = data["categories"][category_name]
    if len(category_questions) < num_questions:
        raise ValueError(
            f"Category {category_name!r} has fewer than {num_questions} questions."
        )
    return random.sample(category_questions, k=num_questions)


def get_answer(question_text, options):
    print(f"\n{question_text}") 
    for index, choice in enumerate(options):
        print(f"  {ascii_lowercase[index]}. {choice}")

    while True:
        selection = input("Enter your answer (a-d): ").strip().lower()
        if selection in ascii_lowercase[:len(options)]:
            return options[ascii_lowercase.index(selection)]
        print("Invalid choice. Please enter one of the listed letters.")


def ask_question(question_data):
    question = question_data["question"]
    options = question_data["options"][:]
    correct_answer = question_data["answer"]

    ordered_alternatives = random.sample(options, k=len(options))
    answer = get_answer(question, ordered_alternatives)

    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}.")
        return 0


# Main program logic starts here
category_name = choose_category(questions["categories"])
questions = prepare_questions(
    questions, category_name, NUM_QUESTIONS_PER_QUIZ
)
print(f"\nStarting a 5-question quiz in {category_name}.")

num_correct = 0

for num, question_data in enumerate(questions, start=1):
    print(f"\nQuestion {num}:")
    num_correct += ask_question(question_data)

print(f"\nYou got {num_correct} correct.")