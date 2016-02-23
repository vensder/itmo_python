

def gen():
    for i in range(10):
        X = yield i
        print(X, 'from G')

G = gen()

next(G) # чтобы запустить ген - обязательное действие
#G.send('Hello') #Переход к след знач

k = G.send('Hello')
print('in prog', k)
