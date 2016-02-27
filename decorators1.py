#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# decorators

def decorator(function_to_decor):
	
	def new_func():
		print('before func call')
		
		function_to_decor() # function
		print('after')
		
	return(new_func)

@decorator	
def func():
	print('hello from func')
	
func()
