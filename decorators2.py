#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# decorators

# несколько длительных функций
# декоратор добавляет вычисление времени выполнения функции

import time
from datetime import datetime

def decorator(func):
	def new_func():
		
		starttime = datetime.now()
		
		func()
		
		print('exectime: ', datetime.now() - starttime)
		
	return new_func
	
@decorator	
def long_func():
	time.sleep(1.2) 	

long_func()
