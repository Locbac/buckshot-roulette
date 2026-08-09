from enum import IntEnum

class Item:
    def __init__(self) -> None:
        pass

    def use(user: "Player", target: "Player", game: "Game") -> None:
        pass

class ItemType(IntEnum):
    "Beer" = 0
    "Cigarettes" = 1
    "Inverter" = 2
    "Jammer" = 3
    "Magnifying_Glass" = 4
    "Hand_Saw" = 5
    "Adrenaline" = 6
    "Burner_Phone" = 7
    "Remote" = 8