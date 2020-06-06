# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:20:21 2018

@author: ellen.punter
"""
#Create a dictionary connecting leaf number to Y value (for central minor offsets)
leaves=range(6,36,1)
order=range(0,30,1)
chambers=range(5,65,2)
hashmapCentralMinorOffsets={}
for i in order:
        hashmapCentralMinorOffsets[leaves[i]]=chambers[i]
#Initiate the arrays into which all the data we need is going to go 
type_array = []
bias_array = []
calibration_array = []
data=[]
gain=[]
time=[]
with open("T:\Medical Physics\mp-rtphys\Development\Software\QATrack Pimilco\Temp Files - Pimlico\LA1\LA1 03-02-2017\Y2CN.prs", mode='r') as infile:
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
leafDoseValues=[]
leafReadingRange=range(6,36,1)
for n in leafReadingRange:
    rawDataPosition=int(hashmapCentralMinorOffsets[n])
    biasPosition=int(hashmapCentralMinorOffsets[n])-3
    calibrationPosition=int(hashmapCentralMinorOffsets[n])-4
    leafDoseValues.append(((float(data[rawDataPosition])-((float(bias_array[biasPosition]))*float(time)))*(float(calibration_array[calibrationPosition])))/float(gain))
#We now want to divide these leaf dose values by the dose value for the 20th leaf (central leaf)
normalisedLeafDoseValues=[x/leafDoseValues[14] for x in leafDoseValues]
