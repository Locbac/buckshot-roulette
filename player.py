class Player:
    def __init__(self, total_health: int) -> None:
        self.total_health: int = total_health
        self.items = []

    def take_damage(self, damage: int) -> int:
        pass

    def add_item(self):
        pass

    def take_item(self):
        pass
