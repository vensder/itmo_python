

import sys, os

add = lambda x,y: x + y

print(add(10,20))

print((lambda x,y: x + y)(10, 20))


list1 = [
      ['Ivan', 'Novikov'],
      ['Maria', 'Kozhevnikova'],
      ['Will', 'Smith'],
      ]

#for i in len(lst):
#    print(lambda lst3: len(lst[i][0])/len(lst[i][1]))

koef = lambda lst: [ len(a[0]) / len(a[1]) for a in lst ]

print(koef(list1))

#lst.sort(key=lambda lst2: lst2[1])
#print(lst)

#def sort(key = lambda lst2: lst2[1]):
