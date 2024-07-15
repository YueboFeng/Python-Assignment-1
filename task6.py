# Paste Task 6's solution here
from diceroll import roll_the_dice
from typing import Tuple
import numpy as np
def roll_the_dice():
    return np.random.randint(1, 7)

def initialise_game() -> Tuple[list, list, list, list, list, list]:
    players = ["Red","Blue","Green","White"]
    positions = [0,0,0,0]
    snake_heads = [25, 44, 65, 76, 99]
    snake_tails = [6, 23, 34, 28, 56]
    ladder_bases = [8, 26, 38, 47, 66]
    ladder_tops = [43, 39, 55, 81, 92]
    return players,positions,snake_heads,snake_tails,ladder_bases,ladder_tops
def get_num_players() -> int:
    players_num = int(input("please input the number of players(minimum 1 and maximum of 4)"))
    while players_num < 1 or players_num > 4:
        players_num = int(input("please reinput"))
    return players_num
def play_game(players, positions,snake_heads, snake_tails, ladder_bases, ladder_tops) -> list:
    while True:
        for player in range(len(players)):
            diceroll=roll_the_dice()
            positions[player] =positions[player] + diceroll
            if positions[player]  <= 100:
                print(players[player],"is in position",positions[player])
                if positions[player] == 100:
                    print(players[player],"has reached 100 and is the winner!")
                    return positions
            else:
                positions[player] = positions[player] - diceroll
                print(players[player],"is in position",positions[player])
# Check if player 1 is either on a snake head or ladder Base
            if positions[player] in snake_heads :
                index = snake_heads.index(positions[player])
                positions[player] = snake_tails[index]
                print(players[player],"stepped on a snake and is now in position",positions[player])
            elif positions[player] in ladder_bases:
                index = ladder_bases.index(positions[player])
                positions[player] =ladder_tops[index]
                print(players[player],"climbed a ladder and is now in position",positions[player])
    # DELETE the line below when you implement the function
    # raise NotImplementedError
def pick_winner(positions):
    for player in range(len(positions)):
        if positions[player] == 100:
            return player
    return -1
    # DELETE the line below when you implement the function
    # raise NotImplementedError
def main():
    players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops = initialise_game()
    num_players = get_num_players()
    final_positions = play_game(players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops)
    winner = pick_winner(final_positions)
    print(f"The winner is {players[winner]}!")

if __name__ == '__main__':
    main()
