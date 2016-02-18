#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 'кот'
data = {a: {}}

s = set()
s.update(['ловит мышей'])
#data.update(кот = s)
data[a] = s
s.update(['живет дома'])
data[a] = s
print(data)

a = 'кит'
s = set()
#data.update(кит = {})
s.update(['плавает в океане'])
#data.update(кит = {a})
data[a] = s
print(data)

import pickle
pickle.dump(data, open('data.p','wb'))
quit()

data2 = pickle.load(open("data.p","rb"))
print(data2)

def choice():
    choice = input('Да (Enter, 1, Y, y) / Нет (0, N, n)\n')
    choice = choice.lower()
    yes = ['', 'да', '', '1', 'y', 'yes']

    if choice in yes:
        choice = 'yes'
    else:
        choice = 'no'
    return choice

print('Загадешь животное?')
if choice() == 'yes':
    print('Это КОТ?')
else:
    print('Пока-пока!')
    quit()

if choice() == 'yes':
    print('Ура! Я угадал!')
else:
    print('Сдаюсь. Кто это?')
    animal = input()
    print('Чем '+ animal + ' отличается от КОТ?')

