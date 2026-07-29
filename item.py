# item.py
from __future__ import annotations
from abc import ABC, abstractmethod
from enum import IntEnum, auto
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game
    from player import Player

class ItemType(IntEnum):
    CIGARETTES = auto()
    MAGNIFYING_GLASS = auto()
    INVERTER = auto()
    ADRENALINE = auto()
    JAMMER = auto()
    PHONE = auto()
    BEER = auto()
    SAW = auto()
    REMOTE = auto()

class Item(ABC):
    item_type: ItemType  # each subclass sets this as a class attribute

    @abstractmethod
    def use(self, user: "Player", target: "Player", game: "Game") -> None:
        pass
