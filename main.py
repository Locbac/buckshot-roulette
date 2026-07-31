# main.py
from enum import IntEnum

from constants import Constants
from shotgun import Shotgun
from player import Player
from game import Game
from constants import Constants 




#what is __repr__ at the end of shotgun

def main():
   
  
    game = Game(player_count=Constants.player_count, total_health=Constants.player_health)
    
    """
    loop through game.play_turn()
    """
    
    shotgun = Shotgun()
    print(shotgun)
    
    shotgun.randomize()
    shotgun.compact()


    print(f"Current settings: {Constants.game_settings}") 

    print("Round 1") 
    #print(shotgun) 
    print(f"{shotgun.live_count()} live") 
    print(f"{shotgun.blank_count()} blank") 


    

    while True: #temp

        debug = input('debug\n')

        if debug == 'debug_shotgun' or debug == 'shoot':
            print(shotgun)
            Shotgun.shoot(shotgun) #new function

        if debug == 'list_players' or debug == 'player_list':
            game.list_players()

        if debug == 'exit':
            exit()

if __name__ == "__main__":
    main()
