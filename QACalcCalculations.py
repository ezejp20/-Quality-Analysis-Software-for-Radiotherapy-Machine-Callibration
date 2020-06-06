# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 10:55:02 2019

@author: ellen.punter

"""
linac_baselines =	{
  "OpenDQA36MV": 100.0,
  "OpenDQA310MV": 100.0,
  "VersaHD": {
          "5x56MVOpen": 0.938,
          "5x56MVWedge": 0.917,
          "5x510MVOpen": 0.945,
          "5x510MVWedge": 0.918,
          "20x206MVOpen": 1.061,
          "20x206MVWedge": 1.112,
          "20x2010MVOpen": 1.051,
          "20x2010MVWedge": 1.101,
              "B1":{
                    "Output6MV": 1.000, 
                    "Output10MV": 1.000, 
                    "MUs6MV": 100.0, 
                    "MUs10MV": 100.0, 
                    "Energy6MV": 0.710, 
                    "Energy10MV": 0.760, 
                    "WedgeFactor6MV": 0.259, 
                    "WedgeFactor10MV": 0.275,
                      "Y1MLC":{
                              "Speed": 3.8, 
                              "CWDistance": 18.0, 
                              "CCWDistance": 18.0, 
                              "CWDose": 25.0, 
                              "CCWDose": 25.0
                               },
                       "Y2MLC":{
                               "Speed": 3.8, 
                               "CWDistance": 18.0, 
                               "CCWDistance": 18.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0},
                       "X1Jaw":{
                               "Speed": 3.3, 
                               "CWDistance": 18.0, 
                               "CCWDistance": 18.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0},
                       "X2Jaw":{
                               "Speed": 3.3, 
                               "CWDistance": 18.0, 
                               "CCWDistance": 18.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0},
                       "Gantry":{
                               "Speed": 4.0, 
                               "CWDistance": 45.0, 
                               "CCWDistance": 45.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0
                               },},
              "E1": {
                     "Output6MV": 1.000, 
                      "Output10MV": 1.000, 
                      "MUs6MV": 100.0, 
                      "MUs10MV": 100.0, 
                      "Energy6MV": 0.710, 
                           "Energy10MV": 0.760, 
                           "WedgeFactor6MV": 0.259, 
                           "WedgeFactor10MV": 0.275,
                      "Y1MLC":{
                              "Speed": 3.8, 
                              "CWDistance": 18.0, 
                              "CCWDistance": 18.0, 
                              "CWDose": 25.0, 
                              "CCWDose": 25.0
                               },
                       "Y2MLC":{
                               "Speed": 3.8, 
                               "CWDistance": 18.0, 
                               "CCWDistance": 18.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0},
                       "X1Jaw":{
                               "Speed": 3.3, 
                               "CWDistance": 18.0, 
                               "CCWDistance": 18.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0},
                       "X2Jaw":{
                               "Speed": 3.3, 
                               "CWDistance": 18.0, 
                               "CCWDistance": 18.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0
                               },
                       "Gantry":{
                               "Speed": 4.0, 
                               "CWDistance": 45.0, 
                               "CCWDistance": 45.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0
                               },
                       },
                    "E2": {
                    "Output6MV": 1.000, 
                    "Output10MV": 1.000, 
                    "MUs6MV": 100.0, 
                    "MUs10MV": 100.0, 
                    "Energy6MV": 0.710, 
                    "Energy10MV": 0.760, 
                    "WedgeFactor6MV": 0.259, 
                    "WedgeFactor10MV": 0.275,
                      "Y1MLC":{
                              "Speed": 3.8, 
                              "CWDistance": 18.0, 
                              "CCWDistance": 18.0, 
                              "CWDose": 25.0, 
                              "CCWDose": 25.0
                               },
                       "Y2MLC":{
                               "Speed": 3.8, 
                               "CWDistance": 18.0, 
                               "CCWDistance": 18.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0},
                       "X1Jaw":{
                               "Speed": 3.3, 
                               "CWDistance": 18.0, 
                               "CCWDistance": 18.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0},
                       "X2Jaw":{
                               "Speed": 3.3, 
                               "CWDistance": 18.0, 
                               "CCWDistance": 18.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0},
                       "Gantry":{
                               "Speed": 4.0, 
                               "CWDistance": 45.0, 
                               "CCWDistance": 45.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0
                               },
                       },},
    "Precise": {
            "5x56MVOpen": 0.937,
          "5x56MVWedge": 0.918,
          "5x510MVOpen": 0.933,
          "5x510MVWedge": 0.912,
          "20x206MVOpen": 1.06,
          "20x206MVWedge": 1.102,
          "20x2010MVOpen": 1.054,
          "20x2010MVWedge": 1.101,
           "LA1":{     "Output6MV": 1.000, 
                    "Output10MV": 1.000, 
                    "MUs6MV": 100.0, 
                    "MUs10MV": 100.0, 
                    "Energy6MV": 0.703, 
                    "Energy10MV": 0.752, 
                    "WedgeFactor6MV": 0.267, 
                    "WedgeFactor10MV": 0.285,
                      "Y1Jaw":{
                              "Speed": 1.4, 
                              "CWDistance": 18.0, 
                              "CCWDistance": 0.0, 
                              "CWDose": 25.0, 
                              "CCWDose": 25.0
                              },
                      "Y2Jaw":{
                              "Speed": 1.4, 
                              "CWDistance": 18.0, 
                              "CCWDistance": 18.0, 
                              "CWDose": 25.0, 
                              "CCWDose": 25.0
                              },
                      "Y1MLC":{
                              "Speed": 1.9, 
                              "CWDistance": 18.0, 
                              "CCWDistance": 18.0, 
                              "CWDose": 25.0, 
                              "CCWDose": 25.0
                               },
                       "Y2MLC":{
                               "Speed": 1.9, 
                               "CWDistance": 18.0, 
                               "CCWDistance": 18.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0},
                       "X1Jaw":{
                               "Speed": 1.4, 
                               "CWDistance": 18.0, 
                               "CCWDistance": 18.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0},
                       "X2Jaw":{
                               "Speed": 1.4, 
                               "CWDistance": 18.0, 
                               "CCWDistance": 18.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0},
                       "Gantry":{
                               "Speed": 5.0, 
                               "CWDistance": 45.0, 
                               "CCWDistance": 45.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0
                               },},
                "LA2":{
                       "Output6MV": 1.000, 
                    "Output10MV": 1.000, 
                    "MUs6MV": 100.0, 
                    "MUs10MV": 100.0, 
                    "Energy6MV": 0.703, 
                    "Energy10MV": 0.752, 
                    "WedgeFactor6MV": 0.267, 
                    "WedgeFactor10MV": 0.285,
                      "Y1Jaw":{
                              "Speed": 1.4, 
                              "CWDistance": 18.0, 
                              "CCWDistance": 0.0, 
                              "CWDose": 25.0, 
                              "CCWDose": 25.0
                              },
                      "Y2Jaw":{
                              "Speed": 1.4, 
                              "CWDistance": 18.0, 
                              "CCWDistance": 18.0, 
                              "CWDose": 25.0, 
                              "CCWDose": 25.0
                              },
                      "Y1MLC":{
                              "Speed": 1.9, 
                              "CWDistance": 18.0, 
                              "CCWDistance": 18.0, 
                              "CWDose": 25.0, 
                              "CCWDose": 25.0
                               },
                       "Y2MLC":{
                               "Speed": 1.9, 
                               "CWDistance": 18.0, 
                               "CCWDistance": 18.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0},
                       "X1Jaw":{
                               "Speed": 1.4, 
                               "CWDistance": 18.0, 
                               "CCWDistance": 18.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0},
                       "X2Jaw":{
                               "Speed": 1.4, 
                               "CWDistance": 18.0, 
                               "CCWDistance": 18.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0},
                       "Gantry":{
                               "Speed": 5.0, 
                               "CWDistance": 45.0, 
                               "CCWDistance": 45.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0
                               },}, 
                        "LA4":{ "Output6MV": 1.000, 
                    "Output10MV": 1.000, 
                    "MUs6MV": 100.0, 
                    "MUs10MV": 100.0, 
                    "Energy6MV": 0.703, 
                    "Energy10MV": 0.752, 
                    "WedgeFactor6MV": 0.267, 
                    "WedgeFactor10MV": 0.285,
                      "Y1Jaw":{
                              "Speed": 1.4, 
                              "CWDistance": 18.0, 
                              "CCWDistance": 0.0, 
                              "CWDose": 25.0, 
                              "CCWDose": 25.0
                              },
                      "Y2Jaw":{
                              "Speed": 1.4, 
                              "CWDistance": 18.0, 
                              "CCWDistance": 18.0, 
                              "CWDose": 25.0, 
                              "CCWDose": 25.0
                              },
                      "Y1MLC":{
                              "Speed": 1.9, 
                              "CWDistance": 18.0, 
                              "CCWDistance": 18.0, 
                              "CWDose": 25.0, 
                              "CCWDose": 25.0
                               },
                       "Y2MLC":{
                               "Speed": 1.9, 
                               "CWDistance": 18.0, 
                               "CCWDistance": 18.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0},
                       "X1Jaw":{
                               "Speed": 1.4, 
                               "CWDistance": 18.0, 
                               "CCWDistance": 18.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0},
                       "X2Jaw":{
                               "Speed": 1.4, 
                               "CWDistance": 18.0, 
                               "CCWDistance": 18.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0},
                       "Gantry":{
                               "Speed": 5.0, 
                               "CWDistance": 45.0, 
                               "CCWDistance": 45.0, 
                               "CWDose": 25.0, 
                               "CCWDose": 25.0
                               },},
                        }
                        }
C1_1=1
C1_2=2
C1_3=3
C7_1=4
C7_2=5
_6MVCF=8
Temp=21.3
Pressure=1013.5
RefValMUs6MV=100
C2_1=6
C2_2=7
C2_3=23
C8_1=9
C8_2=0.6
_10MVCF=25
RefValMUs10MV=100
RefValOutput6MV=100
RefValOutput10MV=100
BackupMU6MV=100
BackupMU10MV=100
C9_1=12
C9_2=5
C10_1=16
C10_2=55
EnergyRefVal6MV=100
EnergyRefVal10MV=100
C3_1=45
C3_2=78
C3_3=5
C5_1=12
C5_2=10
C4_1=6
C4_2=3
C4_3=88
C6_1=0.5
RefValWedgeFactor10MV=56
C6_2=""
RefValWedgeFactor6MV=35
OpenDQA36MV=600
BaselineValueDQA3Open6MV=0.3
OpenDQA310MV=100
BaselineValueDQA3Open10MV=100
_6MVDQA3final=102
_6MVDQA3init=165
_10MVDQA3final=166
_10MVDQA3init=6
Machine="B1"
#Create an average function which calculates the mean by counting how many values are there and averaging them, but not causing an error if the fields are not completed
def avg_function(values):
    x=sum([a for a in values if isinstance(a,float) or isinstance(a,int)])
    i=0
    for a in values:
        if type(a)==float or type(a)==int:
            i=i+1.0
    try:
        avg=x/i
    except: 
        avg=""
    return avg
#Calculate Output 6MV Result
vals=[C1_1,C1_2,C1_3,C7_1,C7_2]
Output6MVResult = ((avg_function(vals)*_6MVCF*((273.15+Temp)/293.15)*(1013.25/Pressure))/(RefValMUs6MV))
#Calculate Output 10MV Result
vals=[C2_1,C2_2,C2_3,C8_1,C8_2]
Output10MVResult = ((avg_function(vals)*_10MVCF*((273.15+Temp)/293.15)*(1013.25/Pressure))/(RefValMUs10MV))
#Calculate relative output 6MV
RelOutputVal6MV=Output6MVResult/RefValOutput6MV
#Calculate relative output 10MV
RelOutputVal10MV=Output10MVResult/RefValOutput10MV
#Calculate relative MUs value for 6MV
RelMUsVal6MV=BackupMU6MV/RefValMUs6MV
#Calculate relative MUs value for 10MV
RelMUsVal10MV=BackupMU10MV/RefValMUs10MV
#Calculate energy result for 6MV
vals1=[C9_1,C9_2]
vals2=[C1_1,C1_2,C1_3,C7_1,C7_2]
Energy6MVResult=avg_function(vals1)/avg_function(vals2)
#Calculate energy result for 10MV
vals1=[C10_1,C10_2]
vals2=[C2_1,C2_2,C2_3,C8_1,C8_2]
Energy10MVResult=avg_function(vals1)/avg_function(vals2)
#Calculate relative energy value 6MV
RelValEnergy6MV=Energy6MVResult/EnergyRefVal6MV
#Calculate relative energy value 10MV
RelValEnergy10MV=Energy10MVResult/EnergyRefVal10MV
#Calculate wedge factor result for 6MV
vals1=[C3_1,C3_2,C3_3,C5_1,C5_2]
y=avg_function(vals1)
vals2=[C1_1,C1_2,C1_3,C7_1,C7_2]
b=avg_function(vals2)
WedgeFactor6MVResult=y/b 
#Calculate wedge factor result for 10MV
vals=[C4_1,C4_2,C4_3,C6_1,C6_2]
y=avg_function(vals)
vals2=[C2_1,C2_2,C2_3,C8_1,C8_2]
b=avg_function(vals2)
WedgeFactor10MVResult=y/b
#Calculate relative wedge factor 6MV
RelWedgeFactor6MV=WedgeFactor6MVResult/RefValWedgeFactor6MV
#Calculate relative wedge factor 10MV
RelWedgeFactor10MV=WedgeFactor10MVResult/RefValWedgeFactor10MV
#Calculate wedge error for 6MV
vals1=[C3_1,C3_2,C3_3]
a=avg_function(vals1)
vals2=[C5_1,C5_2]
b=avg_function(vals2)
vals3=[C3_1,C3_2]
c=avg_function(vals3)
WedgeError6MV=abs((a-b)/c)
#Calculate wedge error for 10MV
vals1=[C4_1,C4_2,C4_3]
a=avg_function(vals1)
vals2=[C6_1,C6_2]
b=avg_function(vals2)
vals3=[C4_1,C4_2]
c=avg_function(vals3)
WedgeError10MV=abs((a-b)/c)
#Calculate reproducibility for 6MV
#Function which calculates the standard deviation 
def std_fctn(values):
    import numpy as np
    a=[]
    for n in range(0,len(values)):
        if type(vals[n])==float or type(vals[n])==int:
            a.append(vals[n])
    return np.std(a)
vals=[C1_1,C1_2,C1_3,C7_1,C7_2]
c=avg_function(vals)
b=std_fctn(vals)
Reproducibility6MV=b/c
#Calculate reproducibility for 10MV
vals=[C2_1,C2_2,C2_3,C8_1,C8_2]
b=std_fctn(vals)
c=avg_function(vals)
Reproducibility10MV=b/c
#Calculate DQA3 Calibratino check for 6MV
try:
    DQA3CalibrationCheck6MV=((OpenDQA36MV/BaselineValueDQA3Open6MV)/(Output6MVResult/RefValOutput6MV))-1
except:
    pass
#Calculate DQA3 Calibratino check for 10MV
try:     
    DQA3CalibrationCheck10MV=((OpenDQA310MV/BaselineValueDQA3Open10MV)/(Output10MVResult/RefValOutput10MV))-1
except:
    pass
#Calculate stability for the 6MV DQA3 
try:
    StabilityDQA36MV=(_6MVDQA3final-_6MVDQA3init)/((_6MVDQA3final+_6MVDQA3init)/2.0)
except:
    pass
#Calculate stability for the 10MV DQA3 
try:
    StabilityDQA310MV=(_10MVDQA3final-_10MVDQA3init)/((_10MVDQA3final+_10MVDQA3init)/2.0)
except:
    pass
#Calculate the Y1 forward speed and Residual Y1 forward speed and Y1 Jaw Reverse Speed and Residual Y1 Reverse Speed.... etc etc 
if Machine=="B1" or Machine=="E1" or Machine=="E2":
    ExpectedY1JawForwardSpeed="N/A"
    ExpectedY1JawReverseSpeed="N/A"
    ExpectedY2JawForwardSpeed="N/A"
    ExpectedY2JawReverseSpeed="N/A"
elif Machine=='E1':
    Y1JawForwardSpeed="N/A"
    ResY1JawFwdSpeed=0
    Y1JawReverseSpeed="N/A"
    ResY1JawRevSpeed=0
    Y2JawForwardSpeed="N/A"
    Y2JawReverseSpeed="N/A"
    ExpectedY1MLCForwardSpeed=linac_baselines["VersaHD"]["E1"]["Y1MLC"]["Speed"]
    ExpectedY1MLCReverseSpeed=linac_baselines["VersaHD"]["E1"]["Y1MLC"]["Speed"]
    ExpectedY2MLCForwardSpeed=linac_baselines["VersaHD"]["E1"]["Y2MLC"]["Speed"]
    ExpectedY2MLCReverseSpeed=linac_baselines["VersaHD"]["E1"]["Y2MLC"]["Speed"]
    ExpectedX1JawForwardSpeed=linac_baselines["VersaHD"]["E1"]["X1Jaw"]["Speed"]
    ExpectedX1JawReverseSpeed=linac_baselines["VersaHD"]["E1"]["X1Jaw"]["Speed"]
    ExpectedX2JawForwardSpeed=linac_baselines["VersaHD"]["E1"]["X2Jaw"]["Speed"]
    ExpectedX2JawReverseSpeed=linac_baselines["VersaHD"]["E1"]["X2Jaw"]["Speed"]
    ExpectedGantryForwardSpeed=linac_baselines["VersaHD"]["E1"]["Gantry"]["Speed"]
    ExpectedGantryReverseSpeed=linac_baselines["VersaHD"]["E1"]["Gantry"]["Speed"]
elif Machine=='B1':
    Y1JawForwardSpeed="N/A"
    ResY1JawFwdSpeed=0
    Y1JawReverseSpeed="N/A"
    ResY1JawRevSpeed=0
    Y2JawForwardSpeed="N/A"
    Y2JawReverseSpeed="N/A"
    ResY2JawRevSpeed=0
    ExpectedY1MLCForwardSpeed=linac_baselines["VersaHD"]["B1"]["Y1MLC"]["Speed"]
    ExpectedY1MLCReverseSpeed=linac_baselines["VersaHD"]["B1"]["Y1MLC"]["Speed"]
    ExpectedY2MLCForwardSpeed=linac_baselines["VersaHD"]["B1"]["Y2MLC"]["Speed"]
    ExpectedY2MLCReverseSpeed=linac_baselines["VersaHD"]["B1"]["Y2MLC"]["Speed"]
    ExpectedX1JawForwardSpeed=linac_baselines["VersaHD"]["B1"]["X1Jaw"]["Speed"]
    ExpectedX1JawReverseSpeed=linac_baselines["VersaHD"]["B1"]["X1Jaw"]["Speed"]
    ExpectedX2JawForwardSpeed=linac_baselines["VersaHD"]["B1"]["X2Jaw"]["Speed"]
    ExpectedX2JawReverseSpeed=linac_baselines["VersaHD"]["B1"]["X2Jaw"]["Speed"]
    ExpectedGantryForwardSpeed=linac_baselines["VersaHD"]["B1"]["Gantry"]["Speed"]
    ExpectedGantryReverseSpeed=linac_baselines["VersaHD"]["B1"]["Gantry"]["Speed"]
elif Machine=='E2':
    Y1JawForwardSpeed="N/A"
    ResY1JawFwdSpeed=0
    Y1JawReverseSpeed="N/A"
    ResY1JawRevSpeed=0
    Y2JawForwardSpeed="N/A"
    ResY2JawFwdSpeed=0
    Y2JawReverseSpeed="N/A"
    ResY2JawRevSpeed=0
    ExpectedY1MLCForwardSpeed=linac_baselines["VersaHD"]["E2"]["Y1MLC"]["Speed"]
    ExpectedY1MLCReverseSpeed=linac_baselines["VersaHD"]["E2"]["Y1MLC"]["Speed"]
    ExpectedY2MLCForwardSpeed=linac_baselines["VersaHD"]["E2"]["Y2MLC"]["Speed"]
    ExpectedY2MLCReverseSpeed=linac_baselines["VersaHD"]["E2"]["Y2MLC"]["Speed"]
    ExpectedX1JawForwardSpeed=linac_baselines["VersaHD"]["E2"]["X1Jaw"]["Speed"]
    ExpectedX1JawReverseSpeed=linac_baselines["VersaHD"]["E2"]["X1Jaw"]["Speed"]
    ExpectedX2JawForwardSpeed=linac_baselines["VersaHD"]["E2"]["X2Jaw"]["Speed"]
    ExpectedX2JawReverseSpeed=linac_baselines["VersaHD"]["E2"]["X2Jaw"]["Speed"]
    ExpectedGantryForwardSpeed=linac_baselines["VersaHD"]["E2"]["Gantry"]["Speed"]
    ExpectedGantryReverseSpeed=linac_baselines["VersaHD"]["E2"]["Gantry"]["Speed"]
elif Machine=="LA1": 
    ExpectedY1MLCForwardSpeed=linac_baselines["Precise"]["LA1"]["Y1MLC"]["Speed"]
    ExpectedY1MLCReverseSpeed=linac_baselines["Precise"]["LA1"]["Y1MLC"]["Speed"]
    ExpectedY2MLCForwardSpeed=linac_baselines["Precise"]["LA1"]["Y2MLC"]["Speed"]
    ExpectedY2MLCReverseSpeed=linac_baselines["Precise"]["LA1"]["Y2MLC"]["Speed"]
    ExpectedX1JawForwardSpeed=linac_baselines["Precise"]["LA1"]["X1Jaw"]["Speed"]
    ExpectedX1JawReverseSpeed=linac_baselines["Precise"]["LA1"]["X1Jaw"]["Speed"]
    ExpectedX2JawForwardSpeed=linac_baselines["Precise"]["LA1"]["X2Jaw"]["Speed"]
    ExpectedX2JawReverseSpeed=linac_baselines["Precise"]["LA1"]["X2Jaw"]["Speed"]
    ExpectedGantryForwardSpeed=linac_baselines["Precise"]["LA1"]["Gantry"]["Speed"]
    ExpectedGantryReverseSpeed=linac_baselines["Precise"]["LA1"]["Gantry"]["Speed"]
    ExpectedY1JawForwardSpeed=linac_baselines["Precise"]["LA1"]["Y1Jaw"]["Speed"]
    ExpectedY1JawReverseSpeed=linac_baselines["Precise"]["LA1"]["Y1Jaw"]["Speed"]
    ExpectedY2JawForwardSpeed=linac_baselines["Precise"]["LA1"]["Y2Jaw"]["Speed"]
    ExpectedY2JawReverseSpeed=linac_baselines["Precise"]["LA1"]["Y2Jaw"]["Speed"]
elif Machine=="LA4": 
    ExpectedY1MLCForwardSpeed=linac_baselines["Precise"]["LA4"]["Y1MLC"]["Speed"]  
    ExpectedY1MLCReverseSpeed=linac_baselines["Precise"]["LA4"]["Y1MLC"]["Speed"]
    ExpectedY2MLCForwardSpeed=linac_baselines["Precise"]["LA4"]["Y2MLC"]["Speed"]
    ExpectedY2MLCReverseSpeed=linac_baselines["Precise"]["LA4"]["Y2MLC"]["Speed"]
    ExpectedX1JawForwardSpeed=linac_baselines["Precise"]["LA4"]["X1Jaw"]["Speed"]  
    ExpectedX1JawReverseSpeed=linac_baselines["Precise"]["LA4"]["X1Jaw"]["Speed"]
    ExpectedX2JawForwardSpeed=linac_baselines["Precise"]["LA4"]["X2Jaw"]["Speed"]  
    ExpectedX2JawReverseSpeed=linac_baselines["Precise"]["LA4"]["X2Jaw"]["Speed"]
    ExpectedGantryForwardSpeed=linac_baselines["Precise"]["LA4"]["Gantry"]["Speed"] 
    ExpectedGantryReverseSpeed=linac_baselines["Precise"]["LA4"]["Gantry"]["Speed"]
    ExpectedY1JawForwardSpeed=linac_baselines["Precise"]["LA4"]["Y1Jaw"]["Speed"]
    ExpectedY1JawReverseSpeed=linac_baselines["Precise"]["LA4"]["Y1Jaw"]["Speed"]  
    ExpectedY2JawForwardSpeed=linac_baselines["Precise"]["LA4"]["Y2Jaw"]["Speed"]       
    ExpectedY2JawReverseSpeed=linac_baselines["Precise"]["LA4"]["Y2Jaw"]["Speed"]  
else:
    Y1JawForwardSpeed= ((file_upload['Y1JawCWDistance']*Y1JawDRFwd)/60.0)/file_upload['Y1JawCWDose']
    ResY1JawFwdSpeed=ExpectedY1JawForwardSpeed-Y1JawForwardSpeed
    Y1JawReverseSpeed= ((file_upload['Y1JawCCWDistance']*Y1JawDRRev)/60.0)/file_upload['Y1JawCCWDose'] 
    ResY1JawRevSpeed=ExpectedY1JawReverseSpeed-Y1JawReverseSpeed  
    Y2JawForwardSpeed= ((file_upload['Y2JawCWDistance']*Y2JawDRFwd)/60.0)/file_upload['Y2JawCWDose']
    ResY2JawFwdSpeed=ExpectedY2JawForwardSpeed-Y2JawForwardSpeed 
    Y2JawReverseSpeed= ((file_upload['Y2JawCCWDistance']*Y2JawDRRev)/60.0)/file_upload['Y2JawCCWDose'] 
    ResY2JawRevSpeed=ExpectedY2JawReverseSpeed-Y2JawReverseSpeed

Y1MLCForwardSpeed= (file_upload['Y1MLCCWDistance']*Y1MLCDRFwd/60.0)/file_upload['Y1MLCCWDose']    
ResY1MLCFwdSpeed=ExpectedY1MLCForwardSpeed-Y1MLCForwardSpeed    
Y1MLCReverseSpeed= (file_upload['Y1MLCCCWDistance']*Y1MLCDRRev/60.0)/file_upload['Y1MLCCCWDose']
ResY1MLCRevSpeed=ExpectedY1MLCReverseSpeed-Y1MLCReverseSpeed    
Y2MLCForwardSpeed= (file_upload['Y2MLCCWDistance']*Y2MLCDRFwd/60.0)/file_upload['Y2MLCCWDose']    
ResY2MLCFwdSpeed=ExpectedY2MLCForwardSpeed-Y2MLCForwardSpeed    
Y2MLCReverseSpeed= (file_upload['Y2MLCCCWDistance']*Y2MLCDRRev/60.0)/file_upload['Y2MLCCCWDose']
ResY2MLCRevSpeed=ExpectedY2MLCReverseSpeed-Y2MLCReverseSpeed    
X1JawForwardSpeed= (X1JawCWDistance*X1JawDRFwd/60.0)/X1JawCWDose    
ResX1JawFwdSpeed=ExpectedX1JawForwardSpeed-X1JawForwardSpeed    
X1JawReverseSpeed= (X1JawCCWDistance*X1JawDRRev/60.0)/X1JawCCWDose    
ResX1JawRevSpeed=ExpectedX1JawReverseSpeed-X1JawReverseSpeed
ResX1JawRevSpeed=ExpectedX1JawReverseSpeed-X1JawReverseSpeed
X2JawForwardSpeed= (X2JawCWDistance*X2JawDRFwd/60.0)/X2JawCWDose
ResX2JawFwdSpeed=ExpectedX2JawForwardSpeed-X2JawForwardSpeed    
X2JawReverseSpeed= (X2JawCCWDistance*X2JawDRRev/60.0)/X2JawCCWDose    
ResX2JawRevSpeed=ExpectedX2JawReverseSpeed-X2JawReverseSpeed    
GantryForwardSpeed=((GantryRotationCWDistance*GantryDRFwd)/60)/GantryRotationCWDose        
ResGantryFwdSpeed=ExpectedGantryForwardSpeed-GantryForwardSpeed    
GantryReverseSpeed=((GantryRotationCCWDistance*GantryDRRev)/60)/GantryRotationCCWDose   
ResGantryRevSpeed=ExpectedGantryReverseSpeed-GantryReverseSpeed
    
results={"Output6MVResult": Output6MVResult, "Output10MVResult": Output10MVResult,"RelOutputVal6MV":RelOutputVal6MV, "RelOutputVal10MV":RelOutputVal10MV,
         "RelMUsVal6MV":RelMUsVal6MV,"RelMUsVal10MV":RelMUsVal10MV, "Energy6MVResult":Energy6MVResult,"Energy10MVResult": Energy10MVResult,
         "RelValEnergy6MV":RelValEnergy6MV,"RelValEnergy10MV":RelValEnergy10MV, "WedgeFactor6MVResult":WedgeFactor6MVResult, "WedgeFactor10MVResult":WedgeFactor10MVResult,
         "RelWedgeFactor6MV":RelWedgeFactor6MV,"RelWedgeFactor10MV":RelWedgeFactor10MV, "WedgeError6MV":WedgeError6MV,"WedgeError10MV":WedgeError10MV,
         "Reproducibility6MV":Reproducibility6MV,"Reproducibility10MV":Reproducibility10MV, "DQA3CalibrationCheck6MV":DQA3CalibrationCheck6MV,
         "DQA3CalibrationCheck10MV":DQA3CalibrationCheck10MV,"StabilityDQA36MV":StabilityDQA36MV,"StabilityDQA310MV":StabilityDQA310MV,
         "Y1JawForwardSpeed":Y1JawForwardSpeed,"ExpectedY1JawForwardSpeed":ExpectedY1JawForwardSpeed,"ResY1JawFwdSpeed":ResY1JawFwdSpeed,
         "Y1JawReverseSpeed":Y1JawReverseSpeed,"ExpectedY1JawReverseSpeed":ExpectedY1JawReverseSpeed,"ResY1JawRevSpeed":ResY1JawRevSpeed,
         "Y2JawForwardSpeed":Y2JawForwardSpeed,"ExpectedY2JawForwardSpeed":ExpectedY2JawForwardSpeed,"ResY2JawFwdSpeed": ResY2JawFwdSpeed,
         "Y2JawReverseSpeed":Y2JawReverseSpeed,"ExpectedY2JawReverseSpeed":ExpectedY2JawReverseSpeed, "ResY2JawRevSpeed":ResY2JawRevSpeed,
         "Y1MLCForwardSpeed":Y1MLCForwardSpeed,"ExpectedY1MLCForwardSpeed":ExpectedY1MLCForwardSpeed, "ResY1MLCFwdSpeed":ResY1MLCFwdSpeed,
         "Y1MLCReverseSpeed":Y1MLCReverseSpeed, "ExpectedY1MLCReverseSpeed":ExpectedY1MLCReverseSpeed,"ResY1MLCRevSpeed":ResY1MLCRevSpeed,
         "Y2MLCForwardSpeed":Y2MLCForwardSpeed, "ExpectedY2MLCForwardSpeed":ExpectedY2MLCForwardSpeed,"ResY2MLCFwdSpeed":ResY2MLCFwdSpeed,
         "Y2MLCReverseSpeed":Y2MLCReverseSpeed, "ExpectedY2MLCReverseSpeed":ExpectedY2MLCReverseSpeed, "ResY2MLCRevSpeed":ResY2MLCRevSpeed,
         "X1JawForwardSpeed":X1JawForwardSpeed, "ExpectedX1JawForwardSpeed":ExpectedX1JawForwardSpeed, "ResX1JawFwdSpeed":ResX1JawFwdSpeed,
         "X1JawReverseSpeed":X1JawReverseSpeed, "ExpectedX1JawReverseSpeed": ExpectedX1JawReverseSpeed, "ResX1JawRevSpeed":ResX1JawRevSpeed,
         "ExpectedX1JawReverseSpeed":ExpectedX1JawReverseSpeed, "ResX1JawRevSpeed":ResX1JawRevSpeed, "X2JawForwardSpeed":X2JawForwardSpeed, 
         "ExpectedX2JawForwardSpeed":ExpectedX2JawForwardSpeed, "ResX2JawFwdSpeed":ResX2JawFwdSpeed, "X2JawReverseSpeed":X2JawReverseSpeed,
         "ExpectedX2JawReverseSpeed":ExpectedX2JawReverseSpeed, "ResX2JawRevSpeed":ResX2JawRevSpeed,"GantryForwardSpeed":GantryForwardSpeed,
         "ExpectedGantryForwardSpeed":ExpectedGantryForwardSpeed, "ResGantryFwdSpeed":ResGantryFwdSpeed, "GantryReverseSpeed":GantryReverseSpeed,
         "ExpectedGantryReverseSpeed":ExpectedGantryReverseSpeed, "ResGantryRevSpeed":ResGantryRevSpeed}