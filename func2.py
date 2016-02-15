

def summ(l):
    summa = 0
    for a in lst:
        summa += a
    return summa

lst = {2:'2',4:'4',6:'6',7:'7'}

print(summ(lst))

def write_to_file(): # func without return
    f = open('rrr', 'a')
    f.write('+1\n')
    f.close()

write_to_file()
write_to_file()

def write_to_file(text): # func without return
    f = open('rrr', 'a')
    s = "{}\n".format(text)
    f.write(s)
    f.close()

write_to_file("adfasdf")

def func(a,b,c = 2): # c - необязательный аргумент
    return a + b + c

print(func(10,20,30))


def func(*args):
    return args

print(type(func(1,2,4)))
print(func(1,2,4))

def debug(*args):
    
    for a in args:
        print(a)

    return args

debug()
(debug(1,2,3))

def func(**kwargs):
    print('name',kwargs['name'])
    print('age', kwargs['age'])
    return kwargs

print(func(name = 'Ivan', age = 19))



