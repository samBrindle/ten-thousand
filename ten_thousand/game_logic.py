import random


class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def calculate_score(dice_tuple):
        score_dict = {}
        score = 0

        # sets up dict of values from tuple
        for num in dice_tuple:
            if num in score_dict:
                score_dict[num] += 1
            else:
                score_dict[num] = 1

        # handles straight
        if len(score_dict) == 6:
            return 1500

        # handles full house
        if len(score_dict) == 3:
            for num in score_dict:
                if score_dict[num] != 2:
                    return 0
            return 1500

        # handles all normal hands
        for num in score_dict:
            if num == 1:
                if score_dict[num] == 1:
                    score += 100
                if score_dict[num] == 2:
                    score += 200
                if score_dict[num] > 2:
                    score += 1000 * (score_dict[num]-2)

            if num == 2:
                if score_dict[num] > 2:
                    score += 200 * (score_dict[num]-2)

            if num == 3:
                if score_dict[num] > 2:
                    score += 300 * (score_dict[num]-2)

            if num == 4:
                if score_dict[num] > 2:
                    score += 400 * (score_dict[num]-2)

            if num == 5:
                if score_dict[num] == 1:
                    score += 50
                if score_dict[num] == 2:
                    score += 100
                if score_dict[num] > 2:
                    score += 500 * (score_dict[num]-2)

            if num == 6:
                if score_dict[num] > 2:
                    score += 600 * (score_dict[num]-2)

        return score

    @staticmethod
    def roll_dice(num):
        temp_list = []

        while len(temp_list) != num:
            temp_list.append(random.randint(1, 6))

        return tuple(temp_list)


def tuple_to_str(die_tuple):
    string = ""
    for num in die_tuple:
        string += str(num) + " "

    return string


def str_to_list_to_tuple(bank_choices):
    new_list = []
    for char in bank_choices:
        new_list.append(int(char))

    return tuple(new_list)


def play_game(logic):

    final_score = 0
    round_score = 0
    temp_score = 0
    bank = 0
    round = 1
    die_in_play = 6
    print("Welcome to Ten Thousand\n(y)es to play or (n)o to decline")

    start = input("> ")

    if start == 'n':
        print("OK. Maybe another time")
    elif start == 'y':
        while True:
            print(f"Starting round {round}")
            print(f"Rolling {die_in_play} dice...")
            roll_result = GameLogic.roll_dice(die_in_play)
            print(f"*** {tuple_to_str(roll_result)}***")
            print("Enter dice to keep, or (q)uit:")

            while True:
                choice = input("> ")
                if choice == 'q':
                    print(f"Thanks for playing. You earned {final_score} points")
                    return
                temp_score = GameLogic.calculate_score(str_to_list_to_tuple(choice))
                die_in_play -= len(choice)
                print(f"You have {temp_score} unbanked points and {die_in_play} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")
                roll_bank_or_quit = input("> ")
                if roll_bank_or_quit == 'q':
                    print(f"Thanks for playing. You earned {final_score} points")
                    return
                elif roll_bank_or_quit == 'b':
                    bank = temp_score
                    final_score += bank
                    temp_score = 0
                    print(f"You banked {bank} points in round {round}")
                    round += 1
                    print(f"Total score is {final_score} points")
                    die_in_play = 6
                    break
                elif roll_bank_or_quit == 'r':
                    temp_score = 0
                    break

    else:
        print("Invalid Input")


if __name__ == '__main__':
    play_game(GameLogic)