f = open('ttt')

print(f.read())

f2 = open('ttt', 'w')
f2.write('some text')
f2.close()
