import random as r

def roll(number,sides):
    total=0
    for count in range(number):
        print(number)
        total += rolldie(sides)     
    return total


def rolldie(sides=6):
    return r.randint(1,sides)

if __name__=='__main__':
    foo=rolldie(6)
    print(foo)
    strength=roll(3,6)
    print(strength)
