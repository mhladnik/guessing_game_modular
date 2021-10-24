from function import play_game_easy, play_game_hard, get_top_scores
name = input("What is your name? ")

while True:
    choose = input("Would you like to A) play a new game, B) see the best scores, or C) quit?")
    if choose.upper() == "A":
        level = input("Choose your level (easy/hard): ")
        if level.upper() == "easy":
            play_game_easy()
        elif level.upper() == "hard":
            play_game_hard()
        else:
            print("There is no such game, sorry.")
            break
    elif choose.upper() == "B":
        for score_dict in get_top_scores():
            print(str(score_dict["name"]) + " needed " + str(score_dict["attempts"]) + " attempts.")
    else:
        break