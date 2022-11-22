from game import event
import random
from game.combat import Combat
from game.combat import Skeleton
from game.display import announce

class Skeleton (event.Event):

    def __init__ (self):
        self.name = " skeletons swarm you"

    def process (self, world):
        result = {}
        result["message"] = "the skeletons have been reduced to nothing but bone...or something like that"
        monsters = []
        if random.randrange(2) == 0:
            monsters.append(Skeleton("Armored Skeleton"))
            monsters[0].speed = 0.5*monsters[0].speed
            monsters[0].health = 5*monsters[0].health
        n_appearing = random.randrange(1,5)
        n = 1
        while n <= n_appearing:
            monsters.append(Drowned("Skeleton "+str(n)))
            n += 1
        announce ("The ship is attacked by a crew of drowned pirates!")
        Combat(monsters).combat()
        result["newevents"] = [ self ]
        return result
