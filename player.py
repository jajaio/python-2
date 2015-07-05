from dice import roll
from interfaces import HasStats
import colors as c
class Player(HasStats):
    def __init__(self):
        self.set_stats()


if __name__=='__main__':
    p1=Player()
    print(c.clear)
    p1.save()
    p1.load()
    p1.show_stats()


