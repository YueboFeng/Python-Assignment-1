# Paste Task 3's solution here
import numpy as np
def roll_the_dice():
    return np.random.randint(1, 7)
from diceroll import roll_the_dice

p1_name = "Red"
p1_position = 0
p2_name = "Blue"
p2_position = 0
snake_heads = [25, 44, 65, 76, 99]
snake_tails = [6, 23, 34, 28, 56]
ladder_bases = [8, 26, 38, 47, 66]
ladder_tops = [43, 39, 55, 81, 92] 

diceroll = roll_the_dice()
new_p1_position = p1_position + diceroll
diceroll = roll_the_dice()
new_p2_position = p2_position + diceroll
if new_p1_position < 100:
    p1_position = new_p1_position
if new_p2_position < 100:
    p2_position = new_p2_position
if p1_position in snake_heads :
    index = snake_heads.index(p1_position)
    new_p1_position = snake_tails[index]
elif p1_position in ladder_bases:
    index = ladder_bases.index(p1_position)
    new_p1_position = ladder_tops[index]
else:
    new_p1_position = p1_position
if p2_position in snake_heads:
    index = snake_heads.index(p2_position)
    new_p2_position = snake_tails[index]
elif p2_position in ladder_bases:
    index = ladder_bases.index(p2_position)
    new_p2_position =ladder_tops[index]
else:
    new_p2_position = p2_position
print(new_p1_position , new_p2_position)
