from item import Item

class Player:
    def __init__(self, total_health: int, player_name: str) -> None:
        self.total_health: int = total_health
        self.health: int = total_health
        self.inventory: list[Item] = []
        self.name: str = player_name #new   

    def take_damage(self, damage: int) -> int:
        old = self.health
        self.health = max(self.health - damage, self.health)
        return self.health - old
        

    def heal(self, amount: int) -> int:
        old = self.health
        self.health = min(self.health + amount, self.total_health)
        return self.health - old
        

    def add_item(self):
        pass

    def take_item(self, item: Item):
        self.inventory.remove(item)

 