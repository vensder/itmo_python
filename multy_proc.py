import os
from threading import Thread
from time import sleep
#from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool

filenames = os.listdir('.')




def run(index):
	print('working in thread')
	size = 0
	for fi in filenames:
		size += os.path.getsize(fi)
		sleep(0.1)
		print(index,':',size)


thread1 = Thread(target=run, args=(1,))
thread2 = Thread(target=run, args=(2,))
thread1.start()
thread2.start()


thread2.join() # присоединяет поток
print('here im')


with Pool(processes=5) as executor:
	for a in executor.map(run, os.listdir('.')):
		print(a)


''''
with ThreadPoolExecutor(max_workers=5) as executor:
	for a in executor.map(run, os.listdir('.')):
		print(a)
'''
