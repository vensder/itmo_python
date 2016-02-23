

#yield

def gensquares(N):
    last_i = 0
    yield -300 # 1 сохраняет состояние

    for i in range(N):
        if i % 2 == 0:
            last_i += 2

        if i < 2:
            yield -i
        else:
            yield i ** 2, last_i
    yield 300

gen = gensquares(5)

#x = next(gen)
#x = next(gen)

for a in gen:
    print(a)
