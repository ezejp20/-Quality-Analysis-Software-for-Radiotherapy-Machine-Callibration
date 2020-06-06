# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 12:12:00 2018

@author: ellen.punter
"""
import leafData
leafDoseValuesJaw=leafData("T:\Medical Physics\mp-rtphys\Development\Software\QATrack Pimilco\Temp Files - Pimlico\LA1\LA1 03-02-2017\Y1CN.prs")
leafDoseValuesMLC=leafData("T:\Medical Physics\mp-rtphys\Development\Software\QATrack Pimilco\Temp Files - Pimlico\LA1\LA1 03-02-2017\Y1CM.prs")
leafErrors=[(leafDoseValuesJaw-leafDoseValuesMLC)/0.2 for x in leafDoseValuesJaw]