# shotgun.py
from enum import IntEnum
from typing import NamedTuple
import random

from game import Game
from player import Player

class Shell(IntEnum):
    EMPTY = 0
    LIVE = 1
    BLANK = 2

class ChamberResult(NamedTuple):
    idx: int
    shell: Shell

class Shotgun:
    def __init__(self, size: int = 8) -> None:
        self.size = size
        self.chambers = []
        self.damage: int = 1
        self.reset()
    
    def reload(self) -> None:
        print("reloading...")
        self.reset()
        self.randomize()
        self.compact()

    def reset(self) -> None:
        # fill self.chambers with EMPTY, size long
        for chamber in range(self.size):
            self.chambers.append(Shell.EMPTY)

    def randomize(self) -> None:
        # fill each chamber with a random Shell
        for chamber in range(self.size):
            choices = [Shell.LIVE, Shell.BLANK, Shell.EMPTY]
            self.chambers[chamber] = random.choice(choices)

    def compact(self) -> None:
        # move EMPTY chambers to the end
        non_empty = [x for x in self.chambers if x != Shell.EMPTY]
        number_to_pad_by = self.size - len(non_empty)
        self.chambers = non_empty + [Shell.EMPTY]*number_to_pad_by

    def rack(self) -> Shell | None:
        # pop/return the next chamber's shell
        _first_non_empty = self.first_non_empty()
        if _first_non_empty is None:
            return
        else: 
            self.chambers[_first_non_empty.idx] = Shell.EMPTY
            return _first_non_empty.shell

    def live_count(self) -> int:
        count = 0
        for chamber in range(self.size):
            if self.chambers[chamber] == Shell.LIVE:
                count += 1
        return count
            

    def blank_count(self) -> int:
        count = 0
        for chamber in range(self.size):
            if self.chambers[chamber] == Shell.BLANK:
                count += 1
        return count


    def empty_count(self) -> int:
        count = 0
        for chamber in range(self.size):
            if self.chambers[chamber] == Shell.EMPTY:
                count += 1
        return count

    def first_non_empty(self) -> ChamberResult | None:
        for chamber in range(self.size):
            shell = self.chambers[chamber]
            if shell != Shell.EMPTY:
                return ChamberResult(chamber, shell)
        return None

    def shoot(self, user: Player, target: Player, game: Game, damage: int = 1) -> int: #new

        if self.chambers[0] == Shell.BLANK:
            
            print("Click")
            self.chambers.remove(self.chambers[0])
            if user == target: 
                print("extra turn")

        elif self.chambers[0] == Shell.LIVE:
            
            print('Bang')
            target.take_damage(self.damage)
            self.chambers.remove(self.chambers[0])

        if self.chambers[0] == Shell.EMPTY:
            self.reload()
            
                 
        
        print(self)
        

    def __repr__(self):
        return f"Shotgun({self.chambers})"


