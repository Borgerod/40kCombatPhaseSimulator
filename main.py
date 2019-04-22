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


# This function returns the amount of integers in the list that is above the hit number
def check_hits(hit_number, rolled_dice):
    total_hit_number = 0
    length = len(rolled_dice)
    # print(length)
    for hits in rolled_dice:
        if hits >= int(hit_number):
            total_hit_number += 1
    return total_hit_number


def check_wounds(toughness, strength1, rolled_dice):
    if int(strength1) - 3 == int(toughness):
        wound_number = 2
    elif int(strength1) - 1 == int(toughness) or int(strength1) - 2 == int(toughness):
        wound_number = 3
    elif int(strength1) == int(toughness):
        wound_number = 4
    elif int(strength1) + 1 == int(toughness) or int(strength1) + 2 == int(toughness):
        wound_number = 5
    elif int(strength1) + 3 == int(toughness):
        wound_number = 6
    else:
        print("Something went wrong in check_wounds: ")
    # print("This is wound number: " + str(wound_number))
    total_wound_number = 0
    length = len(rolled_dice)
    #print(length)
    for wounds in rolled_dice:
        if wounds >= wound_number:
            total_wound_number += 1
    return total_wound_number


def saving_throws(wound_dice, best_sv):
    amt_wounds = 0
    amt_saves = 0
    wound_list = roll_dice(wound_dice)
    for saves in wound_list:
        if saves >= int(best_sv):
            amt_saves += 1
        else:
            amt_wounds += 1

    return amt_wounds, amt_saves
    # print("Amount of wounds: " + str(amt_wounds))
    # print("Amount of saves: " + str(amt_saves))


"""
# -----------------------------------Main Function---------------
p = "a"
while p != "q":
    number_of_dice = input("How many attacks are you rolling?: ")
    hit_number = input("What is the Ballistic skill/weapon skill of the user?: ")
    strength = input("What is the strength of the user(modified with weapon): ")
    Toughness = input("What is the toughness of the target?: ")

    i = roll_dice(number_of_dice)
    t = check_hits(hit_number, i)
    a = roll_dice(t)
    b = check_wounds(Toughness, strength, a)
    print("This is the amount of wounds that you got: " + str(b))

    x = input("What is the best save that the unit has?(accounting for ap): ")
    saving_throws(b, x)

    p = input("press any key to run again, Press q to quit: ")


# ---------------------------------------------------------------

# random_accuracy_test()
"""
