# main.py
from shotgun import Shotgun
from player import Player
from game import Game
import random

def main():
    players = []
    player_count = 2
    
    player_health: int = random.randint(3,6)
    
    for i in range(player_count):
        players.append(Player(total_health=player_health))
    shotgun = Shotgun()
    shotgun.randomize()
    shotgun.compact()
    print(shotgun)

if __name__ == "__main__":
    main()
