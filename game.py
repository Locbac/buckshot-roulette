from player import Player
import random # new, moved from main

class Game:
    def __init__(self, player_count: int = 0, total_health: int = random.randint(3,6)) -> None:
        self.players = []
        if player_count == 0:
            return
        else:
            for i in range(player_count):
                new_player = self.create_player(total_health)
                self.players.append(new_player)

    def create_player(self, total_health: int) -> Player:
        player = Player(total_health)
        return player
        
        


class Turn: # new
    def __init__(self, playercount):
        self.playercount = playercount
        for players in range(playercount):
            pass


                
    









        