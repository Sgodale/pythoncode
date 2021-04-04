# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 20:14:16 2021

@author: shital
"""
import random

print('Guess the number')
c=0
for i in range(0,10):
    ip=input('Enter a number between 1 to 5:')
    #c=0
    rn=random.randint(1,5)
    if rn==int(ip):
        print('Yay! you win.collect one point')
        c=c+1;
    else:
         print('nope! Wrong guess! correct answer is',rn)
print('Game Over! Total points earned:',c)
    
    
