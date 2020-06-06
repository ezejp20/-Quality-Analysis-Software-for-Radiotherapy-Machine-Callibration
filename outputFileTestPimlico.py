# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 10:33:49 2019

@author: ellen.punter
"""
#MACRO NAME: outFile
#Add an error message to be displayed in the test textbox if the file isn't created 
outFile="Error: File not created."
#from django.utils import timezone
from datetime import date
i=1
q=6#start getting data from leaf 6
#this fills the first 5 lines of the output file with empty data (as we are only looking at central leaves here - formatting is done using spaces rather than tabs because the fortmatting has to be quite specific for the output file ) 
msg = "   1;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n   2;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n   3;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n   4;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n   5;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n"
#Get the results out from the arrays 
resultsRange=range(0,30,1)
for r in resultsRange:
    b=int(mlcMinorOffsetsCalculations[leafOffsets1][35-q])
    c=int(mlcMinorOffsetsCalculations[leafOffsets2][35-q])
    #makes sure the alignment is exactly right so that minor offsets file can be read in by the linac properly 
    text = f"   {q};    0.00;    0.00;    0.00;    0.00;    0.00;{b:>8};{c:>8}\n"
    q=q+1
    msg=msg+text
    #this adds on 5 more blank rows for the leaves 36-40
msg=msg+"   36;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n   37;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n   38;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n   39;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n   40;    0.00;    0.00;    0.00;    0.00;    0.00;       0;       0\n" 
#get todays date for filename
date = date.today()
date=str(date)
#change - to _
date2=date.replace("-","_")
#declare filename as results_date and include file pathway 
fname = "SuggestedIPVs_{}.txt".format(date2)
#create file 
UTILS.write_file(fname, msg)


