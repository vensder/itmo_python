
import random

lst = [1,2,3]

e = 0
for j in range(1000000):
    j += 1
    i = random.randint(0,200)

    try:
       l = lst[i]
    except IndexError:
        e += 1
print(j)
print(e)
