import random

secret_number = random.randint(1, 100)
guess = None

while guess != secret_number:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    if guess < secret_number:
        print("Your guess is too low. Try again.")
    elif guess > secret_number:
        print("Your guess is too high. Try again.")
    else:
        print("Correct! You guessed the number.")