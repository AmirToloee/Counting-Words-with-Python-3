import numpy as np
import pandas as pd
txt = open('words1.txt').read()
words = txt.split()

for x in words:
    count=words.count(x)
    print(x,count)
        
      
s=0
for i in range(len(txt)):
    if txt[i] == " ":
        s=s+1           
print('the number of space: ',s)
print('The nunmber of your word: ',len(words))
