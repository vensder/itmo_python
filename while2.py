

s = 'spameggsspameggs'

i = 0
while True:
    i = s.find('me', i)
    if i < 0:
        break
    print(i)
