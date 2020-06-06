# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:57:53 2018

@author: ellen.punter
"""

import numpy as np
with open("T:\Medical Physics\mp-rtphys\Development\Software\QATrack Pimilco\Temp Files - Pimlico\LA1\LA1 03-02-2017\Y2CN.prs", mode='r') as infile:
    type_array = []
    bias_array = []
    calibration_array = []
    data=[]
    gain=[]
    time=[]    
    for line in infile:     
        data=line.split()
        if len(data)==0:continue
    #Get the gain reading
        if data[0]=="Nominal":
            gain.append(line)           
            gain=gain[0].split()
        elif data[0]=="TYPE":
    #Put all the data headings into an array called "type_array" - this is so it's easy to call specific values like "X22" or whatever
            type_array.append(line)
            type_array=[w.replace('\t',' ')for w in type_array]
            type_array=type_array[0].split()
        elif data[0]=="BIAS1":
    #Put all the ICP bias readings into an array called "bias_array"
            bias_array.append(line)
            bias_array=[w.replace('\t',' ')for w in bias_array]
            bias_array=bias_array[0].split()
        elif data[0].startswith("Calibration") and "File" not in data[1]: 
    #Put all the calibration factor readings into an array called "calibration_array"
            calibration_array.append(line)
            calibration_array=[w.replace('\t',' ')for w in calibration_array]
            calibration_array=calibration_array[0].split()
#get time and gain
    time=data[2]
    gain=gain[2]
#Now get the general positions and make calculations of the dose value for each chamber which corresponds to a leaf
#The first data point is y4 because this is the corresponding chamber for leaf 6 - leaf 6 actually lies over chambers Y4 and Y5 but if Y5 is used, the last value (corresponsding to chamber Y63) is out of range
    position=[i for i,x in enumerate(type_array) if x == "Y4"]
    jaw1=[]
    #(since each leaf is 1cm and each chamber is separated by 0.5cm we go in steps of 2)
    leafReadingRange=range(0,60,2)
    for i in leafReadingRange:
        rawDataPosition=int(position[0])+i
        biasPosition=int(position[0])+i-3
        calibrationPosition=int(position[0])+i-4
        jaw1.append(((np.float(data[rawDataPosition])-((np.float(bias_array[biasPosition]))*np.float(time)))*(np.float(calibration_array[calibrationPosition])))/np.float(gain))
