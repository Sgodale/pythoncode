# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:06:05 2021

@author: sgodale
"""
#%%
firstline = ["Happy", "families", "are", "all", "alike;", "every", \
              "unhappy", "family", "is", "unhappy", "in", "its", "own", \
              "way.", "Leo Tolstoy", "Anna Karenina"] 
def problem4_1(wordlist):
    print(wordlist)
    wordlist.sort(key=str.upper)
    print(wordlist)
    #%%