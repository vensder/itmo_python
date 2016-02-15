

def draw(length,symbol,start='[', end=']'):

    print(start,symbol * length,end)


draw(10,'b','<','>')


def letter(name,product):
    print('''
    hello, Bill!
    My name is %s
    send me product: %s
    ''' % (name,product))

letter('Jon','sugar')


