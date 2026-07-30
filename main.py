# main.py
from enum import IntEnum

from constants import Constants
from shotgun import Shotgun
from player import Player
from game import Game
from constants import Constants #new
from game import Turn #new

def main():
   
    # Use getattr to avoid static attribute access issues if PLAYER_COUNT isn't recognized
    game = Game(getattr(Constants, "PLAYER_COUNT"))
    
    for i in range(Constants.player_count): #new
    for i in range(getattr()): #new
        Player_Settings.players.append(Player(total_health=Player_Settings.player_health)) #new

  

    shotgun = Shotgun()
    shotgun.randomize()
    shotgun.compact()


    print(f"Current settings: {Player_Settings.game_settings}") #new

    print("Round 1") #new, current string will be replaced with a function that will count the current round number

    #print(shotgun) #new, didnt delete incase we need to read the final output of the shotgun 
    print(f"{shotgun.live_count()} live") #new, now we can see the live and blank rounds but not the order like in buckshot
    print(f"{shotgun.blank_count()} blank") #new

    turn = Turn(Player_Settings.player_count)


if __name__ == "__main__":
    main()
