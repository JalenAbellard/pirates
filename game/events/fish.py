from game import event
import random
import game.config as config
from ship import 

class Fish(event.Event):

    def __init__ (self):
        self.name = " you attempted to catch some fish "

    def process (self, ship, food):
        x = random.randint(1,20)
        result = {}
        if x <= 5:
            print ("No luck today, hope we still have some food left...")
        elif 5 < x < 15:
            ship.food += 20
            print ("Not bad, at least we wont starve today")
        elif 15 <= x <= 19:
            ship.food += 50
            print ("A lot of fish today, should hold us over for a few days")
        elif x == 20:
            ship.food += 100
            print ("You caught a whale...with a fishing rod...maybe you should become a professinal")
        return result
            
        
