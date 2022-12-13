
from game import location
from game import config
from game.display import announce
from game.events import *
#from game.items import Mysterious_Sword
#Couldn't figure out how to import this file but the item is ready


class Island (location.Location):

    def __init__ (self, x, y, w):
        super().__init__(x, y, w)
        self.name = "templeisland"
        self.symbol = 'TI'
        self.visitable = True
        self.starting_location = Beach_with_ship(self)
        self.locations = {}
        self.locations["beach"] = self.starting_location
        self.locations["trees"] = Trees(self)
        self.locations["temple"] = Temple(self)
        self.locations["Room 1"] = Room_1(self)
        self.locations["Room 2"] = Room_2(self)
        self.locations["Room 3"] = Room_3(self)
        self.locations["Room 4"] = Room_4(self)
        self.locations["Room 5"] = Room_5(self)
        self.locations["Room 6"] = Room_6(self)

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
        #self.events.append (seagull.Seagull())
        #self.events.append(drowned_pirates.DrownedPirates())

    def enter (self):
        announce ("arrive at the beach. Your ship is at anchor in a small bay to the south.")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            announce ("You return to your ship.")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False
        elif (verb == "east" or verb == "west"):
            config.the_player.next_loc = self.main_location.locations["trees"]
        elif (verb == "north"):
             config.the_player.next_loc = self.main_location.locations["temple"]
             announce("You've come upon a mysterious temple, maybe there's something intersting inside")
           


class Trees (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "trees"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        self.event_chance = 0
        self.events.append(man_eating_monkeys.ManEatingMonkeys())
        self.events.append(drowned_pirates.DrownedPirates())
        self.events.append(Undead_Guard.UndeadGuard())

    def enter (self):
        announce ("You walk into the small forest on the island. Nothing around here looks very edible.")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south" or verb == "north" or verb == "east" or verb == "west"):
            config.the_player.next_loc = self.main_location.locations["beach"]

class Temple (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "temple"
        self.verbs['left'] = self
        self.verbs['right'] = self
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.event_chance = 0
        self.events.append(Undead_Guard.UndeadGuard())
        self.events.append(drowned_pirates.DrownedPirates())

    def enter (self):
        announce ("You push through two large doors, a immediate sense of unease washes over you, this is no ordinary temple...")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.locations["beach"]

        elif (verb == "left" or verb == "right"):
            announce ("You ran into a wall...nice")

        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["Room 1"]

class Room_1 (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Room 1"
        self.verbs['left'] = self
        self.verbs['right'] = self
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.event_chance = 0
        self.events.append(Undead_Guard.UndeadGuard())
       

    def enter (self):
        announce ("This room has a long dark tunnel leading somewhere")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.locations["beach"]

        elif (verb == "left" or verb == "right"):
            i = 0
            i += 1
            if i <=2:
                announce ("You found a chest and opened it...it had some health potions in it, nice!")
                config.the_player.ship.healthpotion += 5
            else:
                announce ("You found some empty chest, guess you weren't the first person to find this place")
                
                
        #    announce ("You found some empty chest, guess you weren't the first person to find this place")
        #    i += 1
        #    announce ("You found a chest and opened it...it had some health potions in it, nice!")
        #    i = 0
        #    while i <= 2:
        #        config.the_player.ship.healthpotion += 5
                

        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["Room 2"]
class Room_2 (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Room 2"
        self.verbs['left'] = self
        self.verbs['right'] = self
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.event_chance = 50
        #self.events.append(man_eating_monkeys.ManEatingMonkeys())
        #self.events.append(drowned_pirates.DrownedPirates())

    def enter (self):
        announce (" ")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.locations["beach"]

        elif (verb == "left" or verb == "right"):
            announce ("You ran into a wall...nice")

        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["Room 3"]

class Room_3 (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Room 3"
        self.verbs['west'] = self
        self.verbs['east'] = self
        self.verbs['north'] = self
        self.verbs['south'] = self

    def enter (self):
        announce ("3 Doors appear in front of you with a lone sign in the middle, it appears to be a riddle")
        announce ("The Riddle reads 'I am something people celebrate or resist. I change people’s thoughts and lives. I am obvious to some people but, to others, I am a mystery. What am I?")
        announce ("The west door says 'Wisdom', the north door says 'Age', and the easgt door says 'Love'")
        announce ("Which door should you go through? west, north, or east?")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.locations["Room 2"]

        elif (verb == "west" or verb == "east"):
            announce ("You walk through the door and you end up...in the first room?")
            config.the_player.next_loc = self.main_location.locations["Room 1"]

        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["Room 4"]

class Room_4 (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Room 3"
        self.verbs['left'] = self
        self.verbs['right'] = self
        self.verbs['north'] = self
        self.verbs['south'] = self

    def enter (self):
        #i += 1
        #announce ("You found a chest and opened it...it had some health potions in it, nice!")
        #i = 0
        #while i <= 1:
        #    config.the_player.add_to_inventory([HealthPotion() * 10])
        announce ("3 Doors appear in front of you... again...with a lone sign in the middle, this time a simple question 'What is it you seek?' ")
        announce ("The west door says 'The power to defeat eveil', the north door says 'Wealth and Riches', and the east door says 'Love'")
        announce ("Which door should you go through? west, north, or east?")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            announce ("The door won't budge, guess you have to pick a door")

        elif (verb == "north"):
            announce("You have to pick a door first...you know that right?")

        elif (verb == "west"):
            config.the_player.next_loc = self.main_location.locations["Room 5"]

        elif (verb == "north" or verb == "east"):
            config.the_player.next_loc = self.main_location.locations["Room 1"]
            announce ("Then you have come to the wrong place")

class Room_5 (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Room 3"
        self.verbs['west'] = self
        self.verbs['east'] = self
        self.verbs['north'] = self
        self.verbs['south'] = self

    def enter (self):
        
        announce ("The room is pitch black and you can't see the other side, the door open door to your south is your only source of light, push north or pull back south?")
        
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.locations["Room 1"]
            announce ("You enter the open door behind you and you end up in...the first room?")
            announce ("You swear you can hear an ominoucs voice echo throughout the building whispering 'Come back when you have more courage' ") 

        elif (verb == "north"):
            announce ("You sure? It's really dark in there...")
            config.the_player.next_loc = self.main_location.locations["Room 6"]
                
        elif (verb == "west" or verb == "east"):
           announce ("You ran into a wall...you couldn't see it but...really?")


class Room_6 (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Room 6"
        self.verbs['west'] = self
        self.verbs['east'] = self
        self.verbs['north'] = self
        self.verbs['south'] = self
        #self.item = Mysterios_Sword
        self.event_chance = 100
        self.events.append(Unknown_Boss.UnknownBoss())

        
        
    def enter (self):
        #config.the_player.add_to_inventory([self.item])
        announce ("You come upon a large, open room, something feels off...")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.locations["Room 1"]
            announce ("You enter the open door behind you and you end up in...the first room?")

        elif (verb == "west" or verb == "east"):
            announce ("A wall")

        elif (verb == "north"):
            announce ("A wall")

       




