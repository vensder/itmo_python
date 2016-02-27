#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# decorators

# несколько длительных функций
# декоратор добавляет вычисление времени выполнения функции

def decorator(func):
	def wrapper(arg1, arg2):
		print('Look at me: ', arg1, arg2)
		func(arg1, arg2)
		
	return wrapper
	
@decorator	
def print_full_name(first_name, last_name):
	print('My name is', first_name, last_name)
	
print_full_name('Vasya','Pupkin')
