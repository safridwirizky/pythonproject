from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficult = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempt = 0

if difficult == 'hard':
    attempt = 5
else:
    attempt = 10

list_numbers = []
for i in range(1, 101):
    list_numbers.append(i)

chosen_number = random.choice(list_numbers)

right_guess = False
while not right_guess:
    if attempt == 0:
        print("You've run out of guesses, you lose.")
        break

    print(f"You have {attempt} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))
    if guess == chosen_number:
        right_guess = True

        print(f"You got it! The answer was {guess}.")

    elif guess > chosen_number:
        print("Too high.\nGuess again.\n")
        attempt -= 1

    else:
        print("Too low.\nGuess again.\n")
        attempt -= 1