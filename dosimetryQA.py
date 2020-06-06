# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:12:37 2019

@author: Ellen.Punter
"""
reading1chamber1=1.0 
reading1chamber2=2.0 
reading1chamber3=3.0 
reading1chamber4=4.0 

reading2chamber1=5.0 
reading2chamber2=6.0
reading2chamber3=7.0 
reading2chamber4=8.0 

charge1=10.0
charge2=12.0
time2=20.0
time1=0.0

average1=(reading1chamber1+reading2chamber1)/2
average2=(reading1chamber2+reading2chamber2)/2
average3=(reading1chamber3+reading2chamber3)/2
average4=(reading1chamber4+reading2chamber4)/2

#Add baseline ratios to make comparisons to 
baselineRatios=[4.0, 4.0, 4.0, 4.0, 4.0, 4.0] 

averages=[average1, average2, average3, average4]
ratios=[]
differences=[]
ratios.append(averages[0]/averages[1])
ratios.append(averages[0]/averages[2])
ratios.append(averages[0]/averages[3])
ratios.append(averages[1]/averages[2])
ratios.append(averages[1]/averages[3])
ratios.append(averages[2]/averages[3])
for n in range(0,6):
    differences.append((abs(ratios[n]-baselineRatios[n]))/baselineRatios[n])
leakage=((charge2-charge1)/(time2-time1))*100000
results={"averages":averages, "ratios": ratios, "differences":differences, "leakage":leakage}     
