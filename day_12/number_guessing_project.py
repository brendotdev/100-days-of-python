import os
import random
from art import logo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def guess_the_number():
    guess_this = random.randint(1, 100)
    print("Welcome to:")
    print(logo)
    print("I'm thinking of a number between 1 and 100, try to guess it.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    guesses = 10 if difficulty == 'easy' else 5

    while guesses > 0:
        if guesses > 1:
            print(f"You have {guesses} guesses left.")
        else:
            print("Last try!")

        attempt = int(input("Take your guess: "))

        if attempt == guess_this:
            print(f"Correct! The answer was {guess_this}. Thanks for playing! 😁")
            break
        elif attempt > guess_this:
            print("Too high.")
        else:
            print("Too low.")

        guesses -= 1

        if guesses == 0:
            print(f"Game over. The number was {guess_this}.")

    play_again = input("\nDo you want to play again? Type 'y' to play again or 'n' to quit: ").lower()
    if play_again == 'y':
        clear()
        guess_the_number()
    else:
        print("Goodbye.")

guess_the_number()
