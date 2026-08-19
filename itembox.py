import random
from constants import Constants


class Itembox:


    items = [
       #"beer", 
       #"cigarettes", 
        "inverter", 
       # "jammer", 
       # "magnifying_glass", 
       # "saw", 
       # "adrenaline", 
       # "burner_phone", 
       # "remote"
    ]


    def __init__(self, game, item_count: int = 0) -> None:
            item_count = random.randint(2,4)
          
            for player in range(len(game.players)):
                for _ in range(item_count):
                    if len(game.players[player].inventory) == Constants.item_limit:
                         break
                    random_item = random.choice(Itembox.items)
                    game.players[player].add_item(random_item)

