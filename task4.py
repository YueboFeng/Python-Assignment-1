# Paste Task 4's solution here
p1_name = "Red"
p1_position = 0
p2_name = "Blue"
p2_position = 0
snake_heads = [25, 44, 65, 76, 99]
snake_tails = [6, 23, 34, 28, 56]
ladder_bases = [8, 26, 38, 47, 66]
ladder_tops = [43, 39, 55, 81, 92]

import numpy as np
def roll_the_dice():
    return np.random.randint(1, 7)
from diceroll import roll_the_dice

while True:
    diceroll = roll_the_dice()
    new_p1_position = p1_position + diceroll
    if new_p1_position <= 100:
        p1_position = new_p1_position
        print("Player Red is in position", p1_position)
        if new_p1_position == 100:
            winner = p1_name
            print("Player", winner, "has reached 100 and is the winner!")
            break
    else:
        print("Player Red is in position", p1_position)
    if p1_position in snake_heads :
        index = snake_heads.index(p1_position)
        new_p1_position = snake_tails[index]
        print("Player Red stepped on a snake and is now in position", new_p1_position)
    elif p1_position in ladder_bases:
        index = ladder_bases.index(p1_position)
        new_p1_position = ladder_tops[index]
        print("Player Red climbed a ladder and is now in position", new_p1_position)
    else:
        new_p1_position = p1_position
    p1_position = new_p1_position
    diceroll = roll_the_dice()
    new_p2_position = p2_position + diceroll
    if new_p2_position <= 100:
        p2_position = new_p2_position
        print("Player Blue is in position", p2_position)
        if new_p2_position == 100:
            winner = p2_name
            print("Player", winner, "has reached 100 and is the winner!")
            break
    else:
        print("Player Blue is in position", p2_position)
    if p2_position in snake_heads:
        index = snake_heads.index(p2_position)
        new_p2_position = snake_tails[index]
        print("Player Blue stepped on a snake and is now in position", new_p2_position)
    elif p2_position in ladder_bases:
        index = ladder_bases.index(p2_position)
        new_p2_position = ladder_tops[index]
        print("Player Blue climbed a ladder and is now in position", new_p2_position)
    else:
        new_p2_position = p2_position
    p2_position = new_p2_position
