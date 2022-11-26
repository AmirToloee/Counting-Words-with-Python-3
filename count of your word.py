import numpy as np
import pandas as pd
import csv
import string
txt = open('words1.txt').read()
txt=txt.upper()
words = txt.split()
data = {}
for x in words:
        print(x)
        data[x]=x        
        count=words.count(x)
        data[x]=count  
print(data)
mylist=list(data)
print(data)
s=0
for i in range(len(txt)):
    if txt[i] == " ":
        s=s+1           
print('the number of space: ',s)
print('The nunmber of your word: ',len(words))
        

