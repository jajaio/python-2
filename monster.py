from dice import roll
from interfaces import HasStats
import random

class Zombie(HasStats):
    title="Zombie"
    def __init__(self):
        self.set_stats()
        self.strength += 10
    def action_attack():
        pass

class Ninja(HasStats):
    title="Ninja"
    def __init__(self):
        self.set_stats()
        self.dexterity += 10
monsters=[
    Ninja,
    Zombie
]

def pick_random():
    Monster=random.choice(monsters)
    return Monster()
if __name__ == "__main__":
    zomzom=Zombie()
    print(zomzom.title)
    zomzom.show_stats()
    
    randmon=pick_random()
    
