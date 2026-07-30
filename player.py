from item import Item

class Player:
    def __init__(self, total_health: int) -> None:
        self.total_health: int = total_health
        self.health: int = total_health
        self.inventory: list[Item] = []

    def take_damage(self, damage: int) -> int:
        pass

    def heal(self, amount: int) -> int:
        old = self.health
        self.health = min(self.health + amount, self.total_health)
        return self.health - old
        

    def add_item(self):
        pass

    def take_item(self, item: Item):
        self.inventory.remove(item)
