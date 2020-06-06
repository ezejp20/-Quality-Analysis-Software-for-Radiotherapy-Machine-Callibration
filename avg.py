# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 10:55:02 2019

@author: ellen.punter
"""
#Create a dictionary from the uploaded file which is filled with all the variable values by variable name
import csv
reader = csv.reader(FILE)
file_upload = {rows[0]:rows[1] for rows in reader}
for n in file_upload.keys():
    try:
        file_upload[n]=float(file_upload[n])
    except:
            pass
vals=[C1_1,C1_2,C1_3,C7_1,C7_2]
x=sum([a for a in vals if isinstance(a,float) or isinstance(a,int)])
i=0
for a in vals:
    if type(a)==float or type(a)==int:
        i=i+1.0
c=x/i
Output6MVResult = ((c*_6MVCF*((273.15+Temp)/293.15)*(1013.25/Pressure))/(RefValMUs6MV))
vals=[C2_1,C2_2,C2_3,C8_1,C8_2]
x=sum([a for a in vals if isinstance(a,float) or isinstance(a,int)])
i=0
for a in vals:
    if type(a)==float or type(a)==int:
        i=i+1.0
c=x/i
Output10MVResult = ((c*_10MVCF*((273.15+Temp)/293.15)*(1013.25/Pressure))/(RefValMUs10MV))
RelOutputVal6MV=Output6MVResult/RefValOutput6MV
RelOutputVal10MV=Output10MVResult/RefValOutput10MV
RelMUsVal6MV=BackupMU6MV/RefValMUs6MV
RelMUsVal10MV=BackupMU10MV/RefValMUs10MV
Energy6MVResult=((C9_1+C9_2)/2.0)/((C1_1+C1_2+C1_3+C7_1+C7_2)/5.0)
Energy10MVResult=((C10_1+C10_2)/2.0)/((C2_1+C2_2+C2_3+C8_1+C8_2)/5.0)
RelValEnergy6MV=Energy6MVResult/EnergyRefVal6MV
RelValEnergy10MV=Energy10MVResult/EnergyRefVal10MV
vals=[C3_1,C3_2,C3_3,C5_1,C5_2]
x=sum([a for a in vals if isinstance(a,float) or isinstance(a,int)])
i=0
for a in vals:
    if type(a)==float or type(a)==int:
        i=i+1.0
y=x/i
vals2=[C1_1,C1_2,C1_3,C7_1,C7_2]
z=sum([a for a in vals2 if isinstance(a,float) or isinstance(a,int)])
j=0
for a in vals2:
    if type(a)==float or type(a)==int:
        j=j+1.0
b=z/j
WedgeFactor6MVResult=y/b
vals=[C4_1,C4_2,C4_3,C6_1,C6_2]
x=sum([a for a in vals if isinstance(a,float) or isinstance(a,int)])
i=0
for a in vals:
    if type(a)==float or type(a)==int:
        i=i+1.0
y=x/i
vals2=[C2_1,C2_2,C2_3,C8_1,C8_2]
z=sum([a for a in vals2 if isinstance(a,float) or isinstance(a,int)])
j=0
for a in vals2:
    if type(a)==float or type(a)==int:
        j=j+1.0
b=z/j
WedgeFactor10MVResult=y/b
RelWedgeFactor6MV=WedgeFactor6MVResult/RefValWedgeFactor6MV
RelWedgeFactor10MV=WedgeFactor10MVResult/RefValWedgeFactor10MV
results={"Output6MVResult": Output6MVResult, "Output10MVResult": Output10MVResult,"RelOutputVal6MV":RelOutputVal6MV, "RelOutputVal10MV":RelOutputVal10MV,
         "RelMUsVal6MV":RelMUsVal6MV,"RelMUsVal10MV":RelMUsVal10MV, "Energy6MVResult":Energy6MVResult,"Energy10MVResult": Energy10MVResult,
         "RelValEnergy6MV":RelValEnergy6MV,"RelValEnergy10MV":RelValEnergy10MV, "WedgeFactor6MVResult":WedgeFactor6MVResult, "WedgeFactor10MVResult":WedgeFactor10MVResult,
         "RelWedgeFactor6MV":RelWedgeFactor6MV,"RelWedgeFactor10MV":RelWedgeFactor10MV }