#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#1.5
students = [
        'Ivanov Ivan',
        'Ivanov Stanislav',
        'Petrov Ivan',
        'Ivanov Petr',
        'Petrov Petr',
        'Sidorov Petr',
        'Sidorov Ivan',]

# Split each element of list to list whith Surname, Name
for i in range(len(students)):
    students[i] = students[i].split(' ')

for i in range(len(students)):
    f = open('group_' + students[i][1],'w')
    f.close()

for i in range(len(students)):
    f = open('group_' + students[i][1],'a')
    for j in range(len(students)):
        if students[i][1] == students[j][1]:
            f.write(students[j][0] + '\n')

#3for i in range(len(students)):

list0 = [students[0]]
for i in range(1,len(students)):
    print(students[i])
    if students[0][1] == students[i][1]:
        list0.append(students[i])
#        print(students[i+1])
print(list0)

print(students)

