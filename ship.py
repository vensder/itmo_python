''' -> x coord ->
--------xx  y
-----       |
----xxxx--  v
----------
---x----xx
---x------
---x------
----------
xxx-------
----------
1234567890

[0,0,0,0,0,0,0,0,0,0]
'''

from random import randint

# generating area 10 x 10
area = [[0 for i in range(10)] for i in range(10)]

# Count quantity of random generation x,y
iterations = 0

# Print battle fild
def print_area(area):
    for r in area:
        print(r)

#cells<N> = N
#ship<N>v = [1 for i in range(cells<N>)]

# Generate x,y coord for ship with decks = decks_number
def generate_xy(decks_number):
    x = randint(0,(9-(decks_number-1)))
    y = randint(0,9)
    # Count quantity of random generation x,y
    global iterations
    iterations += 1
    return(x,y)
    
# insert ship in x,y, if there is 0
def insert_horizontal(decks_number):
    x,y = generate_xy(decks_number)
    # Regenerate x,y while we would not find the free area for ship
    while sum(area[y][x:x+decks_number]) != 0:
        x,y = generate_xy(decks_number)
    
    # Insert row with '2' above ship, if it is not first row
    if y > 0:
        area[y-1][x:x+decks_number] = [2 for i in range(decks_number)]
        # Insert '2' in left and right side above ship
        if x > 0:
            area[y-1][x-1] = 2
        if x < 9 - (decks_number-1):
            area[y-1][x+decks_number] = 2
    
    # Insert ship with '1'
    area[y][x:x+decks_number] = [1 for i in range(decks_number)]
    
    # Insert '2' with left and right side of the ship
    if x > 0:
        area[y][x-1] = 2
    if x < 9 - (decks_number-1):
        area[y][x+decks_number] = 2
    
    # Insert row with '2' below ship, if it is not last row
    if y < 9:
        area[y+1][x:x+decks_number] = [2 for i in range(decks_number)]
        # Insert '2' in left and right side below ship
        if x > 0:
            area[y+1][x-1] = 2
        if x < 9 - (decks_number-1):
            area[y+1][x+decks_number] = 2
                
    
# insert ship4v
insert_horizontal(4)

insert_horizontal(3)
insert_horizontal(3)

insert_horizontal(2)
insert_horizontal(2)
insert_horizontal(2)

insert_horizontal(1)
insert_horizontal(1)
insert_horizontal(1)
insert_horizontal(1)

print_area(area)

print('\n--------------------\n')

print('Iterations: ', iterations)

print('\n--------------------\n')

# print area with ships without '2'
area2 = [[0 for i in range(10)] for i in range(10)]
for i in range(10):
    for j in range(10):
        if area[i][j] == 1:
            area2[i][j] = 1
print_area(area2)
print('\n--------------------\n')

# Matrix transpons (area2 -> area3)
area3 = [[0 for i in range(10)] for i in range(10)]
for i in range(10):
    for j in range(10):
        area3[i][j] = area2[j][i]
print_area(area3)

# pseudo ascii
area4 = [['-' for i in range(10)] for i in range(10)]
for i in range(10):
    for j in range(10):
        if area[i][j] == 1:
            area4[i][j] = 'x'
print_area(area4)

print('\n--------------------\n')

# print pseudo ascii battle fild with ships
for ll in area4:
    print(' '.join(ll))
    
