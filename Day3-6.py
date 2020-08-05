# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:16:29 2020

@author: user
"""

d={}

print('歡迎進入系統!')
while True:
    print('1. 建立詞彙')
    print('2. 列出所有單字')
    print('3. 英翻中')
    print('4. 中翻英')
    print('5. 測驗學習結果')
    print('6. 離開系統')
    b=int(input('選擇一項系統'))
    
    if b==1:
        x=0
        while x==0:
            a=input('請輸入中文')
            c=input('請輸入其英文')
            d[a]=c
            r=int(input('按0退出,按1繼續'))
            if r==0:
               x=x+1
    elif b==2:
          print(d)
          x=0
    elif b==3:
          x=0
          while x==0:
              a=input('請輸入英文')
              for key,value in dict.items():
                  c=d[a]
                  print[a]
                  
              else:
                  print('查無此資料')
                 
                  r=int(input('按0退出,按1繼續'))
                  if r==0:
                    x=x+1
    elif b==4:
        x=0
        a=input('請輸入中文')
        while x==0:
             a=input('請輸入英文')
             for key in dict.keys():
                 c=d[a]
                 
             else:
                 print('查無此資料')
                
                 r=int(input('按0退出,按1繼續'))
                 if r==0:
                     x=x+1
    elif b==5:
        for key,value in dict.items():
            print(key)
            f=input('此英文的意思?')
            if f==value:
                print('good job!!!')
            if f!=value:
                print('wrong!')
    elif b==6:
        break
                  
                  
            
          
          
      
              
        