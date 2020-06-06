# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file."""
import csv
import statistics as st
FILE = "T:\Medical Physics\mp-rtphys\Development\Software\QACalc upload to QATrack\pinocchio.csv"
#delete this FILE = line when uploading as a test, it will automatically call itself FILE when uploaded. 
i=0
with open(FILE, mode='r') as infile:
    reader = csv.reader(infile)
    myDict = {rows[0]:rows[1] for rows in reader}
    dictString=str(myDict)
    if dictString.find(': '''):
        i=1
        print ("Not all values have been included, calculations not possible.")
if i==0:
                monthly_stats = {}        
                monthly_stats = {
    "Output (6MV) Result": (((float(myDict['C1.1'])+float(myDict['C1.2'])+float(myDict['C1.3'])+float(myDict['C7.1'])+float(myDict['C7.2']))/5)*float(myDict['6MVCF'])*((273.15+float(myDict['Temp']))/293.15)*(1013.25/float(myDict['Pressure'])))/float(myDict['ElektaPreciseMUs6MV']),
    "Output (6MV) Difference": (((((float(myDict['C1.1'])+float(myDict['C1.2'])+float(myDict['C1.3'])+float(myDict['C7.1'])+float(myDict['C7.2']))/5)*float(myDict['6MVCF'])*((273.15+float(myDict['Temp']))/293.15)*(1013.25/float(myDict['Pressure'])))/float(myDict['ElektaPreciseMUs6MV']))/float(myDict['ElektaPreciseOutput6MV']))-1.0,
    "Output (10MV) Result": (((float(myDict['C2.1'])+float(myDict['C2.2'])+float(myDict['C2.3'])+float(myDict['C8.1'])+float(myDict['C8.2']))/5)*float(myDict['10MVCF'])*((273.15+float(myDict['Temp']))/293.15)*(1013.25/float(myDict['Pressure'])))/float(myDict['ElektaPreciseMUs10MV']),
    "Output (10MV) Difference": (((((float(myDict['C2.1'])+float(myDict['C2.2'])+float(myDict['C2.3'])+float(myDict['C8.1'])+float(myDict['C8.2']))/5)*float(myDict['10MVCF'])*((273.15+float(myDict['Temp']))/293.15)*(1013.25/float(myDict['Pressure'])))/float(myDict['ElektaPreciseMUs10MV']))/float(myDict['ElektaPreciseOutput10MV']))-1.0,
    "Backup MU (6MV) Result": float(myDict['BackupMU6MV']),
    "Backup MU (6MV) Difference":   (float(myDict['BackupMU6MV'])/float(myDict['ElektaPreciseMUs6MV']))-1.0,
    "Backup MU (10MV) Result":float(myDict['BackupMU10MV']),
    "Backup MU (10MV) Difference": (float(myDict['BackupMU10MV'])/float(myDict['ElektaPreciseMUs10MV']))-1.0,
    "Energy (6MV) Result": ((float(myDict['C9.1'])+(float(myDict['C9.2'])))/2.0)/((float(myDict['C1.1'])+float(myDict['C1.2'])+float(myDict['C1.3'])+float(myDict['C7.1'])+float(myDict['C7.2']))/5.0),
    "Energy (6MV) Difference": ((((float(myDict['C9.1'])+(float(myDict['C9.2'])))/2.0)/((float(myDict['C1.1'])+float(myDict['C1.2'])+float(myDict['C1.3'])+float(myDict['C7.1'])+float(myDict['C7.2']))/5.0))/(float(myDict['ElektaPreciseEnergy6MV'])))-1.0,
    "Energy (10MV) Result":((float(myDict['C10.1'])+(float(myDict['C10.2'])))/2.0)/((float(myDict['C2.1'])+float(myDict['C2.2'])+float(myDict['C2.3'])+float(myDict['C8.1'])+float(myDict['C8.2']))/5.0),
    "Energy (10MV) Difference":((((float(myDict['C10.1'])+(float(myDict['C10.2'])))/2.0)/((float(myDict['C2.1'])+float(myDict['C2.2'])+float(myDict['C2.3'])+float(myDict['C8.1'])+float(myDict['C8.2']))/5.0))/(float(myDict['ElektaPreciseEnergy10MV'])))-1.0,
    "Wedge Factor (6MV) Result": ((float(myDict['C3.1'])+(float(myDict['C3.2']))+float(myDict['C3.3'])+float(myDict['C5.1'])+float(myDict['C5.2']))/5.0)/((float(myDict['C1.1'])+(float(myDict['C1.2']))+float(myDict['C1.3'])+float(myDict['C7.1'])+float(myDict['C7.2']))/5.0),
    "Wedge Factor (6MV) Difference":((((float(myDict['C3.1'])+(float(myDict['C3.2']))+float(myDict['C3.3'])+float(myDict['C5.1'])+float(myDict['C5.2']))/5.0)/((float(myDict['C1.1'])+(float(myDict['C1.2']))+float(myDict['C1.3'])+float(myDict['C7.1'])+float(myDict['C7.2']))/5.0))/float(myDict['ElektaPreciseWedgeFactor6MV']))-1.0,
    "Wedge Factor (10MV) Result":((float(myDict['C4.1'])+(float(myDict['C4.2']))+float(myDict['C4.3'])+float(myDict['C6.1'])+float(myDict['C6.2']))/5.0)/((float(myDict['C2.1'])+(float(myDict['C2.2']))+float(myDict['C2.3'])+float(myDict['C8.1'])+float(myDict['C8.2']))/5.0),
    "Wedge Factor (10MV) Difference":((((float(myDict['C4.1'])+(float(myDict['C4.2']))+float(myDict['C4.3'])+float(myDict['C6.1'])+float(myDict['6.2']))/5.0)/((float(myDict['C2.1'])+(float(myDict['C2.2']))+float(myDict['C2.3'])+float(myDict['C8.1'])+float(myDict['C8.2']))/5.0))/float(myDict['ElektaPreciseWedgeFactor10MV']))-1.0,
    "Wedge Error (6MV)": (abs(((float(myDict['C3.1'])+(float(myDict['C3.2']))+float(myDict['C3.3']))/3)-(float(myDict['C5.1'])+(float(myDict['C5.2']))/2.0)))/(float(myDict['C3.1'])+float(myDict['C3.2'])/2.0),
    "Wedge Error (10MV)":(abs(((float(myDict['C4.1'])+(float(myDict['C4.2']))+float(myDict['C4.3']))/3)-(float(myDict['C6.1'])+(float(myDict['C6.2']))/2.0)))/(float(myDict['C4.1'])+float(myDict['C4.2'])/2.0),
    "Reproducibility (6MV)": (st.stdev(float(myDict['C1.1']),float(myDict['C1.2']),float(myDict['C1.3']),float(myDict['C7.1']),float(myDict['C7.2'])))/((float(myDict['C3.1'])+float(myDict['C3.2'])+float(myDict['C3.3'])+float(myDict['C7.1'])+float(myDict['C7.2']))/5.0),
    "Reproducibility (10MV)": (st.stdev(float(myDict['C2.1']),float(myDict['C2.2']),float(myDict['C2.3']),float(myDict['C8.1']),float(myDict['C8.2'])))/((float(myDict['C2.1'])+float(myDict['C2.2'])+float(myDict['C2.3'])+float(myDict['C8.1'])+float(myDict['C8.2']))/5.0),
    "Stability DQA3 (6MV)": (float(myDict['6MVDQA3final'])-float(myDict['6MVDQA3init']))/((float(myDict['6MVDQA3final'])+float(myDict['6MVDQA3init']))/2.0),
    "Stability DQA3 (10MV)":(float(myDict['10MVDQA3final'])-float(myDict['10MVDQA3init']))/((float(myDict['10MVDQA3final'])+float(myDict['10MVDQA3init']))/2.0),
    "Y1 Jaw Forward Speed": (float(myDict['Y1LCWDistance'])*(float(myDict['Y1JawDRFwd'])/60.0))/float(myDict['Y1LCWDose']),
    "Y2 Jaw Forward Speed":(float(myDict['Y2LCWDistance'])*(float(myDict['Y2JawDRFwd'])/60.0))/float(myDict['Y2LCWDose']),
    "Y1 MLC Forward Speed":(float(myDict['Y1MLCCWDistance'])*(float(myDict['Y1MLCDRFwd'])/60.0))/float(myDict['Y1MLCCWDose']),
    "Y2 MLC Forward Speed":(float(myDict['Y2MLCCWDistance'])*(float(myDict['Y2MLCDRFwd'])/60.0))/float(myDict['Y2MLCCWDose']),
    "X1 Jaw Forward Speed":"findOutSoon",
    "X2 Jaw Forward Speed":"findOutSoon",
    "Gantry Forward Speed":(float(myDict['GantryRotationCWDistance'])*(float(myDict['GantryDRFwd'])/60))/float(myDict['GantryRotationCWDose']),
    "Y1 Jaw Reverse Speed":(float(myDict['Y1LCCWDistance'])*(float(myDict['Y1JawDRRev'])/60.0))/float(myDict['Y1LCCWDose']),
    "Y2 Jaw Reverse Speed":(float(myDict['Y2LCCWDistance'])*(float(myDict['Y2JawDRRev'])/60.0))/float(myDict['Y2LCCWDose']),
    "Y1 MLC Reverse Speed":(float(myDict['Y1MLCCCWDistance'])*(float(myDict['Y1MLCDRRev'])/60.0))/float(myDict['Y1MLCCCWDose']),
    "Y2 MLC Reverse Speed":(float(myDict['Y2MLCCCWDistance'])*(float(myDict['Y2MLCDRRev'])/60.0))/float(myDict['Y2MLCCCWDose']),
    "X1 Jaw Reverse Speed":"findOutSoon",
    "X2 Jaw Reverse Speed":"findOutSoon",
    "Gantry Reverse Speed":(float(myDict['GantryRotationCCWDistance'])*(float(myDict['GantryDRRev'])/60.0))/float(myDict['GantryRotationCCWDose'])
    }
                monthly_stats["Open DQA3 (6MV)"]= ((float(myDict['6MVDQA3final'])/float(myDict['BaselineValueOpen6MV']))/((monthly_stats["Output (6MV) Result"]/float(myDict['ElektaPreciseOutput6MV']))))-1.0,
                monthly_stats["Open DQA3 (10MV)"]= ((float(myDict['10MVDQA3final'])/float(myDict['BaselineValueOpen10MV']))/((monthly_stats["Output (10MV) Result"]/float(myDict['ElektaPreciseOutput10MV']))))-1.0,
