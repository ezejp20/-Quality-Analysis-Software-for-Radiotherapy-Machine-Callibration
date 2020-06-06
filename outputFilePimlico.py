# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 10:33:49 2019

@author: ellen.punter
"""

#from django.utils import timezone
from datetime import date
i=1
msg = "\t%d;\t0.00;\t0.00;\t0.00;\t0.00;\t0.00;\t%d;\t%d"%(i, 
date = date.today()
date=str(date)
date2=date.replace("-","_")
print(date2)
fname = "T:/Medical Physics/mp-rtphys/Development/Software/QATrack Pimilco/results_%s.txt" % date2
open(fname, "w").write(msg)

