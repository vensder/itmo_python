#!/usr/bin/enf python
# coding: utf-8

import os # imrort of os module

print (os.listdir('../.')) # list of files and dirs in current dir

for file in os.listdir('..'):
    print (file)
#    print ('---ku-ku---')

