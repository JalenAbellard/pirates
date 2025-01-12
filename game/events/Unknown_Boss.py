from game import event
import random
from game.combat import Combat
from game.combat import Unknown
from game.display import announce
import game.config as config



class UnknownBoss(event.Event):

    def __init__ (self):
        self.name = "a monster of immense proportions appears in front of you"

    def process (self, world):
        result = {}
        result["message"] = "the bigger they are..the harder they fall"
        monsters = []
        n_appearing = 1
        n = 1
        while n <= n_appearing:
            monsters.append(Unknown("Unknown Monster "+str(n)))
            n += 1
        announce ("You are under attack by a behemoth, is resistance futile?")
        Combat(monsters).combat()
        
        return result
