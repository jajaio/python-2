import random as r

def roll(howmany=1,sides=6):
    total=0
    for count in range(howmany):
        print(howmany)
        total += rolldie(sides)     
    return total


def rolldie(sides=6):#Makes sides defaultly set to 6
    return r.randint(1,sides)

if __name__=='__main__':
    import colors as c
    foo=rolldie(6)
    for count in range(20):
        print(c.red+str(foo),end=' ')

