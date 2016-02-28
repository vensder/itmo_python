'''
--------xx
-----
----xxxx--
----------
---x----xx
---x------
---x------
----------
xxx-------
----------
1234567890
abcdefghij


[0,0,0,0,0,0,0,0,0,0]
'''

from random import randint
# generating area 10 x 10
area = [[0 for i in range(10)] for i in range(10)]

def print_area():
    for r in area:
        print(r)

cells4 = 4
cells3 = 3
cells2 = 2
cells1 = 1

ship4v = [1 for i in range(cells4)]
ship3v = [1 for i in range(cells3)]
ship2v = [1 for i in range(cells2)]
ship1v = [1 for i in range(cells1)]

def insert_horizontal(decks_number):
    x = randint(0,(9-(decks_number-1)))
    y = randint(0,9)
    if y > 0:
        area[y-1][x:x+decks_number] = [2 for i in range(decks_number)]
    area[y][x:x+decks_number] = [1 for i in range(decks_number)]
    if y < 9:
        area[y+1][x:x+decks_number] = [2 for i in range(decks_number)]
    print(ship4v)
    print(x)
    print(y)

    
# insert ship4v
insert_horizontal(4)
#insert_horizontal(3)
#y = randint(0,9)
#x = randint(0,(9-(cells4-1)))
#area[y][x:x+cells4] = ship4v

print_area()
