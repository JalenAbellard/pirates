
import random
from game.crewmate import *
from game.location import *
from game.context import Context
from game.display import announce
import game.config as config
#from game.event import fish

class Ship (Context):
    '''The pirate ship. Mostly handles food and sailing around the ocean map.'''
    def __init__(self):
        super().__init__()
        self.hx = 0
        self.hy = 0
        self.medicine = 5
        self.healthpotion = 5
        self.food = 100
        self.loc = None

        self.verbs['anchor'] = self
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        self.verbs['give'] = self
        self.verbs['fish'] = self
        self.verbs['heal'] = self
        

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "north"):
            self.hx = 0
            self.hy = -1
        elif (verb == "south"):
            self.hx = 0
            self.hy = 1
        elif (verb == "east"):
            self.hx = 1
            self.hy = 0
        elif (verb == "west"):
            self.hx = -1
            self.hy = 0
        elif (verb == "anchor"):
            self.hx = 0
            self.hy = 0
        elif (verb  == 'fish'):
            x = random.randint(1,21)
            if x <= 5:
                announce ("No luck today, hope we still have some food left...")
            elif x > 5 and x < 15:
                config.the_player.ship.food += 20
                announce ("Not bad, at least we wont starve today")
            elif x >= 15 and x <= 19:
                config.the_player.ship.food += 50
                announce ("A lot of fish today, should hold us over for a few days")
            elif x == 20:
                config.the_player.ship.food += 100
                announce ("You caught a whale...with a fishing rod...maybe you should become a professinal fisher instead of a pirate")
        elif (verb == "give"):
            # give medicine to crewmember
            if (len(cmd_list) > 3):
                if ((cmd_list[1] == "medicine") and (cmd_list[3] in nouns.keys())):
                    if (self.medicine > 0):
                        nouns[cmd_list[3]].receive_medicine(1)
                        self.medicine =  self.medicine - 1
                    else:
                        announce ("no more medicine to give")
            else:
                announce ("Give medicine to who?")

        #elif (verb == "heal"):
            #if (len(cmd_list) > 2):
             #   if (cmd_list[0] == "heal") and (cmd_list[1] in nouns.keys()):
              #      if (self.healthpotion > 0):
               #         nouns[cmd_list[1]].health = self.health_max
                #        self.healthpotion = self.healthpotion - 1
                 #   else:
                  #      announce ("No health potions to give")
            #else:
              #  announce ("Heal who")

      #  else:
       #     announce ("Error: Ship object doe not understand verb " + verb)


    def print (self):
        print ("ship is at: " + str(self.loc.get_x()) + ", " + str(self.loc.get_y()))
        if ((self.hx==0) and (self.hy==0)):
            print ("ship anchored")
        elif ((self.hx == 1) and (self.hy == 0)):
            print ("ship heading is east")
        elif ((self.hx == -1) and (self.hy == 0)):
            print ("ship heading is west")
        elif ((self.hx == 0) and (self.hy == -1)):
            print ("ship heading is north")
        elif ((self.hx == 0) and (self.hy == 1)):
            print ("ship heading is south")

        print ("ship has " + str (self.medicine) + " medicine")
        print ("ship has " + str (self.healthpotion) + " medicine")

    def get_loc (self):
        return self.loc

    def set_loc (self, loc):
        self.loc = loc

    def start_day (self, world):
        # crew members eat, and possibly die of illnesses
        i = 0
        for crew in config.the_player.get_pirates():
            crew.start_day (self)

    def get_food (self):
        return self.food

    def take_food (self, amt):
        self.food = self.food - amt

    def enter (self):
        pass
        
    def end_day (self, world):

        if ((self.hx != 0) or (self.hy != 0)):
            # find the destination
            new_loc = world.get_loc (self.loc.get_x()+self.hx, self.loc.get_y()+self.hy)

            # change our location
            self.set_loc (new_loc)

            # tell the new location that we entered
            new_loc.enter(self)

        for crew in config.the_player.get_pirates():
            crew.end_day ()
