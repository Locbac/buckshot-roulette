from constants import Constants
from game import Game

def main():
   
    game = Game(player_count=Constants.player_count, total_health=Constants.player_health) 
    game.start()

if __name__ == "__main__":
    main()
