import random
from utils import screen_cleaner
from score import add_score

def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess(difficulty):
    while True:
        guess = input(f"Please guess a number between 1-{difficulty}: ")
        if guess.isnumeric() and int(guess) in range(1, difficulty + 1):
            return int(guess)
        else:
            print("Inavlid input, Try again!")


def play(difficulty):
        print("Welcome to Guess Game!")
        random_number = generate_number(difficulty)
        user_guess = get_guess(difficulty)

        if random_number == user_guess:
            print(f"You win! you guessed {user_guess}, which is the randon number!")
            add_score(difficulty)
            return True
        else:
            print(f"You lose! the random number is {random_number}, while you guessed {user_guess}")
            return False


def play_again(difficulty):
    loop_game = True
    while loop_game:
        replay = input("Would you like to play again?").lower()
        if replay == "n":
            loop_game = False
            print("\nGoodbye!")
        elif replay == "y":
            screen_cleaner()
            play(difficulty)
        else:
            print("Invalid input, please type y or n only!")

