# Interactive quiz system, fourth version
# Kaili Takara
# October 7, 2026

questions = {
    "What is the capital of France?": ["Paris", "Toulouse", "Nice", "Avignon"],
    "What is the capital of Germany?": ["Berlin", "Munich", "Hamburg", "Frankfurt"],
    "What is the capital of Italy?": ["Rome", "Milan", "Naples", "Florence"],
    "The last supper was painted by?": ["da Vinci", "Michelangelo", "Raphael", "Caravaggio"]
}

for question, answers in questions.items():
    correct_answer = answers [0]
    sorted_answers = sorted(answers)

    for label, answer in enumerate(sorted_answers, start=1):
        print(f"{label}. {answer}")

    answer_label = int(input(f"{question} "))
    answer = sorted_answers[answer_label - 1]
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is '{correct_answer}', not {answer!r}.")