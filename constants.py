import random

class Constants:
    player_count = 4
    player_health: int = random.randint(3,6)
    
    game_settings = f"""\nplayer_count: {player_count} \nplayer_health: {player_health}\n"""
    