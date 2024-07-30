from utils import screen_cleaner
from score import score_reset

def welcome():
    score_reset()
    print("\n")
    while True:
        name = input("Please enter your name: ")
        if name.isnumeric():
            print("Name should not contain only numbers, please enter a valid name.")
        elif len(name) < 4:
            print("Name too short. make it at least 4 characters.")
        elif len(name) > 7:
            print("Name too long! 7 characters max.")
        elif not name.isalnum():
            print("No special characters in the name please.")
        else:
            print("\n")
            print(f"Hi {name} and welcome to the World of Games: The Epic Journey")
            print("\n")
            break


def start_play():
    game_again = True
    while game_again:
        game_selected = input("""Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to
guess it back.
2. Guess Game - guess a number and see if you chose like the computer.
3. Currency Roulette - try and guess the value of a random amount of USD in ILS: \n """)

        if game_selected.isnumeric() and 0 < int(game_selected) < 4:
            game_again = False
        else:
            print("That is not a valid number, Please try again! \n ")

    level_again = True
    while level_again:
        level = input("Please select a difficulty level between 1 to 5: \n ")

        if level.isnumeric() and 0 < int(level) < 6:
            level_again = False
        else:
            print("That is not a valid number, Please try again! \n ")


    if game_selected == "1":
        from memory_game import play, play_again
        play(int(level))
        play_again(int(level))
        back_to_main()
    elif game_selected == "2":
        from guess_game import play, play_again
        play(int(level))
        play_again(int(level))
        back_to_main()
    elif game_selected == "3":
        from currency_roulette import play, play_again
        play(int(level))
        play_again(int(level))
        back_to_main()


def back_to_main():
    loop_back = True
    while loop_back:
        back_to_main = input("Would you like to go back to main menu? \n").lower()
        if back_to_main == "y":
            screen_cleaner()
            start_play()
        elif back_to_main == "n":
            loop_back = False
            print("\nGoodbye!")
        else:
            print("Invalid input, please type y or n only!")






