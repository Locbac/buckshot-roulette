from player import Player
import random # new, moved from main


class Player_Settings: #new, I decided to move the game settings to our game.py so main can be reserved for executing the code
    players = []
    player_count = 2
    player_health: int = random.randint(3,6)

    game_settings = f"""\nplayer_count: {player_count} \nplayer_health: {player_health}\n"""





class Game:
    def __init__(self, players: list[Player]) -> None:
        self.players = players


class Turn: # new
    def __init__(self, playercount):
        self.playercount = playercount
        for players in range(playercount):
            pass


                
    









        