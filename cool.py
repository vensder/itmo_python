

import os

for path in os.listdir('.'):
	print(path, os.path.getsize(path)) # file size
	
	
for p in os.walk('.'): # пробегаем по дереву файлов. в Python 3 - as generator
	print(p)


# get PID of current proc
print('pid: ', os.getpid())

# Переменные окружения
print(os.environ)

PATH = os.environ['PATH']
PATH += ':' + os.path.abspath('.')
os.environ['PATH'] = PATH

print('PATH: ', os.environ['PATH'])


import sys

print(sys.byteorder) # big or little


sys.argv # список параметров значений командной строки.

#print('quit')
#quit()
#print('exit')
#exit()

import argparse

for a in range(10):
	if a > 5:
		prin(a)
		sys.exit(0) # ХОтим выйти сейчас
	
sys.exit(0) #

sys.getdefaultencoding()

sys.getfilesystemencoding()

import shutil

shutil.copy2('file1', 'file2')

