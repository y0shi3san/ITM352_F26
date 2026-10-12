# Generate an inteactive quiz the include requirements 5 and 8
# 5.Allow the user to choose a category for their questions
# 8.Create a separate application that interactively asks for questions and answers and stores them in the proper JSON format. [You may use File I/O]
# Kaili Takara
# October 9, 2026

# This version was able to run my quiz using me json file but did not catogarize the different topics, just randomized all questions.
# This version also only asks 4 questions

from string import ascii_lowercase
import random
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "Questions.json")

with open(json_path, "r", encoding="utf-8") as question_file:
    questions = json.load(question_file)



NUM_QUESTIONS_PER_QUIZ = 5

def prepare_questions(data, num_questions):
    all_questions = []
    for category in data["categories"].values():
        all_questions.extend(category)

    num_questions = min(num_questions, len(all_questions))
    return random.sample(all_questions, k=num_questions)


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
questions = prepare_questions(questions, NUM_QUESTIONS_PER_QUIZ)

num_correct = 0

for num, question_data in enumerate(questions, start=1):
    print(f"\nQuestion {num}: {question_data['question']}")
    num_correct += ask_question(question_data)

print(f"\nYou got {num_correct} correct.")