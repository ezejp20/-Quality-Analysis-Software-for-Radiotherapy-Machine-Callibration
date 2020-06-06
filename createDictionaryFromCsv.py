# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv 
with open('T:\Medical Physics RS\Trainees\Lena\VBA\pinocchio.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]:rows[1] for rows in reader}
print mydict
#Alternately, for python <= 2.7.1, you want:

#mydict = dict((rows[0],rows[1]) for rows in reader)
