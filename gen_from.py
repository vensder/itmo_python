def gen1():
	
	yield 100
	yield 101
	
def gen2():
	
	yield from gen1() # python 3
	
	#for a in gen1():
	#	yield
