from dice import roll

class Player():
    def __init__(self):
        self.strength=roll(3,6)
        self.constitution=roll(3,6)
        self.dexterity=roll(3,6)
        self.intelligence=roll(3,6)
        self.wisdom=roll(3,6)
        self.charisma=roll(3,6)
    def show_stats(self):
        text='''
        Strength: {s.strength}
        Constitution: {s.constitution}
        Intelligence: {s.intelligence}
        Wisdom: {s.wisdom}
        Charisma: {s.charisma}
        Dexterity: {s.dexterity}
        '''
        print(text.format(s=self))
if __name__=='__main__':
    p1=Player()
    print(p1.strength)
    p2=Player()
    print(p2.strength)


