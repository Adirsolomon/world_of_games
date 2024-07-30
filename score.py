from utils import scores_file_name


def add_score(difficulty):
    wining_points = (difficulty * 3) + 5
    try:
        with open(scores_file_name, "r") as file:
            current_score = int(file.read().strip())
    except FileNotFoundError:
        with open(scores_file_name, "w") as file:
            file.write(str(wining_points))
    new_score = current_score + wining_points

    with open(scores_file_name, "w") as file:
        file.write(str(new_score))


def score_reset():
    with open(scores_file_name, "w") as file:
        file.write("0")


