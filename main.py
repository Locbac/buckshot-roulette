# main.py
from shotgun import Shotgun
from player import Player

def main():
    shotgun = Shotgun()
    shotgun.randomize()
    shotgun.compact()
    print(shotgun)

if __name__ == "__main__":
    main()
