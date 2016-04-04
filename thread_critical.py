from multiprocessing import Process


def write(filename, word):
	with open (filename, 'w') as f:
		f.write("{}\n".format(word) * 1000000)
	
if __name__ == '__main__':	
	
	FILENAME = 'TTTTTT.txt'
	
	p1 = Process(target=write, args = (FILENAME, 'hello'))
	p1.start()
	
	
	p2 = Process(target=write, args = (FILENAME, 'bye'))
	p2.start()
	
	
