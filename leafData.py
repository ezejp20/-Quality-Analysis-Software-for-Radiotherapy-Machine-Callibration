# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:20:21 2018

@author: ellen.punter
"""
import numpy as np
def leafData(filename, sign = 1):
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
    with open(filename, mode='r') as infile:
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
    #position33=[i for i,x in enumerate(type_array) if x == "Y33"]
    #print(position33[0])
    #print(data[position33[0]])
    #print position
    leafDoseValues=[]
    #(since each leaf is 1cm and each chamber is separated by 0.5cm we go in steps of 2)
    leafReadingRange=range(0,60,2)
    for i in leafReadingRange:
        #print(i)
        #Position is being incremented by 1 because the central ICP chamber is positioned between two leaves, and if the 
        rawDataPosition=int(position[0])+i
        biasPosition=int(position[0])+i-3
        calibrationPosition=int(position[0])+i-4
        leafDoseValues.append(((np.float(data[rawDataPosition])-((np.float(bias_array[biasPosition]))*np.float(time)))*(np.float(calibration_array[calibrationPosition])))/np.float(gain))
        #print(data[rawDataPosition],bias_array[biasPosition],time,calibration_array[calibrationPosition],gain)
        #print(leafDoseValues[len(leafDoseValues)-1])
       # print(time)
        #print(rawDataPosition)
        #print(data[rawDataPosition])
        #print(rawDataPosition)
#We now want to divide these leaf dose values by the dose value for the 20th leaf (central leaf)
    #print hashmapCentralMinorOffsets
    #print leafDoseValues
    #print(sign)
    return leafDoseValues 
leafDoseValuesJaw1=leafData("T:\Medical Physics\mp-rtphys\Development\Software\QATrack Pimilco\Temp Files - Pimlico\LA1\LA1 03-02-2017\Y1CN.prs")
leafDoseValuesMLC1=leafData("T:\Medical Physics\mp-rtphys\Development\Software\QATrack Pimilco\Temp Files - Pimlico\LA1\LA1 03-02-2017\Y1CM.prs")
leafDoseValuesJaw2=leafData("T:\Medical Physics\mp-rtphys\Development\Software\QATrack Pimilco\Temp Files - Pimlico\LA1\LA1 03-02-2017\Y2CN.prs")
leafDoseValuesMLC2=leafData("T:\Medical Physics\mp-rtphys\Development\Software\QATrack Pimilco\Temp Files - Pimlico\LA1\LA1 03-02-2017\Y2CM.prs")
normalisedLeafDoseValuesJaw1=[]
normalisedLeafDoseValuesMLC1=[]
normalisedLeafDoseValuesJaw2=[]
normalisedLeafDoseValuesMLC2=[]
inTolerance=""
returnRange=range(0,30,1) 
for i in returnRange:
    normalisedLeafDoseValuesJaw1.append(leafDoseValuesJaw1[i]/leafDoseValuesJaw1[15]*100)
    normalisedLeafDoseValuesMLC1.append(leafDoseValuesMLC1[i]/leafDoseValuesMLC1[15]*100)
    normalisedLeafDoseValuesJaw2.append(leafDoseValuesJaw2[i]/leafDoseValuesJaw2[15]*100)
    normalisedLeafDoseValuesMLC2.append(leafDoseValuesMLC2[i]/leafDoseValuesMLC2[15]*100)
leafErrors1=[]
leafOffsets1=[]
leafErrors2=[]
leafOffsets2=[]
resultsRange=range(0,30,1)
for i in resultsRange:
    leafErrors1.append((((normalisedLeafDoseValuesMLC1[i]/normalisedLeafDoseValuesJaw1[i])*100)-100)/20)
    leafOffsets1.append(leafErrors1[i]*12*-1)
    leafErrors2.append((((normalisedLeafDoseValuesMLC2[i]/normalisedLeafDoseValuesJaw2[i])*100)-100)/20)
    leafOffsets2.append(leafErrors2[i]*12)
    if abs(leafErrors1[i])>=0.7:
        inTol="Investigate"
    elif abs(leafErrors1[i])>=1.0:
        inTol="Not Clinical"
#creating output file for recalibrating the linac
q=6#start getting data from leaf 6
#this fills the first 5 lines with empty data (as we are only looking at central leaves here) 
msg = "   1;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n   2;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n   3;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n   4;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n   5;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n"
#Get the results out from the arrays 
for r in resultsRange:
    b=int(leafOffsets1[35-q])
    c=int(leafOffsets2[35-q])
    #makes sure the alignment is exactly right so that minor offsets file can be read in by the linac properly 
    text = f"   {q};    0.00;    0.00;    0.00;    0.00;    0.00;{b:>8};{c:>8}\n"
    q=q+1
    msg=msg+text
    #this adds on 5 more blank rows for the leaves 36-40
msg=msg+"   36;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n   37;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n   38;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n   39;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n   40;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n"
from datetime import date#this is for the filename
date = str(date.today())
#replace dashes for underscores to that this can be used in a filename 
date2=date.replace("-","_")
#print(date2)
fname = "T:/Medical Physics/mp-rtphys/Development/Software/QATrack Pimilco/MinorOffsets_%s.txt" % date2
open(fname, "w").write(msg)

