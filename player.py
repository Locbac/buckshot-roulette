from calendar import day_name



from item import Item


class Player:
    def __init__(self, total_health: int, player_name: str, is_turn: bool = False, alive: bool = True) -> None:
        self.total_health: int = total_health
        self.health: int = total_health
        self.inventory: list[Item] = []
        self.name: str = player_name #new   
        self.isturn: bool = is_turn
        self.alive: bool = alive

    def take_damage(self, damage: int) -> int:
        current_health = self.health
        self.health = current_health - damage
        print(f"{self.name} took {damage} damage")
        

    def heal(self, amount: int) -> int:
        old = self.health
        self.health = min(self.health + amount, self.total_health)
        return self.health - old
        

    def add_item(self) -> None:
        pass

    def take_item(self, item: Item):
        self.inventory.remove(item)

 
    def death(self) -> None:
        self.alive = False
        print(f"{self.name} has been eliminated")
        
