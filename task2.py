# Paste Task 2's solution here
p1_name = "Red"
p1_position = 0
p2_name = "Blue"
p2_position = 0
snake_heads = (13,31,49,61,72)
snake_tails = (2,15,21,33,54)
ladder_bases = (8,22,36,43,51)
ladder_tops = (14,53,50,79,72)
import numpy as np
def roll_the_dice():
    return np.random.randint(1, 7)
from diceroll import roll_the_dice
diceroll = roll_the_dice()
new_p1_position = p1_position + diceroll
diceroll = roll_the_dice()
new_p2_position = p2_position + diceroll
if new_p1_position <= 100:
    p1_position = new_p1_position
if new_p2_position <= 100:
    p2_position = new_p2_position
print(p1_position,p2_position)
