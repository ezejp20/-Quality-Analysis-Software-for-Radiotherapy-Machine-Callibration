# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 11:30:25 2018

@author: ellen.punter
"""

settings =	{
  "Tolerances": {
          "Investigate": {
                  "MLC": 0.7, "X": 0.7, "YD": 0.7, "Optical":1.5},
          "Not Clinical": {"MLC": 1, "X": 1, "YD": 1, "Optical":2}},
  "Minor Settings MLC":{"Adj Ratio":12, "Vol Effect":20},
  "Major Offset/Gain Settings": {
          "Offset Adj Ratio":{"MLC":12, "X":35,"YD":30},
          "Gain Adj Ratio":{"MLC":25, "X":75,"YD":54}},
  "IC Profiler Properties":{
          "1":{
                  "Serial No.":5699436, "SDD": 100.0, "Offset X": 0.0, "Offset Y": 0.3},
          "2":{
                  "Serial No.":6904824, "SDD": 100.0, "Offset X": 0.0, "Offset Y": -0.2}
          },
   "Gain/OffsetCalculation Weighting": {
           "Gain Weights":{"(5)-15": 0, "5-(7.5)":0, "(15)-7.5": 1 },
           "Offset Weights": {"(5)-15": 1, "5-(7.5)":1, "(15)-7.5": 1 }
           },
   "Penumbra Model Paraneters": {
           "Edge Percent":{"MLC":50, "X": 50, "Y":56},
           "Algorithm": "Square Root",
           "6MV":{
                   "20-80% Width":{
                           "10x10":{"MLC":5.5,"X": 3.5, "Y":5.5},
                           "30x30":{"MLC":5.5,"X": 4, "Y":6.5},
                           "+7.5":{"MLC":6, "Y":6}
                           },
                   "Transmission/Scatter":{
                           "10x10":{"MLC":5,"X": 4.5, "Y":8},
                           "30x30":{"MLC":5.5,"X": 5, "Y":8.5},
                           "+7.5":{"MLC":6, "Y":8.5},}},
         "10MV":{
                   "20-80% Width":{
                           "10x10":{"MLC":5.5,"X": 3.5, "Y":5.5},
                           "30x30":{"MLC":5.5,"X": 4, "Y":6.5}
                           },
                   "Transmission/Scatter":{
                           "10x10":{"MLC":5,"X": 4.5, "Y":8},
                           "30x30":{"MLC":5.5,"X": 5, "Y":8.5}
                           }
                   }
                                  }
            }
   
  