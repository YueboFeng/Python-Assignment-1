# Paste Task 5's solution here
import numpy as np
def roll_the_dice():
    return np.random.randint(1, 7)
from diceroll import roll_the_dice

p1_name = "Red"
p1_position = 0
p2_name = "Blue"
p2_position = 0
p3_name = "Green"
p3_position = 0
p4_name = "White"
p4_position = 0
snake_heads = [25, 44, 65, 76, 99]
snake_tails = [6, 23, 34, 28, 56]
ladder_bases = [8, 26, 38, 47, 66]
ladder_tops = [43, 39, 55, 81, 92]
players = int(input("please input the number of players(minimum 1 and up to and including 4): "))
positions = 0
while players < 1 or players > 4:
    players = int(input("please reinput: "))
if players == 1:
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
            new_p1_position =ladder_tops[index]
            print("Player Red climbed a ladder and is now in position", new_p1_position)
        else:
            new_p1_position = p1_position
        p1_position = new_p1_position
if players == 2:
    while True:
# 1
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
# 2
        diceroll=roll_the_dice()
        new_p2_position = p2_position + diceroll
        if new_p2_position <= 100:
            p2_position = new_p2_position
            print("Player Blue is in position", p2_position)
            if p2_position == 100:
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
            indes = ladder_bases.index(p2_position)
            new_p2_position = ladder_tops[index]
            print("Player Blue climbed a ladder and is now in position", new_p2_position)
        else:
            new_p2_position = p2_position
        p2_position = new_p2_position

if players == 3:
    while True:
# 1
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
# 2
        diceroll = roll_the_dice()
        new_p2_position = p2_position + diceroll
        if new_p2_position <= 100:
            p2_position = new_p2_position
            print("Player Blue is in position", p2_position)
            if p2_position == 100:
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
            indes = ladder_bases.index(p2_position)
            new_p2_position = ladder_tops[index]
            print("Player Blue climbed a ladder and is now in position", new_p2_position)
        else:
            new_p2_position = p2_position
        p2_position = new_p2_position
# 3
        diceroll = roll_the_dice()
        new_p3_position = p3_position + diceroll
        if new_p3_position <= 100:
            p3_position = new_p3_position
            print("Player Green is in position", p3_position)
            if new_p3_position == 100:
                winner = p3_name
                print("Player", winner, "has reached 100 and is the winner!")
                break
        else:
            print("Player Green is in position",p3_position)
        if p3_position in snake_heads :
            index = snake_heads.index(p3_position)
            new_p3_position = snake_tails[index]
            print("Player Green stepped on a snake and is now in position", new_p3_position)
        elif p1_position in ladder_bases:
            index = ladder_bases.index(p3_position)
            new_p3_position = ladder_tops[index]
            print("Player Green climbed a ladder and is now in position", new_p3_position)
        else:
            new_p3_position = p3_position
        p3_position = new_p3_position
  
if players == 4:
    while True:
# 1
        diceroll=roll_the_dice()
        new_p1_position =p1_position + diceroll
        if new_p1_position <= 100:
            p1_position = new_p1_position
            print("Player Red is in position",p1_position)
            if new_p1_position == 100:
                winner = p1_name
                print("Player",winner,"has reached 100 and is the winner!")
                break
        else:
            print("Player Red is in position",p1_position)
        if p1_position in snake_heads :
            index = snake_heads.index(p1_position)
            new_p1_position = snake_tails[index]
            print("Player Red stepped on a snake and is now in position",new_p1_position)
        elif p1_position in ladder_bases:
            index = ladder_bases.index(p1_position)
            new_p1_position = ladder_tops[index]
            print("Player Red climbed a ladder and is now in position",new_p1_position)
        else:
            new_p1_position = p1_position
        p1_position = new_p1_position
# 2
        diceroll=roll_the_dice()
        new_p2_position = p2_position + diceroll
        if new_p2_position <= 100:
            p2_position = new_p2_position
            print("Player Blue is in position",p2_position)
            if p2_position == 100:
                winner = p2_name
                print("Player",winner,"has reached 100 and is the winner!")
                break
        else:
            print("Player Blue is in position",p2_position)
        if p2_position in snake_heads:
            index = snake_heads.index(p2_position)
            new_p2_position = snake_tails[index]
            print("Player Blue stepped on a snake and is now in position",new_p2_position)
        elif p2_position in ladder_bases:
            index = ladder_bases.index(p2_position)
            new_p2_position = ladder_tops[index]
            print("Player Blue climbed a ladder and is now in position",new_p2_position)
        else:
            new_p2_position = p2_position
        p2_position = new_p2_position
# 3
        diceroll=roll_the_dice()
        new_p3_position =p3_position + diceroll
        if new_p3_position <= 100:
            p3_position = new_p3_position
            print("Player Green is in position",p3_position)
            if new_p3_position == 100:
                winner = p3_name
                print("Player",winner,"has reached 100 and is the winner!")
                break
        else:
            print("Player Green is in position",p3_position)
        if p3_position in snake_heads :
            index = snake_heads.index(p3_position)
            new_p3_position = snake_tails[index]
            print("Player Green stepped on a snake and is now in position",new_p3_position)
        elif p3_position in ladder_bases:
            index = ladder_bases.index(p3_position)
            new_p3_position = ladder_tops[index]
            print("Player Green climbed a ladder and is now in position",new_p3_position)
        else:
            new_p3_position = p3_position
        p3_position = new_p3_position
# 4
        diceroll=roll_the_dice()
        new_p4_position = p4_position + diceroll
        if new_p4_position <= 100:
            p4_position = new_p4_position
            print("Player White is in position",p4_position)
            if p4_position == 100:
                winner = p4_name
                print("Player",winner,"has reached 100 and is the winner!")
                break
        else:
            print("Player White is in position",p4_position)
        if p4_position in snake_heads:
            index = snake_heads.index(p4_position)
            new_p4_position = snake_tails[index]
            print("Player White stepped on a snake and is now in position",new_p4_position)
        elif p4_position in ladder_bases:
            index = ladder_bases.index(p4_position)
            new_p4_position = ladder_tops[index]
            print("Player White climbed a ladder and is now in position",new_p4_position)
        else:
            new_p4_position = p4_position
        p4_position = new_p4_position
