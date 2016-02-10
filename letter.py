#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = '''Python  is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax. For an introduction to programming in Python, see the Python Tutorial. The Python Library Reference documents built-in and standard  types,  constants,  functions  and  modules.  Finally, the Python Reference Manual describes the syntax and semantics of the core language in (perhaps too) much detail.  (These documents may be located via the INTERNET RESOURCES below; they may be installed on your system as well.)'''

print(len(s))
l = len(s)

for i in range(0,l,2):
    s1 = s[i:] + str(i) + s[:i]
    s = s1
print(s1)
print(s)

print(len(s))

ss = s.split(' ')

print('List: ')
print(ss)

print('Lenght of List: ')
print(len(ss))

sss = 0

print('Digits: ')
for i in range(0,len(ss)):
    if ss[i].isdigit():
        print(ss[i])
        sss = sss + int(ss[i])

print('Sum is: ' + str(sss))


u = ''
num = ''
summ = 0
for u in s:
    if u.isdigit():
        num = num + u
    elif num !='':
        summ = summ + int(num)
        num = '' 
print(summ)
