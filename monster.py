from dice import roll
from interfaces import HasStats

monsters=[
'Zombie'
'Ninja'
]

class Zombie(HasStats):
    def __init__(self):
        self.set_stats()
        self.strength += 10


class Ninja(HasStats):
    def __init__(self):
        self.set_stats()
        self.dexterity += 10

