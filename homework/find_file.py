#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# student: Dmitry Makarov

import os # import of os module

# check current version of Python
import platform
print(platform.python_version())

'''
/usr/bin/
/usr/lib/
/etc/
/usr/local/lib/
/usr/include/
/usr/share/python/
/usr/share/man/man1/
'''

# variables:
dir_path='/usr/bin/'
find_name='python'
files_number = 0

#print (os.listdir(dir_path)) # list of files and dirs in current dir


# open file for writing, create it if doesn't exist, truncate it if exists ('w+')
file_for_writing = open('output_file.txt', 'w+')

current_message = 'We found these files in dir "' + dir_path +'", which names include substring "python":\n'

print(current_message)
file_for_writing.write(current_message)

# Find files with including find_name 
for file_name in os.listdir(dir_path):
    if file_name.find(find_name) != -1:
        print(file_name)
        file_for_writing.write(file_name + '\n')
        # increment number of found files
        #files_number = files_number + 1
        files_number += 1

current_message = '\nNumber of files is:' + str(files_number)
print(current_message)
file_for_writing.write(current_message)
file_for_writing.close()

input("Press Enter to continue...")

    
file_for_reading = open('output_file.txt')
print('\nRead from closed and opened for reading file:\n')
print(file_for_reading.read())

