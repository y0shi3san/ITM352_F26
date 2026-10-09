# Interactive quiz system, fourth version
# Kaili Takara
# October 7, 2026

questions = {
    "What is the capital of France?": ["Paris", "Toulouse", "Nice", "Avignon"],
    "What is the capital of Germany?": ["Berlin", "Munich", "Hamburg", "Frankfurt"],
    "question": "What is the capital of Italy?": "answer": "Rome",
    "question": " The last supper was painted by?": "answer": "da Vinci"
}

for question, answers in questions.items():
    correct_answer = answers [0]
    sorted_answers = sorted(answers)

    for label, answer in enumerate(sorted_answers, start=1):

    answer_label = int(input(f"(question)"))
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is '{correct_anwser}', not {answer!r}.")