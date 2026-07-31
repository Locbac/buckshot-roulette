from player import Player
import random 
from shotgun import Shotgun



class Game:
    def __init__(self, \
                player_count: int = 0, \
                total_health: int = random.randint(3,6), \
            ) -> None: #player_name = new
        
        self.players: list[Player] = []
        self.current_turn: Player

        
        if player_count == 0:
            return
        else:
            for i in range(player_count):
                player_name = f"Player_{i+1}"
                new_player = self.create_player(total_health, player_name)
                self.players.append(new_player)
                print('player created')

    def create_player(self, total_health: int, player_name: str = '') -> Player:      
        player = Player(total_health, player_name)
        
        return player
        
        
    def list_players(self) -> list[Player]: #new
        for x in range(len(self.players)):
            print(f'{self.players[x].name} health: {self.players[x].health} items: {self.players[x].inventory}')
        return self.players
    
    def start(self) -> None:
        random.shuffle(self.players)
        self.current_turn = self.players[0]

    def play_turn(self) -> None:
        self.current_turn.play()

    def next_turn(self):
        pass