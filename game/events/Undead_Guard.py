from game import event
import random
from game.combat import Combat
from game.combat import Guard
from game.display import announce

class UndeadGuard (event.Event):

    def __init__ (self):
        self.name = " undead guards attack"

    def process (self, world):
        result = {}
        result["message"] = "You have defeated the undead guards!"
        monsters = []
        if random.randrange(2) == 0:
            monsters.append(Guard("Undead Guard Captain"))
            monsters[0].speed = 1.5*monsters[0].speed
            monsters[0].health = 2*monsters[0].health
        n_appearing = random.randrange(1,5)
        n = 1
        while n <= n_appearing:
            monsters.append(Guard("Undead Guard "+str(n)))
            n += 1
        announce ("This guard seems different from the rest, but he's still attacking you")
        Combat(monsters).combat()
        if random.randrange(2) == 0:
            result["newevents"] = [ self ]
        else:
            result["newevents"] = [ ]
        
        return result
