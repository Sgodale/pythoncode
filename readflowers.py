# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 13:05:42 2021

@author: sgodale
"""
#%%
import csv
def problem3_7(filename,flower):
    infile=open(filename)
    for row in csv.reader(infile):
        if row[0]==flower:
            print(row[1])
        
    infile.close()
    #%%