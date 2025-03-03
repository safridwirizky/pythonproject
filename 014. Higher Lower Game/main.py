from game_data import data
import random
from art import logo, vs

score = 0

def start_game():
    global score

    print(logo)
    print(f"Current score: {score}")

    a, b = random.sample(data, 2)
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

    invalid_input = True
    while invalid_input:
        invalid_input = False

        guess = input("Guess the most follower. Type 'A' or 'B': ")

        if guess == 'A':
            if a['follower_count'] > b['follower_count']:
                print("Your guess is right.")
                score += 1
                start_game()

            else:
                print(f"Your guess is wrong.\nYour score: {score}")
                exit()

        elif guess == 'B':
            if b['follower_count'] > a['follower_count']:
                print("Your guess is right.")
                score += 1
                start_game()

            else:
                print(f"Your guess is wrong.\nYour score: {score}")
                exit()

        else:
            print("Please type 'A' or 'B'!")
            invalid_input = True

start_game()










