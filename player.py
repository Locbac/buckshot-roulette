from item import Item

class Player:
    def __init__(self, total_health: int) -> None:
        self.total_health: int = total_health
        self.health: int = total_health
        self.inventory: list[Item] = []

    def take_damage(self, damage: int) -> int:
        pass

    def heal(self, amount: int) -> int:
        if self.health + amount >= self.total_health:
            self.health = self.total_health
        else:
            self.health += 1

    def add_item(self):
        pass

    def take_item(self, item: Item):
        self.inventory.remove(item)
