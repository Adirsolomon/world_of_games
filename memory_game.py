import time
import os
import random
from utils import screen_cleaner
from score import add_score

def generate_sequence(difficulty):
    sequence = []
    for i in range(difficulty):
        random_number = random.randint(1, 101)
        sequence.append(random_number)
    return sequence


def get_user_list(difficulty):
    user_input = []
    for i in range(difficulty):
        input_loop = True
        while input_loop:
            num = input("Please enter number " + str(i + 1) + ": ")
            if num.isnumeric():
                user_input.append(int(num))
                input_loop = False
                break
            else:
                print("Invalid input. try again.")
    return user_input


def play(difficulty):
    screen_cleaner()
    input("Welcome to memory game. press any key to generate the sequence: ")
    random_list = generate_sequence(difficulty)
    print(random_list)
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    input("Your time to shine. how many do you remember? press any key to start your input: ")
    user_list = get_user_list(difficulty)
    if random_list == user_list:
        print("You win!")
        add_score(difficulty)
        return True
    else:
        print("You lose!")
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



