from dice import roll
from interfaces import HasStats
from utils import ask
import colors as c

class Player(HasStats):
    def __init__(self):
        self.set_stats()
    def pick_move(self):
        move=ask("What move do you want to make?")


if __name__=='__main__':
    player=Player()
    print(c.clear)
    player.save()
    #player.load()
    player.show_stats()
    player.pick_move()


