import numpy as np
import pandas as pd
txt = open('words1.txt').read()
words = txt.split()
print(words)
s=0
for i in range(len(txt)):
    if txt[i] == " ":
        s=s+1           
print('the number of space: ',s)
print('The nunmber of your word: ',len(words))







'''
def count_wandds(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)
print(count_wandds("words1.txt"))




       

import csv
import string

translator = str.maketrans('', '', string.punctuation)


word_count = {}
text = open('words1.txt').read()

words = text.split()

for word in words:
    word = word.translate(translator).lower()
    count = word_count.get(word, 0)
    print(count)
    count += 1
    word_count[word] = count

word_count_list = sorted(word_count, key=word_count.get, reverse=True)
for word in word_count_list[:10]:
    print(word, word_count[word])

output_file = open('words.csv', 'w')
writer = csv.writer(output_file)
writer.writerow(['word', 'count'])
for word in word_count_list:
    writer.writerow([word, word_count[word]])

'''
