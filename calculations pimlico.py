# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 15:06:51 2018

@author: ellen.punter
"""
normalisedLeafDoseValuesJaw1=[]
normalisedLeafDoseValuesMLC1=[]
returnRange=range(0,30,1) 
for i in returnRange:
    normalisedLeafDoseValuesJaw1.append(jaw1[i]/jaw1[15]*100)
    normalisedLeafDoseValuesMLC1.append(mlc1[i]/mlc1[15]*100)
leafErrors1=[]
leafOffsets1=[]
resultsRange=range(0,30,1)
for i in resultsRange:
    leafErrors1.append((((normalisedLeafDoseValuesMLC1[i]/normalisedLeafDoseValuesJaw1[i])*100)-100)/20)
    leafOffsets1.append(leafErrors1[i]*12*-1)
mlcMinorOffsetsCalculations={"leafErrors1":leafErrors1,"leafOffsets1": leafOffsets1 }