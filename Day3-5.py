# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:30:31 2020

@author: user
"""

d={}

while True:
    print('--------------------')
    print('1.加法')
    print('2.減法')
    print('3.乘法')
    print('4.除法')
    print('5.離開')
    
    x=input('選擇數字')
    x=int(x)
    if x==1:
        b=input('輸入數字')
        c=input('輸入數字')
        b=int(b)
        c=int(c)
        print('A:',b+c)
    elif x==2:
        b=input('輸入數字')
        c=input('輸入數字')
        b=int(b)
        c=int(c)
        print('A:',b-c)
    elif x==3:
        b=input('輸入數字')
        c=input('輸入數字')
        b=int(b)
        c=int(c)
        print('A:',b*c)
    elif x==4:
        b=input('輸入數字')
        c=input('輸入數字')
        b=int(b)
        c=int(c)
        print('A:',b/c)
    elif x==5:
        break
        
        
        
    