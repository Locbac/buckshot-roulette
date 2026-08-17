

class Item:

     def beer(item: str, game):
            print(game.shotgun)
            print("you used the beer")
            game.shotgun.rack(game)
            print(game.shotgun)


     def item_used(item: str, shotgun: list):
        match item:
            case 'beer':
                Item.beer(item, shotgun)    
            
   






















# I wasnt sure how to use any of this, I put it down here
#        from enum import IntEnum 

#      def __init__(self) -> None:
     #   pass

    #def use(user: "Player", target: "Player", game: "Game") -> None:
      #  pass

    #class ItemType(IntEnum):
        #"beer" = 0
       # "cigarettes" = 1
      #  "inverter" = 2
     #   "jammer" = 3
    #    "magnifying_glass" = 4
   #     "hand_saw" = 5
  #      "adrenaline" = 6
 #       "burner_phone" = 7
#        "remote" = 8

