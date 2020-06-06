# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:01:01 2019

@author: Ellen.Punter
"""
C1_1=9.0
C1_2=10.0
C1_3=11.0
C2_1=9.0
C2_2=10.0
C2_3=11.0
C3_1=9.0
C3_2=10.0
C3_3=11.0
C4_1=9.0
C4_2=10.0
C4_3=11.0
C5_1=28.0
C5_2=27.0
C6_1=28.0
C6_2=27.0
C7_1=28.0
C7_2=27.0
C8_1=28.0
C8_2=27.0
C9_1=28.0
C9_2=27.0
C10_1=28.0
C10_2=27.0
_6MVCF=1.0
Temp=20.1
Pressure=1012.0
RefValMUs6MV=100.0

vals=[C3_1,C3_2,C3_3,C5_1,C5_2]
x=sum([a for a in vals if isinstance(a,float) or isinstance(a,int)])
i=len(vals)
y=x/i

import numpy as np
a=[]
vals=[C1_1,C1_2,C1_3,C7_1,C7_2]
for n in range(0,4):
    if type(vals[n])==float or type(vals[n])==int:
        a.append(vals[n])
b=np.std(a)
x=sum([a for a in vals if isinstance(a,float) or isinstance(a,int)])
i=len(vals)
c=x/i
Reproducibility6MV=b/c
print(a)
print(b)
print(c)
print(Reproducibility6MV)