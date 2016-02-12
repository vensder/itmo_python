# lists
# generator spiscov
c = [c*3 for c in 'list' if c !='i']

c = [c + d for c in 'list' if c != 'i' 
           for d in 'spam' if d != 'a']

c = list('list')

#i = c.index('i', start = 2, end = 4)
i = c.index('i',1,4)
print(i)
c.reverse()
p = c.copy()

print(c)

a = [1,2,3,4,5]

del a[2]

#kortezhi
a = ()
a = tuple()
a = (1,2,3,4,5)
b = [1,2,3,4,5]
c = list(a)
a = tuple(c)

print(a.__sizeof__())
print(b.__sizeof__())

#d = {b : 1}

a = ('s')
print(type(a))
a = ('s',)
print(type(a))

b = ('s', 7, ['sdfasdf',33], 44, 66)
print(b)

# Словари беспорядочные массив пар

d = {}
print(d)
d = {'dict': 1, 'dictionary': 2}
print(d)

d = dict(short='dict', long='dictionary')
d = dict.fromkeys(['a', 'b'])

range(7) #create list from 0 to 7
d = {a: a**2 for a in range(7)}
d[4] = 'asdfasdfasd'
print(d)
print(d[6])
d2 = {'1212': 'Hello',}
print(d.get(3)) # d[3]
print(d.get(200,None)) #possibility to assign default value

print(d.items())
print(len(d.keys()), len(d))
print(d.values())

d.update(d2)
print(d)
d.clear()
print(d)

print('========================')

#mnozhestva set - непоследовательный неотсортированный, повторяющиеся элементы не дублируются
# добавлять только хешируемые неизменяемые элементы
a = set()
a = {600,200, 'c', 'd',600,200,200,600, 'c'}
print(a)

a = a = {i**2 for i in range(10)}
a.add('4')
print(a)
print('4' in a)



