# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 02:25:51 2021

@author: sgodale
"""

#%%
def problem3_3(month,day,year):
    mon=("January","February","March","April","May","June","July","August","September","October","November","December")
    for i in range(1,13):
        if month==i:
            date=mon[i-1]+" "+str(day)+", "+str(year)
            print(date)
        #%%