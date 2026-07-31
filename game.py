from player import Player
import random 
from shotgun import Shotgun



class Game:
    def __init__(self, player_count: int = 0, total_health: int = random.randint(3,6), player_name: str = '') -> None: #player_name = new
        self.players = []
        if player_count == 0:
            return
        else:
            for i in range(player_count):
                new_player = self.create_player(total_health, player_name)
                self.name = f"Player_" + f"{i}"
                self.players.append(new_player)
                print('player created')

    def create_player(self, total_health: int, player_name: str = '') -> Player:      
        player = Player(total_health, player_name)
        
        return player
        
        
    def list_players(self, players): #new
        for x in range(len(players)):
            print(f'{players[x].name} health: {players[x].health} {players[x].inventory}')

                
    









        