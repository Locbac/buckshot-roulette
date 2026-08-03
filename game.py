from player import Player
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
                print('player created')

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
        random.shuffle(self.players)


        print("hi")
        print("turn order:")
        for x in range(len(self.players)): print(self.players[x].name) 

        
        #print(f"other players: {other_players}")

        self.current_turn = self.players[0]


        
        self.turn()
        

    def turn(self) -> None:

        print(f'{self.current_turn.name}s turn')
        self.current_turn.isturn = True

        print('Options:')
        self.list_players()

        shoot_choice = input(f'You are {self.current_turn.name}, Please select a player to shoot\n')

        if shoot_choice == self.current_turn.name:
            print('You shot yourself')
        elif shoot_choice == any(self.players):
            print(f"You shot {shoot_choice}")
        else:
            print("error")
        

       

        
        