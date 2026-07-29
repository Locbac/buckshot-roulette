import math
import random

#0 = skip
#1 = live
#2 = blank 
EMPTY = 0
LIVE = 1
BLANK = 2
MAG_SIZE = 8



def main():
    shotgun = []

    for chamber in range(MAG_SIZE):
        shotgun.append(EMPTY)

    print(f"Init: {shotgun}")


    for chamber in range(MAG_SIZE):
        random_number = random.randint(0,2)
        shotgun[chamber] = random_number


    print(f"Randomized Init: {shotgun}")

    #
    #  We now need to move all EMPT[ies] to the end.
    #
    #  Elegant solution? Without having to loop through, many times, 
    #  remove all "EMPTY" chambers, then pad it 0's till
    #  we get to 8 in the chamber.
    #

    non_empty = [x for x in shotgun if x != EMPTY] # some cool shit I remember from last week CS first year.
    number_to_pad_by = MAG_SIZE - len(non_empty)
    shotgun = non_empty + [EMPTY]*number_to_pad_by

    # 
    #  Now sanity checks
    # 

    print(f"FRONT LOADED: {shotgun}")

if __name__ == "__main__":
    main()
