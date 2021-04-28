# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 19:20:52 2021

@author: dario
"""

from nltk import bigrams

with open("C:/Users/dario/Downloads/Shakespear.txt") as file:
    f = file.read()

special_char = [";",":","!","*",",",".","-","_","\n","'","?"]

for i in special_char:
    f = f.replace(i,"")

f = f.lower().strip().split()

bigramList = list(bigrams(f))

bigramDic= {}

for bigram in bigramList:
    if bigram in bigramDic:
        bigramDic[bigram] += 1 
    else:
        bigramDic[bigram] = 1

sortedDic= dict(sorted(bigramDic.items(), key=lambda kv:kv[1], reverse=True))

with open ("bigrams.txt", "w") as outf:
    for key, value in list(sortedDic.items()):
        (a,b) = key
        outf.write(a + " " + b + "\t" + str(value) + "\n")
    
