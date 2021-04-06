# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 01:53:16 2021

@author: sgodale
"""

#%%
def problem3_1(filename):
    infile=open(filename)
    sum=0
    for line in infile:
        sum=sum+len(line)
        print(line,end="")
    print()
    print()
    print("There are",sum,"letters in the file.")   
    infile.close()
    #%%