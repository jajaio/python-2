from dice import roll

class Monster():
    def __init__(self):
        self.dmg=roll(3,6)
        self.hp=roll(6,10)
        self.agi=roll(1,10)

    def show(self):
        text='''
        DMG: {s.dmg}
        HP:  {s.hp}
        AGI: {s.agi}
        '''
        print(text.format(s=self))

if __name__=='__main__':
    m=Monster()
    m.show()

