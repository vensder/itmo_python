# coding: utf-8

f = open('ttt', 'w') # open for write
f.write('hello') # write
print(type(f))

f.close() # writen

f = open('ttt') # open for read
print(f.read())
