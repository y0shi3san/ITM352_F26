# Interactive quiz system, fifth version
# Kaili Takara
# October 7, 2026

from string import ascii_lowercase

questions = {
    "What is the capital of France?": ["Paris", "Toulouse", "Nice", "Avignon"],
    "What is the capital of Germany?": ["Berlin", "Munich", "Hamburg", "Frankfurt"],
    "What is the capital of Italy?": ["Rome", "Milan", "Naples", "Florence"],
    "What is the airspeed of an unladen swallow?": ["10", "12", "8", "15"],
    "The last supper was painted by?": ["da Vinci", "Michelangelo", "Raphael", "Caravaggio"]
}

num_correct = 0

for num, (question, answers) in enumerate(questions.items(), start=1):
    correct_answer = answers [0]
    print(f"\nQuestion {num}: {question}")

    sorted_answers = sorted(answers)
    label_to_answer = dict(zip(ascii_lowercase, random.sample(sorted_answers, k=len(sorted_answers))))

    for label, answer in label_to_answer.items():
        print(f"{label}. {answer}")

    answer_label = input("Choice? ").lower()

    answer = label_to_answer.get(answer_label)

    
    if answer == correct_answer:
        print("Correct!")
        num_correct += 1
    else:
        print(f"The answer is '{correct_answer}', not {answer!r}.")

print(f"You got {num_correct} correct out of {len(questions)} questions.")