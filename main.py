# main.py
from enum import IntEnum

from constants import Constants
from shotgun import Shotgun
from player import Player
from game import Game
from constants import Constants 
from game import Turn



#what is __repr__ at the end of shotgun

def main():
   
    # Use getattr to avoid static attribute access issues if PLAYER_COUNT isn't recognized
    game = Game(getattr(Constants, "player_count"))
    
    for i in range(Constants.player_count): 
        Constants.players.append(Player(total_health=Constants.player_health)) 

    

    shotgun = Shotgun()
    print(shotgun)
    
    shotgun.randomize()
    shotgun.compact()


    print(f"Current settings: {Constants.game_settings}") 

    print("Round 1") 
    #print(shotgun) 
    print(f"{shotgun.live_count()} live") 
    print(f"{shotgun.blank_count()} blank") 

  
   
    

if __name__ == "__main__":
    main()
