from constants import Constants
from game import Game

def main():

    while True:
        game = Game(player_count=Constants.player_count) 
        game.start()

if __name__ == "__main__":
    main()
