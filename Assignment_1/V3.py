#
# Kaili Takara
# October 7, 2026

questions = {
    "question": "What is the capital of France?": ["Paris", "Touleuse", "Nice", "Avignon"],
    "question": "What is the capital of Germany?: ["Berlin", "Munich", "Hamburg", "Frankfurt"],
    "question": "What is the capital of Italy?": "answer": "Rome",
    "question": " The last supper was painted by?": "answer": "da Vinci"
}

for question, answers in questions.items():
    correct answer = answers [0]
    answer = input(f"(question)")
    answer = input(f"{question}? ")
    for answer in answers:
        print(f"- (answes)")
        ``
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is '{correct_anwser}', not {answer!r}.")