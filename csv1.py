import csv
from random import randint

with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    
with open('eggs.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		print(', '.join(row))

# 1. Две функции - 1) пишет в csv list of lists,2) чтение из csv 

def list_generator():
    lst= [[randint(1,9) for i in range(10)] for i in range(10)]
    return lst

def print_lst(lst):
    for row in lst:
        print(*row, sep=', ')

def write_csv(lst):
    with open('list_of_lists.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',
                                quotechar=';', quoting=csv.QUOTE_MINIMAL)
        for row in lst:
            csvwriter.writerow(row)

lst = list_generator()
print_lst(lst)
write_csv(lst)

