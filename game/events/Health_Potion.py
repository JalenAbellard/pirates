from game import event
import random
import game.config as config
from ship import

class HealthPotion(event.Event):

    def __init__(self):
        self.name  = " you pop open a healing potion "

    def process (self, ship):
        
