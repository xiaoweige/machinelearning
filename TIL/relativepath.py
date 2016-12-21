# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 16:05:31 2016

@author: Stud
http://www.cnblogs.com/dreamafar/p/6203035.html
"""
import os


def readFile(filename):
    filehandle = open(filename)
    print filehandle.read()
    filehandle.close()



fileDir = os.path.dirname(os.path.realpath('__file__'))
print fileDir

#For accessing the file in the same folder
filename = "water_demand2009.csv"
print "This is contents of " +filename
readFile(filename)
#
#For accessing the file in a folder contained in the current folder
filename = os.path.join(fileDir, './dataset/same.txt')
#print "This is contents of" +filename
print filename
readFile(filename)

#For accessing the file in the parent folder of the current folder
#filename = os.path.join(fileDir, '..dataset/same.txt')
#readFile(filename)

#For accessing the file inside a sibling folder.
filename = os.path.join(fileDir, './folder2/same.txt')
filename = os.path.abspath(os.path.realpath(filename))
print filename
readFile(filename)