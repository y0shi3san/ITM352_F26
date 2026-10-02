# Interactive quiz system V2
# Make a list with the questions and anwers
# Kaili Takara 
# October 2, 2026  

questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the capital of Germany?", "answer": "Berlin"},
    {"question": "What is the capital of Italy?", "answer": "Rome"},
    {"question": " The last supper was painted by?", "answer": "da Vinci"}
]

for question, correct_anwser in questions:
    answer = input(f"{question}? ")
    if answer == correct_anwser:
        print("Correct!")
    else:
        print(f"The answer is '{correct_anwser}', not {answer!r}.")