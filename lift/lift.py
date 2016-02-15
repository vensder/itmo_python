#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# student: Dmitry Makarov

#import os # import of os module

# checking for current version of Python
#import platform
from platform import python_version
print('Current version of Python is: ' + python_version() + '\n')

# files small.lift and larghe.lift store floor number, where are lifts
# if files doesn't exist, they will be create with default number of floor = 1
for i in('small','large'):
    try:
        f = open(i + '.lift')
    except FileNotFoundError:
        f = open(i + '.lift','w')
        f.write('1')
        f.close()

# on which flor are lifts
small_lift = 1
large_lift = 1

start_flour = input('On which flour are you placed?\n')

print(start_flour)


