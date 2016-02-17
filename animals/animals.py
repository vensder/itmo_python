#!/usr/bin/env python3
# -*- coding: utf-8 -*-


a = 'кот'
data = {a: {}}

s = set()
s.update(['ловит мышей'])
data.update(кот = s)
s.update(['живет дома'])
data.update(кот = s)


#data.update(кит = {})
a = 'плавает в океане'
data.update(кит = {a})
print(data)
quit()

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

