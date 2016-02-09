#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import platform
print(platform.python_version())

# f = open('file_name_read.txt')
# print(f.read())

f2 = open('file_name_write', 'w+')
f2.write('hello\n')
print('read from opened file for writing with "w+"')
print(f2.read())
#f2.close()

f = open('file_name_write')
print('read from closed file:')
print(f.read())

quit

