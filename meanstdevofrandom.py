# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:26:44 2021

@author: sgodale
"""

#%%
import statistics
import random
numList = []
random.seed(150)
for i in range(0,25):
    numList.append(round(100*random.random(),1))
def problem4_2(ran_list):
 m1=statistics.mean(ran_list)
 sd=statistics.stdev(ran_list)
 print(m1)
 print(sd)
 
#%%