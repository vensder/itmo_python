#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  2016_python.py
#  
#  Student Dmitry Makarov <vensder@gmail.com>



# Даны следующие файлы:
''''
import struct

rgbstr='aabbcc'
print(struct.unpack('BBB',rgbstr.decode('hex')))
'''


print('Test:')
h = '#00ff00'.lstrip('#')
print('RGB =', tuple(int(h[i:i+2], 16) for i in (0, 2 ,4)))



class Color:

    string = ''

    def to_rgb(self):
		
        hex_string = self.string.lstrip('#')
        
        rgb =  tuple((int(hex_string[i:i+2], 16) for i in (0, 2 ,4)))
        
        return rgb
		
		

class Green(Color):

    string = '#00ff00'


class Red(Color):

    string = '#ff0000'


class Blue(Color):

    string = '#0000ff'

green = Green()
print(green.string)
print(green.to_rgb())

red = Red()
print(red.string)
print(red.to_rgb())

blue = Blue()
print(blue.string)
print(blue.to_rgb())


class Line:
	
    def __init__(self, color):
        self.color = color
        
    def show(self, l):
        self.l = l # длина
        print(self.color * self.l)


line = Line('B')
line.show(10) # линия цвета B длиной 10


# Напишите:
#
# 1. в классе Color метод "to_rgb", который будет возвращать
# цвет в виде кортежа, например (30, 10, 20)
#
# 2. напишите класс Line с методом show( <длина> ).
# В конструкторе этому классу передается цвет.
#
# По запуску метода линия отображается в консоле в виде повторения
# заданного символа, например R. Соответственно Red - это R, Green - G,
# Blue - B.
#
# Повторение столько раз, сколько задано в параметре <длина>.
#
# * 3. переопределите оператор сложения (__add__) так, чтобы
# появилась возможность складывать цвета, а сложение шло соответственно зеленый
# с зеленым, красный с красным.. Результат каждой составляющей <= 255.
