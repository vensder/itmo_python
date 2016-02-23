
ls = [x * 2 for x in range(10)] # list gen

dct = {"User {}".format(x):x * 2 for x in range(10)} # dict gen

st = {x * 3 for x  in range(10)} # set generator


print(lst,dct,st)

from datetime import datetime

start = datetime.now()

gen = (x * 2 for x in range(100000)) # gen expressoin № выражение генератор

print('after createi:', datetime.now())

print(gen)

for i, a in enumerate(gen):
    # вычисление значения а
    if i > 100000 - 10:
        print(a)

print(datetime.now() - start)
