# items/cigarettes.py
from item import Item, ItemType

class Cigarettes(Item):
    item_type = ItemType.CIGARETTES

    def use(self, user: "Player", target: "Player", game: "Game") -> None:
        user.heal(1)
