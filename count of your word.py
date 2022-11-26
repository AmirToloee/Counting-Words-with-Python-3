import numpy as np
import pandas as pd
import csv
import string
#read your file and open it
txt = open('words1.txt').read()
#all words convert to capital words
txt=txt.upper()
#split your words in list
words = txt.split()
data = {}
for x in words:
        print(x)
        #add your words in list to your dict 
        data[x]=x
        #count your words by count func and store it
        count=words.count(x)
        #add thats count in your dic
        #dic data remove the duplicate in your sets
        data[x]=count  
print(data)
s=0
for i in range(len(txt)):
    if txt[i] == " ":
        s=s+1           
print('the number of space: ',s)
print('The nunmber of your word: ',len(words))
        

