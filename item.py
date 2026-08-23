

class Item:
     
     def beer(item: str, game):
            print(game.shotgun)
            print("you used the beer")
            game.shotgun.rack(game)
            print(game.shotgun)

     def magnifying_glass(item:str, game):
          print(game.shotgun)
          print(game.shotgun.chambers[0].name)

     def saw(item:str, game):
          game.shotgun.damage = 2
          

     def cigarettes(item:str, game):
          
          if game.current_turn.total_health > game.current_turn.health: 
               game.current_turn.health += 1
               print(f"{game.current_turn.name} healed 1 hp")

     def inverter(item:str, game):
          from shotgun import Shell

          print(game.shotgun)
          if game.shotgun.chambers[0] == 1:
               game.shotgun.chambers[0] = Shell.BLANK
               print(game.shotgun)

          elif game.shotgun.chambers[0] == 2:
               game.shotgun.chambers[0] = Shell.LIVE
               print(game.shotgun)  

     def remote(turn_order):
          turn_order = turn_order * -1
          
          return(turn_order)

     def item_used(item: str, turn_order, game: None):
        match item:
            case 'beer':
                Item.beer(item, game)

            case 'magnifying_glass':
                  Item.magnifying_glass(item, game)

            case 'saw':
                  Item.saw(item, game)

            case 'cigarettes':
                  Item.cigarettes(item, game)

            case 'inverter':
                  Item.inverter(item, game)

            case 'remote':
                  turn_order = Item.remote(turn_order)
                  return(turn_order)  





















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

