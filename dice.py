import random as r

def roll(howmany=1,sides=6):
    total=0
    for count in range(howmany):
        print(howmany)
        total += rolldie(sides)#works off of rolldie funct.     
    return total

def rolldie(sides=6):#Makes sides defaultly set to 6
    return r.randint(1,sides)

def parse_roll(text):
    """Parses traditional dice notation (ex: 3d6)"""
    (howmany, sides) = parse(text)
    return roll(howmany, sides)

def parse(text):
    """Parses traditional dice notation (ex: 3d6)"""
    (howmany, sides) = text.split('d')
    return (int(howmany), int(sides))

if __name__=='__main__':
    import colors as c
    print(parse_roll('2d10'))
    exit()
    def testrolldie(sides):
        foo=rolldie(6)
        for count in range(20):
            print(c.red + str(foo), end=' ')

        print(c.clear)

        testrolldie(6)
        testrolldie(20)
        testrolldie(100)

        print(c.yellow +'' +c.reset)
        for count in range(20):
            foo=roll()
            print(c.random_color()+str(foo)+c.reset,end=' ')
        print()
        print()

        for text in ['2d6', '4d6', '1d20','2d100',]:
            print("parse({})".format(text))
            print(parse(text))
            print('parse_roll({})'.format(text))
            print(parse_roll(text))

