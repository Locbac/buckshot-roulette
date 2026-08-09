from player import Player
from shotgun import Shotgun
from itembox import Itembox

import random 

class Game:
    def __init__(self, \
                player_count: int = 0, \
                total_health: int | None = None, \
            ) -> None: #player_name = new
        
        self.players: list[Player] = []
        self.current_turn: Player
        self.shotgun: Shotgun

        total_health = random.randint(2,5)
        
        if player_count == 0:
            return
        else:
            for i in range(player_count):
                player_name = f"player_{i+1}"
                new_player = self.create_player(total_health, player_name)
                self.players.append(new_player)

    def create_player(self, total_health: int, player_name: str = '') -> Player:      
        return Player(total_health, player_name)
        
        
    def list_players(self):
        for player in self.players:
            print(
            f"{player.name}\t"
            f"health: {player.health}\t" 
            f"turn: {player.isturn}\t"
            f"alive: {player.alive}\t"
            f"items: {player.inventory}\t")
            

    def start(self) -> None:

        self.shotgun = Shotgun()
        """
        amon: one thing I'm noticing on first overview of the code, 
        we create a shotgun in the game, I remember in the drawing we made -
        maybe not though - at least I said that it made sense to have
        the game *own* the shotgun, then the players use it.
        Because the shotguns aren't owned by each player, it's per game, there's ONE shotgun.

        so I think it would make sense to create maybe self.shotgun: list[Shotgun] = [].
        or maybe even simpler, self.shotgun: Shotgun.
        So we always have a reference to it I guess.
        """
        self.shotgun.randomize()
        self.shotgun.compact()

        random.shuffle(self.players)
        Itembox(self)
        """
        amon: for item box... I'm thinking. A dictionary.
        {
            "Player_1" = \
                Itembox(
                    Item(type0)
                    Item(type1)
                    ...
                    Item(typen)
                )
            "Player_2" = ...
        }
        Like we assign an itembox to each player. Linked via
        the player's name as the key. Then the value is just a whole
        ass itembox class. Like a new memory address pointing to
        a new itembox class instance.

        The thing is, that follow the common sense. Like the game
        hands out itemboxes right. The `Game` class should keep track of it.

        Thing is, I'm not sure if that's easier, or if just letting
        player class keep track of it makes sense.

        Realistically, that's not what happens. But, I think it would be easier.
        OR.
        We don't mess with who owns it. Just have it run.
        Then immediately unpack all the items into the player's inventory.

        I think that's easiest.
        """

        self.turn(self.shotgun)

        
        

    def turn(self, shotgun) -> None:

        turn_count = 0 # I like this tbh
        alive_players = []
        """
        amon: would it make sense to just copy the players list
        from self.players as a copied list, not a copy of the reference?
        alive_players: list[Player] = self.players.copy()
        """
        bonus_turn = False

        for player in range(len(self.players)):
            alive_players.append(self.players[player])

        print(f"{shotgun.live_count()} live")
        print(f"{shotgun.blank_count()} blank")

        self.current_turn = alive_players[turn_count]
        self.current_turn.isturn = True
        current_turn = self.current_turn

       

        while True: 
            self.list_players()

            while True:
                try:

                    options = input(f"""{current_turn.name} choose an option:\nshoot       use_item\n""")

                    if options == 'use_item':
                        self.use_item(current_turn)

                    elif options == 'shoot':
                        bonus_turn = self.shoot_choice(alive_players, shotgun, current_turn, bonus_turn)
                        """
                        amon: ngl I dont know what bonus turn means
                        is it like when you shoot yourself, and it's blank, you
                        are the next turn again?
                        """

                        if bonus_turn:
                            print("extra turn")
                            bonus_turn = False
                        else:
                            break
                except Exception:
                   print("Invalid input, please try again")

            self.check_alive_players(alive_players)
            if self.check_game_over(alive_players):
                break

            current_turn, turn_count = self.next_turn(current_turn, alive_players, turn_count)

            #next round

            
    def next_turn(self, current_turn, alive_players, turn_count):
        
        turn_count += 1  
        if turn_count > len(alive_players)-1:
            turn_count = 0
            """
            amon: I think you can do something like
            if turn_count % len(alive_players) == 0
            basically like if you divide the turn count by
            how many alive players there are, and it's not 0
            that means that it hasn't cycled fully
            example:
            3 people, turn 0
            0%3 = 0, weird case, would mean 'recycle', but don't need to
            turn 1
            1%3 = 1, since 3 doesn't go in, remainder 1
            2%3 = 2
            3%3 = 0

            might be too much bs?

            but I think this is the main way to deal with these sort of things
            use modulo

            could be nice to learn that and try to implement it here
            """
            

        self.current_turn.isturn = False
        self.current_turn = alive_players[turn_count]
        self.current_turn.isturn = True
        current_turn = self.current_turn
         
        return(current_turn, turn_count)

            
    def shoot_choice(self, alive_players, shotgun, current_turn, bonus_turn):
        """
        amon: might need a 'try:' 'except:' thing here incase a wrong input
        was done, otherwise I wouldn't really change anything here
        """

        shoot_choice_name = input(f'You are {current_turn.name}, Please select a player to shoot\n')
        
        for player in alive_players:
            if shoot_choice_name == player.name:
                shoot_choice = player
                break
        
        if shoot_choice.name == current_turn.name:
            print('You shot yourself')
            bonus_turn = Shotgun.shoot(shotgun, current_turn, shoot_choice, bonus_turn, self)
            """
            amon: I'm so confused on what the fuck is going on here
            cause the shotgun.shoot method has: user, target, bonus turn, players (???), damage as inputs
            how the hell does this work with 'shotgun' being passed into it?

            ---

            wait, I see something weird.
            there's Shotgun.shoot(...). So we literally are calling the entire shotgun class
            we are not calling the actual shotgun we already have in the game.
            like we create a temp class in memory to use Shotgun.shoot() basically.
            we should be doing shotgun.shoot() not Shotgun.shoot(), because lowercase is the
            shotgun we already have
            Shotgun is the class.

            Also why I say ??? to players being passed to shotgun. I feel like that's complicated as
            hell. Why does the shotgun need to know who the players are. It just needs
            to know the person using and person shot.
            I think we can bring the bonus turn stuff outwards somehow.

            ---

            I now see how the bonus turn thing works.
            I think we just need to figure out how to do this with the
            proper like - ownership of variables and things.

            Like right now you pass in bonus turn, then it modifies bonus turn
            instead of passing a result back.

            I think we might have to say def shoot(...) -> bool: or -> ShotResult: 
            where ShotResult is a side class or maybe we have a new thing in Constants
            That way we can just have it return something.
            So we shotgun.shoot(...). Then we don't need to pass in a bonus_turn variable.
            We can then just expect that shotgun.shoot(...) returns a ShotResult class.
            Inside we can do like ShotResult.bonus_turn is true or false and 
            ShotResult.damage_dealt = 1, etc.

            I don't think I can do all this before I sleep today, idk I'll try.
            Hopefully I can access github in China, and do some work there, otherwise
            I'm screwed. It's kind of tight down there for western companies access.
            """
                    
        else:
            for player in range(len(alive_players)):
                if alive_players[player].name == shoot_choice.name and alive_players[player].name != current_turn.name:    
                    print(f"{current_turn.name} shot {alive_players[player].name}")
                    bonus_turn = Shotgun.shoot(shotgun, current_turn, shoot_choice, bonus_turn, self)
                    break
    
        return bonus_turn

    def check_alive_players(self, alive_players):
        for player in range(len(alive_players)):
            if alive_players[player].alive == False:   
                alive_players.remove(alive_players[player])
                break

        """
        amon: kinda cool system
        I was thinking this could be better optimized
        but then I realize
        this needs to be simple and readable
        we're not trying to score 100% on a cs course and
        optimize for fastest time

        this is good
        """


    def check_game_over(self, alive_players):
        if len(alive_players) == 1:
            print(f"{alive_players[0].name} has won the game!")
            alive_players[0].wins =+ 1

            print("Next round")
            return True
        return(False)

        
   
    def use_item(self, current_turn):
        print(f"Please select an item: {current_turn.inventory} or select a player to' shoot")
        """
        amon: I think this is called "abstract implementation"
        or something like that

        you just assume the thing works

        then let someone else implement it.

        this is gonna be fucked to implement. the itembox stuff
        amon: I think this is called "abstract implementation"
        """
        