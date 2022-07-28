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
                    score = 0
                else:
                    1500

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


def welcome():
    print("Welcome to Ten Thousand\n(y)es to play or (n)o to decline")


def decline_game():
    print("OK. Maybe another time")

def handle_roll_bank_quit(roll_bank_or_quit, final_score, temp_score, round):
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
        return
    elif roll_bank_or_quit == 'r':
        temp_score = 0
        return


def start_round(current_round, die_in_play, user_choice, temp_score):
    if not user_choice:
        print(f"Starting round {current_round}")

    print(f"Rolling {die_in_play} dice...")
    roll_result = get_roll_result(die_in_play)
    print(f"*** {tuple_to_str(roll_result)}***")
    if check_for_zilch(roll_result):
        print("****************************************\n**        Zilch!!! Round over         **\n**************"
              "**************************")
        print(f"You banked {temp_score} points in round {current_round}")
        return
    print("Enter dice to keep, or (q)uit:")
    return tuple_to_str(roll_result)

def check_for_zilch(roll_result):
    if GameLogic.calculate_score(roll_result) == 0:
        return True
    return False


def get_roll_result(die_in_play):
    return GameLogic.roll_dice(die_in_play)


def check_for_cheater(user_choice, die_roll_data):
    for char in user_choice:
        if char not in die_roll_data:
            print("Hey, its not cool to cheat! Lets restart this round eh?")
            return True

    return False


def handle_zilch(user_input):
    if user_input == 0:
        print("Zilch! Your input had a value of 0 and you now get 0 for the round! Better luck next round :)")
        return True
    return False


def play_game(logic):

    final_score = 0
    temp_score = 0
    re_roll_score = 0
    current_round = 1
    die_in_play = 6
    re_roll = False
    welcome()

    start = input("> ")

    if start == 'n':
        decline_game()
    elif start == 'y':
        while True:
            die_roll_result = start_round(current_round, die_in_play, re_roll, temp_score)
            re_roll = False
            temp_score = re_roll_score
            re_roll_score = 0

            while True:
                choice = input("> ")
                if choice == 'q':
                    print(f"Thanks for playing. You earned {final_score} points")
                    return
                if check_for_cheater(choice, die_roll_result):
                    break
                temp_score += GameLogic.calculate_score(str_to_list_to_tuple(choice))
                if handle_zilch(temp_score):
                    current_round += 1
                    break
                die_in_play -= len(choice)
                if die_in_play == 0:
                    die_in_play = 6
                print(f"You have {temp_score} unbanked points and {die_in_play} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")
                roll_bank_or_quit = input("> ")
                if roll_bank_or_quit == 'q':
                    print(f"Thanks for playing. You earned {final_score} points")
                    return
                elif roll_bank_or_quit == 'b':
                    final_score += temp_score
                    print(f"You banked {temp_score} points in round {current_round}")
                    current_round += 1
                    temp_score = 0
                    print(f"Total score is {final_score} points")
                    die_in_play = 6
                    break
                elif roll_bank_or_quit == 'r':
                    re_roll = True
                    re_roll_score = temp_score
                    break

    else:
        print("Invalid Input")


if __name__ == '__main__':
    play_game(GameLogic)