from constants import Constants
from game import Game

def main():

    while True:
        game = Game(player_count = Constants.player_count, total_health = Constants.total_health) 
        game.start()
        # amon: you cooked with cleaning up main

if __name__ == "__main__":
    main()
