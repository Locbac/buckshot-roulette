from calendar import day_name

from game import Game, Shotgun
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
        

    def add_item(self) -> None:
        pass

    def take_item(self, item: Item):
        self.inventory.remove(item)

 
    def play(self, game: Game, shotgun: Shotgun) -> None:
        players = game.get_players()
        options = {}

        for player in players:
            options[player.name] = player
            
        """
        Try except means infinite loop until you get it right.
        """

        try:
            play_option = input("Shoot which player name?\n")
            target_player = options[play_option]

            if target_player is not None:
                print(f"Selected: {target_player.name}")
        except KeyError:
            print("Invalid player name")
            
        shotgun.shoot(user = self, target=target_player, game=game, damage=shotgun.damage)