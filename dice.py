import random as r
import colors as c
sides=[None]
sides.append('''
 -------
|       |
|   •   |
|       |
 -------
''')

sides.append('''
 -------
| •     |
|       |
|     • |
 -------
''')

sides.append('''
 -------
| •     |
|   •   |
|     • |
 -------
''')
sides.append('''
 -------
| •   • |
|       |
| •   • |
 -------
''')

sides.append('''
 -------
| •   • |
|   •   |
| •   • |
 -------
''')

sides.append('''
 -------
| •   • |
| •   • |
| •   • |
 -------
''')
how_many=1
print(c.clear)
while True:
    how=input('How many dice? ').strip().lower()
    if not how:
        how=last
    elif how=="bye":
        exit()
    else:
        how=int(how)
        last=how
    print(c.clear)
    for count in range(how):
        number=r.randint(1,6)
        print(c.blue+''+sides[number].strip()+c.reset)

if __name__='__main__':
    roll()
