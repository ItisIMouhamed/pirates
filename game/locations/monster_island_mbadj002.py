from game import location
from game import event
import game.config as config
from game.display import announce
from game.events import *
import game.items as items
import game.events.guessing_puzzle_mbadj002 as guessing_puzzle_mbadj002

class MonsterIsland (location.Location):

    def __init__(self, x, y, w):
        super().__init__(x, y, w)
        self.name = "monster_island"
        self.symbol = 'I'
        self.visitable = True
        self.starting_location = Beach_with_ship(self)
        self.locations = {}
        self.locations["beach"] = self.starting_location
        self.locations["jungle"] = Jungle(self)
        self.locations["lake"] = Lake(self)
        self.locations["cave"] = Cave(self)

    def enter(self,ship):
        print("You have arrived at an odd looking island. \n" +
              "The air is humid and there seems to be a constant thunder cloud looming over you.")

    def visit (self):
        config.the_player.location = self.starting_location
        config.the_player.location.enter()
        super().visit()

class Beach_with_ship (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "beach"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self

    def enter (self):
        announce ("arrive at the beach. Your ship is at anchor in a small bay to the south")

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            announce ("You return to your ship.")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False
        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["jungle"]
        elif (verb == "east"):
            config.the_player.next_loc = self.main_location.locations["lake"]
        elif (verb == "west"):
            config.the_player.next_loc = self.main_location.locations["cave"]
            

class Jungle (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "jungle"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        
        # Have a couple of items and the ability to pick them up
        self.verbs['take'] = self
        self.item_in_jungle = items.Stick()
        self.item_in_clothes = items.Knife()
        self.event_chance = 100
        self.events.append (guessing_puzzle_mbadj002.Sphinx())

    def enter (self):
        description = ("You arrived in the jungle.\n" +
                  "The trees are as tall as skyscrappers. \n" +
                  "Mosquitos the size of oragnges constantly buzz around you.")
        announce(description)

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "east"):
            config.the_player.next_loc = self.main_location.Locations["lake"]
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.Locations["beach"]
        if (verb == "west"):
            config.the_player.next_loc = self.main_location.locations["cave"]

class Lake (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "lake"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self

        self.verbs['take'] = self
        self.item_in_lake = items.Shinyrock()
        self.item_in_lake = items.Waterbottle()

    def enter (self):
        description = ("You have arrived at a lake. \n" +
                  "It seems very peaceful, perhaps you can rest here.")
        announce(description)

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "north"):
            config.the_player.next_loc = self.main_location.Locations["jungle"]
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.Locations["beach"]
        if (verb == "west"):
            config.the_player.next_loc = self.main_location.locations["cave"]

class Cave (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "lake"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self

        self.verbs['take'] = self
        self.items_in_cave = items.torch()

    def enter (self):
        description = ("You have arrived at a huge cave. \n" +
                  "It is very dark and cold. \n" +
                  "It seems no one has been here for a while.")
        announce(description)

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "north"):
            config.the_player.next_loc = self.main_location.Locations["jungle"]
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.Locations["beach"]
        if (verb == "east"):
            config.the_player.next_loc = self.main_location.Locations["lake"]
        


