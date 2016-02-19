#/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    k = 0/0 # требующий проверку код
except ZeroDivisionError: # задать тип исключения
    print('Are you stupid? Zero Division!')
    k = 0 # код исправления ситуации? при возникновении ошибки.
print(k)

try:
    f = open('asdfsdfaf')
    f.read()
except FileNotFoundError:
    print('Where is file?')

#2 + '1'

f = ["123","231",100,"fff"]
ints = []

try:
    for line in lst:
        ints.append(int(line))

except ValueError as e:
    print('это не число')

except Exception:
    print('WTF?')

else:
    print('all is good')

finally:
    f.close()
    print('я зaакрыл файл')


