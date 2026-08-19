from player import Player
from shotgun import Shotgun
from itembox import Itembox

import random 

class Game:
    def __init__(self, \
                player_count: int = 0, \
                total_health: int | None = None, \
            ) -> None: #player_name = new
        
        self.players: list[Player] = []
        self.current_turn: Player
        self.shotgun: Shotgun

        
        
        if player_count == 0:
            return
        else:
            for i in range(player_count):
                player_name = f"player_{i+1}"
                new_player = self.create_player(total_health, player_name)
                self.players.append(new_player)

    def create_player(self, total_health: int, player_name: str = '') -> Player:      
        return Player(total_health, player_name)
        
        
    def list_players(self):
        for player in self.players:
            print(
            f"{player.name}\t"
            f"health: {player.health}\t" 
            f"turn: {player.isturn}\t"
            f"alive: {player.alive}\t"
            f"items: {player.inventory}\t")
            

    def start(self) -> None:

        self.shotgun = Shotgun()
        
        self.shotgun.randomize()
        self.shotgun.compact()

        random.shuffle(self.players)
       
        Itembox(self)
      

        self.turn(self.shotgun)

        
        

    def turn(self, shotgun) -> None:

        turn_count = 0 # I like this tbh
        alive_players: list[Player] = self.players.copy()
  
        bonus_turn = False

        # for player in range(len(self.players)):
        #     alive_players.append(self.players[player])

        print(f"{shotgun.live_count()} live")
        print(f"{shotgun.blank_count()} blank")

        self.current_turn = alive_players[turn_count]
        self.current_turn.isturn = True
        current_turn_player: Player = self.current_turn


    
        while True: 
            self.list_players()
 
            while True:
               # try:

                    options = input(f"""{current_turn_player.name} choose an option:\nshoot       item\n""")

                    if options == 'item':
                        current_turn_player.use_item_prompt(game=self)

                    elif options == 'shoot':
                        bonus_turn = self.shoot_choice(alive_players, shotgun, current_turn_player, bonus_turn)

                        if bonus_turn:
                            print("extra turn")
                            bonus_turn = False
                        else:
                            break
              #  except Exception:
                  # print("Invalid input, please try again")

            self.check_alive_players(alive_players)
            if self.check_game_over(alive_players):
                break
            
            current_turn_player, turn_count = self.next_turn(current_turn_player, alive_players, turn_count)

            #next round

            
    def next_turn(self, current_turn, alive_players, turn_count):

        turn_count += 1  
        if turn_count > len(alive_players)-1:
            turn_count = 0
            
        self.current_turn.isturn = False
        self.current_turn = alive_players[turn_count]
        self.current_turn.isturn = True
        current_turn = self.current_turn
         
        return(current_turn, turn_count)

            
    def shoot_choice(self, alive_players, shotgun, current_turn, bonus_turn):
   

        shoot_choice_name = input(f'You are {current_turn.name}, Please select a player to shoot\n')
        
        for player in alive_players:
            if shoot_choice_name == player.name:
                shoot_choice = player
                break
        
        if shoot_choice.name == current_turn.name:
            print('You shot yourself')
            bonus_turn = Shotgun.shoot(shotgun, current_turn, shoot_choice, bonus_turn, self)
            
                    
        else:
            for player in range(len(alive_players)):
                if alive_players[player].name == shoot_choice.name and alive_players[player].name != current_turn.name:    
                    print(f"{current_turn.name} shot {alive_players[player].name}")
                    bonus_turn = Shotgun.shoot(shotgun, current_turn, shoot_choice, bonus_turn, self)
                    break
    
        return bonus_turn

    def check_alive_players(self, alive_players):
        for player in range(len(alive_players)):
            if alive_players[player].alive == False:   
                alive_players.remove(alive_players[player])
                break

    def check_game_over(self, alive_players):
        if len(alive_players) == 1:
            print(f"{alive_players[0].name} has won the game!")
            alive_players[0].wins =+ 1

            print("Next round")
            return True
        return(False)

        
   
   
         

        