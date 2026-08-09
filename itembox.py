import random



class Itembox:


    items = [
        "Beer", 
        "Cigarettes", 
        "Inverter", 
        "Jammer", 
        "Magnifying_Glass", 
        "Hand_Saw", 
        "Adrenaline", 
        "Burner_Phone", 
        "Remote"
    ]
    """
    amon: I think it would make sense to do it the old way
    have a class Item:
    Then have the same IntEnum thing, just a formality.
    But we can then have Item.Beer Item.Cigarettes, etc.
    Then we have like a new class for each type of item as a 'subclass'.
    That way, all we need to know - from pov of the Game class. Is that
    someone is using an item.
    """

    def __init__(self, item_count: int, game: "Game") -> None:
            #old: item_count = random.randint(2,4)
            """
            amon: I think it makes more sense to randomize it when calling 
            to create a new itembox from the game class or main class.
            that way it's easier to coordinate the exact same random
            number of items for ALL itemboxes in that round.
            """
            for player in range(len(game.players)):
                for _ in range(item_count):
                    random_item = random.choice(Itembox.items)
                    #old: game.players[player].inventory.append(random_item)
                    """
                    amon: I'm using the new add_item method (tap in)
                    side note, this is cause it's apparently bad practice to
                    directly modify (attributes / properties) from a class.
                    you're supposed to use a method for best practices
                    """
                    game.players[player].add_item(random_item)

