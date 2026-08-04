from player import Player
from shotgun import Shotgun
import random 

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
                player_name = f"player_{i+1}"
                new_player = self.create_player(total_health, player_name)
                self.players.append(new_player)

    def create_player(self, total_health: int, player_name: str = '') -> Player:      
        player = Player(total_health, player_name)
        
        return player
        
        
    def list_players(self):
        for x in range(len(self.players)):
            print(f"""
            {self.players[x].name} 
            health: {self.players[x].health} 
            items: {self.players[x].inventory}, 
            turn: {self.players[x].isturn}""")
            

    def start(self) -> None:

        shotgun = Shotgun()
        shotgun.randomize()
        shotgun.compact()

        random.shuffle(self.players)

        print("turn order:")
        for x in range(len(self.players)): print(self.players[x].name) 

        self.current_turn = self.players[0]
        self.turn(shotgun)
        

    def turn(self, shotgun) -> None:

        while True:
            print(f'{self.current_turn.name}s turn')
            self.current_turn.isturn = True

            print('Options:')
            self.list_players()

            shoot_choice_name = input(f'You are {self.current_turn.name}, Please select a player to shoot\n')

            for player in range(len(self.players)):
                if shoot_choice_name == self.players[player].name:
                   shoot_choice = self.players[player]
                   break


            if shoot_choice.name == self.current_turn.name:
                print('You shot yourself')
                Shotgun.shoot(shotgun, self.current_turn, shoot_choice)
            
            else:
                for player in range(len(self.players)):
                    if self.players[player].name == shoot_choice.name and self.players[player].name != self.current_turn.name:
                        
                        print(f"{self.current_turn.name} shot {self.players[player].name}")
                        Shotgun.shoot(shotgun, self.current_turn, shoot_choice)
                        break

            pause = input('')
        
       
       
        