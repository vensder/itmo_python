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

def insertv(cellsx):
	x = randint(0,9)
	y = randint(0,(9-(cellsx-1)))
	area[y][x:x+cellsx] = [1 for i in range(x)]

# insert ship4v
insertv(4)
#y = randint(0,9)
#x = randint(0,(9-(cells4-1)))
#area[y][x:x+cells4] = ship4v

print_area()
