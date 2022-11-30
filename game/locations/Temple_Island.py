
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
            announce("You've come upon a mysterious temple, maybe there's something intersting inside")
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
        announce ("You push through two large doors, a immediate sense of unease washes over you, this is no ordinary temple...")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "backward"):
            config.the_player.next_loc = self.main_location.locations["beach"]

        elif (verb == "left" or verb == "right"):
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
        announce ("This room has a long dark tunnel, ")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "backward"):
            config.the_player.next_loc = self.main_location.locations["beach"]

        elif (verb == "left" or verb == "right"):
            i += 1
            announce ("You found a chest and opened it...it had some health potions in it, nice!")
            i = 0
            while i <= 2:
                config.the_player.add_to_inventory([HealthPotion() * 10])
                

        elif (verb == "forwards"):
            config.the_player.next_loc = self.main_location.locations["room_2"]

class Room_2 (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Room 2"
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
            config.the_player.next_loc = self.main_location.locations["room_2"]

class Room_3 (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Room 3"
        self.verbs['left'] = self
        self.verbs['right'] = self
        self.verbs['forward'] = self
        self.verbs['left door'] = self
        self.verbs['right door'] = self
        self.verbs['middle door'] = self
        self.verbs['backward'] = self

    def enter (self):
        announce ("3 Doors appear in front of you with a lone sign in the middle, it appears to be a riddle")
        announce ("The Riddle reads 'I am something people celebrate or resist. I change people’s thoughts and lives. I am obvious to some people but, to others, I am a mystery. What am I?")
        announce ("The left door says 'Wisdom', the middle door says 'Age', and the right door says 'Love'")
        announce ("Which door should you go through? left, middle, or right?")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "backward"):
            config.the_player.next_loc = self.main_location.locations["room_2"]

        elif (verb == "left" or verb == "right"):
            announce ("You ran into a wall...did you not see it?")

        elif (verb == "left door" or verb == "right door"):
            announce ("You walk through the door and you end up...in the first room?")
            config.the_player.next_loc = self.main_location.locations["room_1"]

         elif (verb == "forwards"):
            announce("You have to pick a door first...you know that right?")

        elif (verb == "middle door"):
            config.the_player.next_loc = self.main_location.locations["room_4"]

class Room_4 (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Room 3"
        self.verbs['left'] = self
        self.verbs['right'] = self
        self.verbs['forward'] = self
        self.verbs['left door'] = self
        self.verbs['right door'] = self
        self.verbs['middle door'] = self
        self.verbs['backward'] = self

    def enter (self):
        i += 1
        announce ("You found a chest and opened it...it had some health potions in it, nice!")
        i = 0
        while i <= 1:
            config.the_player.add_to_inventory([HealthPotion() * 10])
        announce ("3 Doors appear in front of you... again...with a lone sign in the middle, this time a simple question 'What is it you seek?' ")
        announce ("The left door says 'The power to defeat eveil', the middle door says 'Wealth and Riches', and the right door says 'Love'")
        announce ("Which door should you go through? left, middle, or right?")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "backward"):
            announce ("The door won't budge, guess you have to pick a door")

        elif (verb == "left" or verb == "right"):
            announce ("You ran into a wall...did you not see the it?")

         elif (verb == "forwards"):
            announce("You have to pick a door first...you know that right?")

        elif (verb == "left door"):
            config.the_player.next_loc = self.main_location.locations["room_5"]

        elif (verb == "middle door" or verb == "right door"):
            config.the_player.next_loc = self.main_location.locations["room_1"]
            announce ("Then you have come to the wrong place")

class Room_5 (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Room 3"
        self.verbs['left'] = self
        self.verbs['right'] = self
        self.verbs['forward'] = self
        self.verbs['left door'] = self
        self.verbs['right door'] = self
        self.verbs['middle door'] = self
        self.verbs['backward'] = self

    def enter (self):
        
        announce ("The room is pitch black and you can't see the other side, the door open door behind is your only source of light, push forward or pull back?")
        
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "backward"):
            config.the_player.next_loc = self.main_location.locations["room_1"]
            announce ("You enter the open door behind you and you end up in...the first room?")
            announce ("You swear you can hear an ominoucs voice echo throughout the building whispering 'Come back when you have more courage' ") 

        elif (verb == "forward"):
            announce ("You sure? It's really dark in there...")
            if (verb == "forward"):
                announce ("Are you sure you're sure? There could be monsters in their...")
                if (verb == "forward"):
                    config.the_player.next_loc = self.main_location.locations["room_6"]
                elif (verb == "backwards"):
                    config.the_player.next_loc = self.main_location.locations["room_1"]
                    announce ("You enter the door behind you and you end up in...the first room?")
                    announce ("You swear you can hear an ominoucs voice echo throughout the building whispering 'Come back when you have more courage' ")
            elif  (verb == "backwards"):
                    config.the_player.next_loc = self.main_location.locations["room_1"]
                    announce ("You enter the door behind you and you end up in...the first room?")
                    announce ("You swear you can hear an ominoucs voice echo throughout the building whispering 'Come back when you have more courage' ")

        elif (verb == "left" or verb == "right"):
           announce ("You ran into a wall...you couldn't see it but...really?")

       




