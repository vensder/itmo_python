
x = 10
lst = [10]

def create_func():
    global x
    
    x += 1
    
    def func(x):
        return x * 2

    return func

func_1 = create_func()

print(func_1(x))
print(func_1(x))

