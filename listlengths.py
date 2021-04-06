# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 03:01:17 2021

@author: sgodale
"""
#%%
newEngland = ["Maine","New Hampshire","Vermont", "Rhode Island", 
"Massachusetts","Connecticut"]

def problem2_3(ne):
    leng=len(ne)
    for i in range(0,leng):
        print(ne[i],"has",len(ne[i]),"letters.")
        
        #%%