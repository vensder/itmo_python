# coding: utf-8

f = open('ttt', 'w') # open for write
f.write('hello') # write
#print(type(f))

f.close() # writen

f = open('ttt') # open for read
print(f.read())

f = open('my_file.txt','w') # open for writing, truncating the file firs
f.write('write1\n')
f.close()

f = open('my_dir/my_file.txt','a') # open for writing, appending to the end of the file if it exists
f.write('write2\n')
f.write('write3\n')
f.close()

f = open('my_file.txt') # open for reading
a = f.read()
l = a.split('\n')
print(l)
l.remove('')
print(l)
