import random
import requests
from requests.structures import CaseInsensitiveDict
from utils import screen_cleaner
from score import add_score

url = "https://api.freecurrencyapi.com/v1/latest"

headers = CaseInsensitiveDict()
headers["apikey"] = "fca_live_5kFFeonQLtEovyXXfmdYkdghGAYjLw2knZI4sR5V"

resp = requests.get(url, headers=headers)
data = resp.json()


def get_money_interval(difficulty):
    random_number = random.randint(1, 100)
    print(f"The random number is: {random_number}")
    current_rate = data["data"]["ILS"]
    correct_answer = random_number * current_rate
    allowed_range = 10 - difficulty
    money_interval = range(int(correct_answer-allowed_range), int(correct_answer+allowed_range))
    return money_interval


def get_guess_from_user():
    while True:
        user_guess = input("Please enter your guess: ")
        if user_guess.isnumeric():
            return int(user_guess)
        else:
            print("Invalid input. Try again.")


def play(difficulty):
    win = get_money_interval(difficulty)
    user_input = get_guess_from_user()
    if user_input in win:
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

