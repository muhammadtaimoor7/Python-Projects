# NUMBER GUESSING WITH DIFFERENT LEVELS

print("Welcome to our project")

# THESE ARE RULES OF GAME
print("Rules of the Game:")
print("1. Choose a difficulty level: Easy (1-50), Medium (1-100), Hard (1-500)")
print("2. I will choose a secret number in the chosen range.")
print("3. You have to guess the number.")
print("4. After each guess, I will tell you if your guess is too high or too low.")
print("5. Try to guess the number in as few attempts as possible!")

# Ask user for difficulty level
level = input("Choose the difficulty level: ")

if level == "easy":
    start, end = 1, 50  # in this way we can ask about levels
elif level == "medium":
    start, end = 1, 100
else:
    start, end = 1, 500

import random

# Start game loop
while True:
    secret_number = random.randint(start, end)
    attempts = 0

    # User guessing loop
    while True:
        guess = int(input(f"Guess a number between {start} and {end}: "))
        attempts += 1

        if guess < secret_number:
            print("Low number guessed!")
        elif guess > secret_number:
            print("High number guessed!")
        else:
            print(f"You have guessed the correct number in {attempts} attempts")
            break
    play_again=input("do you want to paly again(yes/no):").lower()
    if play_again!="yes":
        print("thanks for playing game")  
        break  
