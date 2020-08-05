# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:26:04 2020

@author: AE401
"""

def w(total,p):
    p=int(p)
    average=(total/p)
    return(average)

def z(p,ss,higest):
    for k in range(p):
        if ss[k]>higest:
            higest=ss[k-1]
            b=ns[k-1]
    return higest,b

def j(p,ss,lowest):
    for u in range(p):
        if ss[u]>lowest:
            lowest=ss[u]
            c=ns[u]
    return lowest,c
    
k=[]  
u=[]
ns=[]
ss=[]

total=0
average=0
higest=0
lowest=100

p=input("請輸入人數")
p=int(p)

for k in range(p):
    s=input("請輸入分數")
    s=int
    ss.append(s)
    n=input("請輸入名字")
    ns.append(n)

print("average is",w(total,p))

print("the higest score is",z(p,ss,higest))

print("the lowest score is",j(p,ss,lowest))











