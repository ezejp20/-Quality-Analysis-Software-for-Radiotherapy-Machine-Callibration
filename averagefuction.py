# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:06:11 2019

@author: ellen.punter
"""

vals=[1,2,"a",1,3]
x=sum([a for a in vals if isinstance(a,float) or isinstance(a,int)])
i=0
for a in vals:
    if type(a)==float or type(a)==int:
        i=i+1.0
c=x/i