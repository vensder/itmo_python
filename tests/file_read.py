#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

file_name = 'my_file.txt'
try:
    with open (file_name) as f:
        content = f.read()
        print(content)
        print('-------')
        content = f.read()
        print(content)
        print('-------')
        content = f.read()
        print(content)
        print('-------')

except FileNotFoundError as e:
    print('File not found\n' + str(e))
    print('Try to create it')
    with open(file_name,'w') as f:
        f.write('done:\n\nproblems:\n\ntodo:\n\n')
        f.close()

with open (file_name) as f:
    content = f.read()
    content = content.split('\n')
    print(content)

with open (file_name) as f:
    content1 = f.readlines()
    for i in range(len(content1)):
        content1[i] = content1[i].strip()
    print(content1)

content3 = []
with open (file_name) as f:
    for line in f:
        content3.append(line.strip())
    list(filter(lambda s: s != '', content3))
    print(content3)
