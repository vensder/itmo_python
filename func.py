#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, os


def myfunc(x,y):
    def add(x,y): # определяем функцию add
        return x + y # возвращаем сумму
    return add

def func():
    pass # 

print(myfunc('Хэллоу ','ворлддд'))
