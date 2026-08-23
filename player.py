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
        
        

    def heal(self, amount: int) -> int:
        old = self.health
        self.health = min(self.health + amount, self.total_health)
        return self.health - old
        

    def add_item(self, item: str ) -> None:
        self.inventory.append(item)

  #  def take_item(self, item: Item):
   #     self.inventory.remove(item)

 
    def death(self, turn_order: int, turn_count: int) -> None:
        self.alive = False
        self.health = 0
        print(f"{self.name} has been eliminated")

        if turn_order < 0:
             print(f"Turn count {turn_count}")
             turn_count = turn_count - 1
             print(f"Turn count {turn_count}")
        return(turn_count)

    def use_item_prompt(self, turn_order, game) -> None:

        option = input(f"Please select an item: {self.inventory}\n")

        if option in self.inventory:
                turn_order = Item.item_used(option, turn_order, game)
                self.inventory.remove(option)
                print(f"Turn order: {turn_order}")
                return(turn_order)
        else:
                print("not an item")
        

        