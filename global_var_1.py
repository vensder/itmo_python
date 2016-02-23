
x = 0

def some_func(lst=[]):

    global x
    x += 1

    lst.append(x)

    print(id(lst), lst)

some_func()
some_func()
some_func([3, 4])
some_func()
