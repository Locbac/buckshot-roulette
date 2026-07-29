# shotgun.py
from enum import IntEnum
import random

class Shell(IntEnum):
    EMPTY = 0
    LIVE = 1
    BLANK = 2

class Shotgun:
    def __init__(self, size=8):
        self.size = size
        self.chambers = []
        self.reset()

    def reset(self):
        # fill self.chambers with EMPTY, size long
        for chamber in range(self.size):
            self.chambers.append(Shell.EMPTY)

    def randomize(self):
        # fill each chamber with a random Shell
        for chamber in range(self.size):
            choices = [Shell.LIVE, Shell.BLANK, Shell.EMPTY]
            self.chambers[chamber] = random.choice(choices)

    def compact(self):
        # move EMPTY chambers to the end
        non_empty = [x for x in self.chambers if x != Shell.EMPTY]
        number_to_pad_by = self.size - len(non_empty)
        self.chambers = non_empty + [Shell.EMPTY]*number_to_pad_by

    def rack(self):
        # pop/return the next chamber's shell
        first_non_empty_chamber = self.first_non_empty(self)
        value = self.chambers[first_non_empty_chamber]
        self.chambers[first_non_empty_chamber] = Shell.EMPTY
        return value

    def live_count(self):
        count = 0
        for chamber in range(self.size):
            if self.chambers[chamber] == Shell.LIVE:
                count += 1
        return count
            

    def blank_count(self):
        count = 0
        for chamber in range(self.size):
            if self.chambers[chamber] == Shell.BLANK:
                count += 1
        return count


    def empty_count(self):
        count = 0
        for chamber in range(self.size):
            if self.chambers[chamber] == Shell.EMPTY:
                count += 1
        return count

    def first_non_empty(self):
        for chamber in range(self.size):
            if chamber != Shell.EMPTY:
                return chamber

    def __repr__(self):
        return f"Shotgun({self.chambers})"
