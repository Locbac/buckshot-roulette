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
            self.chambers[chamber] = Shell.EMPTY

    def randomize(self):
        # fill each chamber with a random Shell
        for chamber in range(self.size):
            choices = [Shell.LIVE, Shell.BLANK, Shell.EMPTY]
            self.chambers[chamber] = random.choice(choices)

    def compact(self):
        # move EMPTY chambers to the end
        pass

    def rack(self):
        # pop/return the next chamber's shell
        pass

    def live_count(self):
        pass

    def blank_count(self):
        pass

    def __repr__(self):
        return f"Shotgun({self.chambers})"
