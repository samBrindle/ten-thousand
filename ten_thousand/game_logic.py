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

        print(temp_list)
        return tuple(temp_list)