print(monthly_stats)

Output6MV = ((myDict['C1.1']+myDict['C1.2']+myDict['C1.3']+myDict['C7.1']+myDict['C7.2'])/5.0)*myDict['6MVCF']*((273.15+myDict['Temp'])/293.15)*(1013.25/myDict['Pressure'])/myDict['ElektaPreciseMUs6MV']
Output10MV=(((myDict['C2.1']+myDict['C2.2']+myDict['C2.3']+myDict['C8.1']+myDict['C8.2'])/5.0)*myDict['10MVCF']*((273.15+myDict['Temp'])/293.15)*(1013.25/myDict['Pressure']))/myDict['ElektaPreciseMUs10MV']
(((((myDict['C2_1']+myDict['C2_2']+myDict['C2_3']+myDict['C8_1']+myDict['C8_2'])/5.0)*myDict['_10MVCF']*((273.15+myDict['Temp'])/293.15)*(1013.25/myDict['Pressure']))/myDict['ElektaPreciseMUs10MV'])/myDict['ElektaPreciseOutput10MV'])-1.0
Output10MVResult=((C_1+C2_2+C2_3+C8_1+C8_2)/5.0)*10MVCF*((273.15+Temp)/293.15)*(1013.25/Pressure)/ElektaPreciseMUs10MV
 Y1JawForwardSpeed= (file_upload['Y1LCWDistance']*Y1JawDRFwd/60.0)/file_upload['Y1LCWDose']
    "Y2 Jaw Forward Speed":(float(myDict['Y2LCWDistance'])*(float(myDict['Y2JawDRFwd'])/60.0))/float(myDict['Y2LCWDose']),
    "Y1 MLC Forward Speed":(float(myDict['Y1MLCCWDistance'])*(float(myDict['Y1MLCDRFwd'])/60.0))/float(myDict['Y1MLCCWDose']),
    "Y2 MLC Forward Speed":(float(myDict['Y2MLCCWDistance'])*(float(myDict['Y2MLCDRFwd'])/60.0))/float(myDict['Y2MLCCWDose']),
    "X1 Jaw Forward Speed":"findOutSoon",
    "X2 Jaw Forward Speed":"findOutSoon",
    GantryForwardSpeed=((GantryRotationCWDistance*GantryDRFwd)/60)/GantryRotationCWDose
    "Y1 Jaw Reverse Speed":(float(myDict['Y1LCCWDistance'])*(float(myDict['Y1JawDRRev'])/60.0))/float(myDict['Y1LCCWDose']),
    "Y2 Jaw Reverse Speed":(float(myDict['Y2LCCWDistance'])*(float(myDict['Y2JawDRRev'])/60.0))/float(myDict['Y2LCCWDose']),
    "Y1 MLC Reverse Speed":(float(myDict['Y1MLCCCWDistance'])*(float(myDict['Y1MLCDRRev'])/60.0))/float(myDict['Y1MLCCCWDose']),
    "Y2 MLC Reverse Speed":(float(myDict['Y2MLCCCWDistance'])*(float(myDict['Y2MLCDRRev'])/60.0))/float(myDict['Y2MLCCCWDose']),
    "X1 Jaw Reverse Speed":"findOutSoon",
    "X2 Jaw Reverse Speed":"findOutSoon",
    "Gantry Reverse Speed":(float(myDict['GantryRotationCCWDistance'])*(float(myDict['GantryDRRev'])/60.0))/float(myDict['GantryRotationCCWDose'])