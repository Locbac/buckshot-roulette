from item import Item

class Player:
    def __init__(self, total_health: int, player_name: str, is_turn: bool = False, alive: bool = True, wins: int = 0) -> None:
        self.total_health: int = total_health
        self.health: int = total_health
        self.inventory: list = []
        self.name: str = player_name #new   
        self.isturn: bool = is_turn
        self.alive: bool = alive
        self.wins: int = wins

    def take_damage(self, damage: int) -> int:
        old = self.health
        self.health = max(self.health - damage, 0)
        damage_taken = old - self.health
        print(f"{self.name} took {damage_taken} damage")
        print(f"{self.name} now at {self.health} health")
        return damage_taken
        

    def heal(self, amount: int) -> int:
        old = self.health
        self.health = min(self.health + amount, self.total_health)
        return self.health - old
        

    def add_item(self, item: str ) -> None:
        self.inventory.append(item)

  #  def take_item(self, item: Item):
   #     self.inventory.remove(item)

 
    def death(self) -> None:
        self.alive = False
        self.health = 0
        print(f"{self.name} has been eliminated")
        

    def use_item_prompt(self, game) -> None:

        option = input(f"Please select an item: {self.inventory}\n")

        if option in self.inventory:
                Item.item_used(option, game)
                self.inventory.remove(option)
        else:
                print("not an item")
        

        