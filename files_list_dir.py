

import sys, os

os.listdir('.') # получаем список имен файлов и папок

#if os.path.isdir(fullpath): # проверяем что это каталог

args = sys.argv # параметры запуска модуля

try:
    print(args[1])
except IndexError:
    print('iinput paremeter')

def find_word_in_file(filename, word):
    for line in open(filename):
        if word in line:
            return filename
    return None, None

def ask_is_dir(directory, lst, word):
    if not os.path.isdir(directory):
        raise NotDirectoryError(directory)

    for name in os.listdir(directory):
        if not os.path.isdir(name):
            finded_file = find_word_in_file(name, word)
            if finded_file :
                lst.append(finded_file)

            else:
                ask_is_dir(name, lst, word)

if __name__ == '__main__': # проверка на то, тчо запустл , как программу
    directory = sys.argv[1] # получаем аргумент запуска проги
    word = sys.argv[2]
    lst = []
    
    ask_is_dir(directory, lst, word)

    gen = (name for name in lst)

    for name in gen:
        print(name)





