from game import event
import random
import game.config as config

 

class Fish(event.Event):

    def __init__ (self):
        self.name = " you attempted to catch some fish "

    def process (self, ship, food):
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
        return result
            
        
