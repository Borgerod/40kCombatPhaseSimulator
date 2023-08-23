from math import *  # math module
import random
import tkinter as tk

# this assigns random numbers between 1 and 6 to numdice amount and returns a list of them


def roll_dice(numdice):
    dice_roll = []
    for index in range(int(numdice)):
        dice_roll.append(random.randint(1, 6))
    return dice_roll


# this tests the randomness of the random function for numbers between 1 and 6
def random_accuracy_test():
    # -------------------------------------------------------------------------------------------
    dice_roll = roll_dice(10)
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0

    for index in dice_roll:

        if index == 1:
            one += 1
        elif index == 2:
            two += 1
        elif index == 3:
            three += 1
        elif index == 4:
            four += 1
        elif index == 5:
            five += 1
        elif index == 6:
            six += 1

    print("ones: " + str(one))
    print("twos: " + str(two))
    print("threes: " + str(three))
    print("fours: " + str(four))
    print("fives: " + str(five))
    print("sixes: " + str(six))
    # -------------------------------------------------------------------------------------------


''' NEW VERSION '''
# This function returns the amount of integers in the list that is above the hit number
def check_hits(BS, num_attacks):
    hit_rolls = roll_dice(num_attacks)
    print(hit_rolls)
    total_hits = 0
    for hits in hit_rolls:
        if hits >= int(BS):
            total_hits += 1
    return total_hits

def check_wounds(toughness, strength1, rolled_dice):
    if int(strength1) * 2 <= int(toughness):
        to_wound = 2
    elif int(strength1) < int(toughness) or int(strength1) - 2 == int(toughness):
        to_wound = 3
    elif int(strength1) == int(toughness):
        to_wound = 4
    elif int(strength1) > int(toughness):
        to_wound = 5
    elif int(strength1) >= int(toughness):
        to_wound = 6
    else:
        print("Something went wrong in check_wounds: ")
    total_num_wounds = 0
    for wounds in rolled_dice:
        if wounds >= to_wound:
            total_num_wounds += 1
    return total_num_wounds


def saving_throws(num_wounds, best_sv, AP):
    num_not_saved = 0
    num_saved = 0
    save_rolls = roll_dice(num_wounds)
    print(save_rolls)
    for save_roll in save_rolls:
        adj_save_roll = save_roll-int(AP)
        if adj_save_roll >= int(best_sv):
            num_saved += 1
        else:
            num_not_saved += 1

    return num_not_saved, num_saved
    # print("Amount of wounds: " + str(num_not_saved))
    # print("Amount of save_roll: " + str(num_saved))

