# shotgun.py
from enum import IntEnum
from typing import NamedTuple
import random
from player import Player
from itembox import Itembox

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
    
    def reload(self, game = None) -> None:
        print("reloading...")
        self.reset()
        self.randomize()
        self.compact()

        Itembox(game)

        print(f"{self.live_count()} live")
        print(f"{self.blank_count()} blank")

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

    def rack(self, game) -> Shell | None:

        print(f"racked {self.chambers[0].name}")
        self.chambers.remove(self.chambers[0])

        if self.chambers[0] == Shell.EMPTY:
           self.reload(game) 



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


    def shoot(self, user: Player, target: Player, bonus_turn, players = None): 

        if self.chambers[0] == Shell.BLANK:
            
            print("Click")

            self.chambers.remove(self.chambers[0])

            if user == target: 
               
                bonus_turn = True

        elif self.chambers[0] == Shell.LIVE:
            
            print('Bang')
            target.take_damage(self.damage)

            self.chambers.remove(self.chambers[0])

        if not self.chambers or self.chambers[0] == Shell.EMPTY:
            self.reload(players)
            
        if target.health == 0:
            target.death()

        self.damage = 1

        return bonus_turn
        
        

    def __repr__(self):
        return f"Shotgun({self.chambers})"


