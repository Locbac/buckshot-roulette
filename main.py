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
    
  
    game.start()

    


if __name__ == "__main__":
    main()
