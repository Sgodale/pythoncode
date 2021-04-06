# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 19:38:23 2021

@author: sgodale
"""

#%%
import math
def problem2_7():
    a=input("Enter length of side one:")
    a1=float(a)
    b=input("Enter length of side two:")
    b1=float(b)
    c=input("Enter length of side three:")
    c1=float(c)
    s=(a1+b1+c1)/2
    area=math.sqrt(s*(s-a1)*(s-b1)*(s-c1))
    print("Area of a triangle with sides",a1,b1,c1,"is",area)
    #%%