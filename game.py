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
        for player in self.players:
            print(
            f"{player.name}\t"
            f"health: {player.health}\t" 
            f"items: {player.inventory}\t" 
            f"turn: {player.isturn}\t"
            f"alive: {player.alive}\t")
            

    def start(self) -> None:

        shotgun = Shotgun()
        shotgun.randomize()
        shotgun.compact()

        random.shuffle(self.players)
        self.turn(shotgun)
        

    def turn(self, shotgun) -> None:

        turn_count = 0
        alive_players = []

        for player in range(len(self.players)):
            alive_players.append(self.players[player])

        print(f"{shotgun.live_count()} live")
        print(f"{shotgun.blank_count()} blank")

        self.current_turn = alive_players[turn_count]
        self.current_turn.isturn = True
        current_turn = self.current_turn

        while True: 
            self.list_players()
            self.shoot_choice(alive_players, shotgun, current_turn)
            self.check_alive_players(alive_players)
            current_turn, turn_count = self.next_turn(current_turn, alive_players, turn_count)

            
    def next_turn(self, current_turn, alive_players, turn_count):

          
        
         self.current_turn.isturn = False
         self.current_turn = alive_players[turn_count]
         self.current_turn.isturn = True
         current_turn = self.current_turn
         
         
         turn_count = turn_count + 1
         if turn_count > len(alive_players)-1:
                     turn_count = 0
         return(current_turn, turn_count)

            
    def shoot_choice(self, alive_players, shotgun, current_turn):

        shoot_choice_name = input(f'You are {current_turn.name}, Please select a player to shoot\n')
        
        for player in alive_players:
            if shoot_choice_name == player.name:
                shoot_choice = player
                break
        
        if shoot_choice.name == current_turn.name:
            print('You shot yourself')
            Shotgun.shoot(shotgun, current_turn, shoot_choice)
                    
        else:
            for player in range(len(alive_players)):
                if alive_players[player].name == shoot_choice.name and alive_players[player].name != current_turn.name:    
                    print(f"{current_turn.name} shot {alive_players[player].name}")
                    Shotgun.shoot(shotgun, current_turn, shoot_choice)
                    break


    def check_alive_players(self, alive_players):
        for player in range(len(alive_players)):
            if alive_players[player].alive == False:   
                alive_players.remove(alive_players[player])
                break

        if len(alive_players) == 1:
            print(f"{alive_players[0].name} has won the game!")    

   
        