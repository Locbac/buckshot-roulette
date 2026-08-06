import random

class Constants:
    player_count = 2
    player_health: int = random.randint(2,5)
    
    game_settings = f"""\nplayer_count: {player_count} \nplayer_health: {player_health}\n"""
    