import numpy as np
import pandas as pd
import csv
import string
#thats your file
txt = open('words1.txt').read()
words = txt.split()
print(words)
data = {}
for x in words:
        print(x)
        data[x]=x        
        count=words.count(x)
        data[x]=count  
print(data)  
        

