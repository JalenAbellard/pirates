
from game import location
from game import config
from game.display import announce
from game.events import *

class Island (location.Location):

    def __init__ (self, x, y, w):
        super().__init__(x, y, w)
        self.name = "island with temple"
        self.symbol = 'IT'
        self.visitable = True
        self.starting_location = Beach_with_ship(self)
        self.locations = {}
        self.locations["beach"] = self.starting_location
        self.locations["trees"] = Trees(self)

    def enter (self, ship):
        print ("arrived at an island")

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
        self.event_chance = 50
        self.events.append (seagull.Seagull())
        self.events.append(drowned_pirates.DrownedPirates())

    def enter (self):
        announce ("arrive at the beach. Your ship is at anchor in a small bay to the south.")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            announce ("You return to your ship.")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False
        elif (verb == "east" or "west"):
            config.the_player.next_loc = self.main_location.locations["trees"]
        elif (verb == "north"):
            print ("You've come upon a mysterious temple, maybe there's something intersting inside")
            config.the_player.next_loc = self.main_location.locations["temple"]


class Trees (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "temple"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        self.event_chance = 50
        self.events.append(man_eating_monkeys.ManEatingMonkeys())
        self.events.append(drowned_pirates.DrownedPirates())

    def enter (self):
        announce ("You walk into the small forest on the island. Nothing around here looks very edible.")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south" or verb == "north" or verb == "east" or verb == "west"):
            config.the_player.next_loc = self.main_location.locations["beach"]

class Temple (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "trees"
        self.verbs['left'] = self
        self.verbs['right'] = self
        self.verbs['forward'] = self
        self.verbs['backward'] = self
        self.event_chance = 50
        self.events.append(Undead_Guard.UndeadGuard())
        self.events.append(drowned_pirates.DrownedPirates())

    def enter (self):
        announce ("You push through two large doors, a immediate sense of unease washes over you, this is no ordinary temple...you can either push forward or retreat")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "backward"):
            config.the_player.next_loc = self.main_location.locations["beach"]

        elif (verb == "left" or ver == "right"):
            announce ("You ran into a wall...nice")

        elif (verb == "forwards"):
            config.the_player.next_loc = self.main_location.locations["Room_1"]

class Room_1 (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Room 1"
        self.verbs['left'] = self
        self.verbs['right'] = self
        self.verbs['forward'] = self
        self.verbs['backward'] = self
        self.event_chance = 50
        #self.events.append(man_eating_monkeys.ManEatingMonkeys())
        #self.events.append(drowned_pirates.DrownedPirates())

    def enter (self):
        announce ("You push through two large doors, a immediate sense of unease washes over you, this is no ordinary temple...you can either push forward or retreat")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "backward"):
            config.the_player.next_loc = self.main_location.locations["beach"]

        elif (verb == "left" or verb == "right"):
            announce ("You ran into a wall...nice")

        elif (verb == "forwards"):
            config.the_player.next_loc = self.main_location.locations["room_W"]

class Room_2 (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Room 1"
        self.verbs['left'] = self
        self.verbs['right'] = self
        self.verbs['forward'] = self
        self.verbs['backward'] = self
        self.event_chance = 50
        #self.events.append(man_eating_monkeys.ManEatingMonkeys())
        #self.events.append(drowned_pirates.DrownedPirates())

    def enter (self):
        announce (" ")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "backward"):
            config.the_player.next_loc = self.main_location.locations["beach"]

        elif (verb == "left" or verb == "right"):
            announce ("You ran into a wall...nice")

        elif (verb == "forwards"):
            config.the_player.next_loc = self.main_location.locations["room_W"]




