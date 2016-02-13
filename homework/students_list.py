#!/usr/bin/env python3
# -*- coding: utf-8 -*-

language = input('Choise the language: type "en" for English or type "ru" for Russian:\n')

#1
students = [
        'Ivanov Ivan',
        'Ivanov Stanislav',
        'Petrov Ivan',
        'Ivanov Petr',
        'Petrov Petr',
        'Sidorov Petr',
        'Sidorov Ivan',]

if language == 'ru':
    students = [
            'Иванов Иван',
            'Иванов Станислав',
            'Петров Иван',
            'Иванов Петр',
            'Петров Петр',
            'Сидоров Петр',
            'Сидоров Иван',
            ]

quantity = len(students)

if language == 'ru':
    print('Список студентов:')
else:
    print('Students list:')
for i in range(quantity):
    print(str(i+1)+'.',students[i])

#2
if language == 'ru':
    print(
'''Введите порядковый номер студента.
Номер должен быть от 1 до''', quantity)
else:
    print('''
Input the student number, please
The number should be from 1 to''', quantity)
index = int(input()) - 1

if not (0 <= index < quantity):
    if language == 'ru':
        print('Порядковый номер за пределами диапазона, извините...')
    else:
         print('Index out of range, sorry...')
    quit()

if language == 'ru':
    print('Вы ввели номер:', index+1)
    print('Студент под номером ' + str(index+1) + ':', students[index])
else:
    print('Your number is:', index+1)
    print('Student with number', index+1, 'is', students[index])

#3
print('Input range of students numbers in format "x-y", where x is begin, y is end of range:')
students_range = input().split('-')
begin = int(students_range[0])
end = int(students_range[1])
print(students[begin-1:end])

#4
i=0
if language == 'ru':
    for s in students:
        if s.find('р') != -1:
            i+=1
else:
    for s in students:
        if s.find('r') != -1:
            i+=1

if language == 'ru':
    print('Количество студентов с буквой "р":', i)
else:
    print('Quantity of students with letter "r" is:', i)

#5
# Split each element of list to list whith Surname, Name
for i in range(len(students)):
    students[i] = students[i].split(' ')

list0 = [students[0]]
for i in range(1,len(students)):
    print(students[i])
    if students[0][1] == students[i][1]:
        list0.append(students[i])
#        print(students[i+1])
print(list0)


print(students)

