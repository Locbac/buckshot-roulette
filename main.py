# main.py
from shotgun import Shotgun
from player import Player
from game import Game
from game import Player_Settings #new
from game import Turn #new


def main():
   
    
    for i in range(Player_Settings.player_count): #new
        Player_Settings.players.append(Player(total_health=Player_Settings.player_health)) #new

    print(f"players: {Player_Settings.players[0].health}")

    shotgun = Shotgun()
    shotgun.randomize()
    shotgun.compact()


    print(f"Current settings: {Player_Settings.game_settings}") #new

    print("Round 1") #new, current string will be replaced with a function that will count the current round number

    #print(shotgun) #new, didnt delete incase we need to read the final output of the shotgun 
    print(f"{shotgun.live_count()} live") #new, now we can see the live and blank rounds but not the order like in buckshot
    print(f"{shotgun.blank_count()} blank") #new


if __name__ == "__main__":
    main()
