from dice import roll
import colors as c
class HasStats():
    health=100

    def set_stats(self):
        self.strength=roll(3,6)
        self.constitution=roll(3,6)
        self.dexterity=roll(3,6)
        self.intelligence=roll(3,6)
        self.wisdom=roll(3,6)
        self.charisma=roll(3,6)


    def show_stats(self):
        text='''
        Strength: {s.strength>2}
        Constitution: {s.constitution>2}
        Intelligence: {s.intelligence>2}
        Wisdom: {s.wisdom>2}
        Charisma: {s.charisma>2}
        Dexterity: {s.dexterity>2}
        '''
        print(text.format(s=self))


class Player(HasStats):
    def __init__(self):
        self.set_stats()
        self.show_stats()

if __name__=='__main__':
    p1=Player()
    print(c.clear)
    p1.show_stats()


