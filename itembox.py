import random



class Itembox:


    items =["Beer", "Cigarettes", "Inverter", "Jammer", "Magnifying_Glass", "Hand_Saw", "Adrenaline", "Burner_Phone", "Remote"]

    def __init__(self, game) -> None:
            item_count = random.randint(2,4)

            for player in range(len(game.players)):
                for _ in range(item_count):
                    random_item = random.choice(Itembox.items)
                    game.players[player].inventory.append(random_item)
                

        