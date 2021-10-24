import random
import json
import datetime

def play_game_easy():
    secret = random.randint(1, 30)
    attempts = 0
    wrong_guesses = list()
    score_list = get_score_list()

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1
        if guess == secret:
            score_list.append({"name": name, "attempts": attempts, "date": str(datetime.datetime.now()),
                               "wrong_guesses": wrong_guesses})
            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))
            print(f"You've guessed it - congratulations {name}! It's number {secret}. You needed {attempts}")
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
            wrong_guesses.append(guess)
        elif guess < secret:
            print("Your guess is not correct... try something bigger")
            wrong_guesses.append(guess)

def play_game_hard():
    secret = random.randint(1, 30)
    attempts = 0
    wrong_guesses = list()
    score_list = get_score_list()

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1
        if guess == secret:
            score_list.append({"name": name, "attempts": attempts, "date": str(datetime.datetime.now()),
                               "wrong_guesses": wrong_guesses})
            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))
            print(f"You've guessed it - congratulations {name}! It's number {secret}. You needed {attempts}")
            break
        else:
            print("Wrong, try again.")
            wrong_guesses.append(guess)

def get_score_list():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list

def get_top_scores():
    score_list = get_score_list()
    return (sorted(score_list, key=lambda person: person['attempts']))[:3]