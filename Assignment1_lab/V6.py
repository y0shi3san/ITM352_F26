# Interactive quiz system, sixth version
# Randomize the order of the questions and the order of the answers for each question
# Kaili Takara
# October 7, 2026

from string import ascii_lowercase
import random

questions = {
    "What is the capital of France?": ["Paris", "Toulouse", "Nice", "Avignon"],
    "What is the capital of Germany?": ["Berlin", "Munich", "Hamburg", "Frankfurt"],
    "What is the capital of Italy?": ["Rome", "Milan", "Naples", "Florence"],
    "What is the airspeed of an unladen swallow?": ["10", "12", "8", "15"],
    "The last supper was painted by?": ["da Vinci", "Michelangelo", "Raphael", "Caravaggio"],
    "Which NHL player has the most career goals?": ["Wayne Gretzky", "Mario Lemieux", "Jaromir Jagr", "Sidney Crosby"],
    "Which classic novel opens with the line 'call me Ishmael'?": ["Moby Dick", "The Great Gatsby", "The Old Man and the Sea", "The Scarlet Letter"]
}

NUM_QUESTIONS_PER_QUIZ = 5

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(questions))
selected_questions = random.sample(list(questions.items()), k=num_questions)

num_correct = 0

for num, (question, answers) in enumerate(selected_questions, start=1):
    correct_answer = answers [0]
    print(f"\nQuestion {num}: {question}")

    sorted_answers = sorted(answers)
    label_to_answer = dict(zip(ascii_lowercase, random.sample(sorted_answers, k=len(sorted_answers))))

    for label, answer in label_to_answer.items():
        print(f"{label}. {answer}")
    while (answer_label := input("Choice? ").lower()) not in label_to_answer:
        print(f"Invalid choice. Please select one of {', '.join(label_to_answer.keys())} .")

    answer = label_to_answer.get(answer_label)

    
    if answer == correct_answer:
        print("Correct!")
        num_correct += 1
    else:
        print(f"The answer is '{correct_answer}', not {answer!r}.")

print(f"You got {num_correct} correct out of {len(selected_questions)} questions.")