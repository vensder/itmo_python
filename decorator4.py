#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# decorators

# несколько длительных функций
# декоратор добавляет вычисление времени выполнения функции

def decorator_maker(name):
	print('Im decorator maker')

	def my_decorator(func):
		def wrapper():
			print('Look at me: im wrapper')
			func()
			
		return wrapper
	print('Im return decorator')
	return my_decorator
	
@decorator_maker(name='alex')	
def func():
	pass

func()
func()


