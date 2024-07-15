# Paste Task 7's solution here
from diceroll import roll_the_dice, special_roll
from helpers import generate_surprises
import numpy as np
def roll_the_dice():
    return np.random.randint(1, 7)
def special_roll():
    return np.random.randint(0, 3)
def generate_surprises():
    special_tiles = np.random.choice(np.arange(1, 101), 10)
    return special_tiles

def initialise_game() -> dict:
    game = {
        "players": {'Red': 0,'Blue': 0,'Green': 0,'White': 0},
        "snakes": {'25': 6, '44': 23, '65': 34, '76': 28, '99': 56},
        "ladders": {'8': 43, '26': 39, '38': 55, '47': 81, '66': 92}
    }
    return game

def get_num_players() -> int:
    players_num = int(input("please input the number of players(minimum 1 and maximum of 4)"))
    while players_num < 1 or players_num > 4:
        players_num = int(input("please reinput"))
    z = int(players_num)
    return players_num

def play_game(game: dict) -> str:
    special_tiles_r = generate_surprises()
    i = 0
    x = 6
    while True:
        for player in game["players"].keys():
            if i == 1:
                i = 2
                continue
            if x < 4:
                x +=1
                continue
            diceroll = roll_the_dice()
            game["players"][player] += diceroll
            if game["players"][player]  <= 100:
                print("Player",player,"is in position",game["players"][player])
                if game["players"][player] == 100:
                    print("Player",player,"has reached 100 and is the winner!")
                    return player
            else:
                game["players"][player] = game["players"][player] - diceroll
                print("Player",player,"is in position",game["players"][player])

            str_list_snakes = list(game["snakes"].keys())
            int_list_snakes = [int(x) for x in str_list_snakes]
            str_list_ladders = list(game["ladders"].keys())
            int_list_ladders = [int(x) for x in str_list_ladders]
            if game["players"][player] in int_list_snakes:
                game["players"][player] = game["snakes"][str(game["players"][player])]
                print("Player",player,"stepped on a snake and is now in position",game["players"][player])
            elif game["players"][player] in int_list_ladders:
                game["players"][player] = game["ladders"][str(game["players"][player])]
                print("Player",player,"climbed a ladder and is now in position",game["players"][player])
            
            if game["players"][player] in special_tiles_r:
                print(player,"get the special tiles")
                special_roll_r = special_roll()
                current_player = player
                if special_roll_r == 0:
                    x = 1
                    print(player,"roll the",special_roll_r)            
                elif special_roll_r == 1:
                    print(player,"roll the",special_roll_r)
                    i = 1   
                else:
                    print(player,"roll the",special_roll_r)
                    for player in game["players"].keys():
                        if player != current_player:
                            if game["players"][player] <= 5:
                                game["players"][player] = 0
                                print(player,"is",game["players"][player])
                            else:
                                game["players"][player] -= 5
                                print(player,"is",game["players"][player])
                        
def pick_winner(players: dict) -> str:
    for player in players.keys():
        if players[player] == 100:
            return player
    return None

def turn_by_turn_gameplay():
    game = initialise_game()
    while True:
        for player in game["players"].keys():
            user_command = input("Enter 'roll' to roll the dice. Enter 'quit' to quit :")
            while user_command != 'roll' and user_command != 'quit':
                user_command = input("Error. Please reinput :")
            if user_command == 'roll':
                diceroll = roll_the_dice()
                game["players"][player] = game["players"][player] + diceroll
                if game["players"][player]  <= 100:
                    print("Player",player,"is in position",game["players"][player])
                    if game["players"][player] == 100:
                        print("Player",player,"has reached 100 and is the winner!")
                        return player
                else:
                    game["players"][player] = game["players"][player] - diceroll
                    print("Player",player,"is in position",game["players"][player])
                
                if game["players"][player] in game["snakes"] : 
                    game["players"][player] = game["snakes"][game["players"][player]]
                    print("Player",player,"stepped on a snake and is now in position",game["players"][player])
                elif game["players"][player] in game["ladders"]:
                    game["players"][player] = game["ladders"][game["players"][player]]
                    print("Player",player,"climbed a ladder and is now in position",game["players"][player])
            else:
                return None

def main():
    game = initialise_game()
    num_players = get_num_players()
    winner = play_game(game)
    print(f"The winner is {winner}!")
    turn_by_turn_gameplay()

if __name__ == '__main__':
    main()
