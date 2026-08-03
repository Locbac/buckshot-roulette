# main.py
from constants import Constants
from shotgun import Shotgun
from game import Game





#what is __repr__ at the end of shotgun

def main():
   
  
    game = Game(player_count=Constants.player_count, total_health=Constants.player_health)
    
    """
    loop through game.play_turn()
    """
    
    shotgun = Shotgun()
    shotgun.randomize()
    shotgun.compact()


    print("Round 1") 
    print(f"{shotgun.live_count()} live") 
    print(f"{shotgun.blank_count()} blank")


    print("main")

    game.start()

    

    while True: #temp

        debug = input('debug\n')

        if debug == 'debug_shotgun' or debug == 'shoot':
            print(shotgun)
            Shotgun.shoot(shotgun) #new function

        if debug == 'list_players' or debug == 'player_list':
            game.list_players()

        if debug == 'exit':
            exit()

        if debug == 'start':
           game.start()

        if debug == 'turn':
            game.turn()
            
        if debug == 'settings':
            print(f"Current settings: {Constants.game_settings}") 

if __name__ == "__main__":
    main()
