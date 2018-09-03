# -*- coding: utf-8 -*-
"""
Created on Wed May 09 15:26:51 2018

@author: Shubham Dudeja
"""
# -*- coding:utf8 -*-
import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from url_summarizer import FrequencySummarizer
import requests

with open("output.txt") as f:
    text = f.read()
tokens = [t for t in text.split()]
clean_tokens = tokens[:]
 
sr = stopwords.words('english')


for token in tokens:
     if token in stopwords.words('english'):
         t=token.encode('utf-8')
         clean_tokens.remove(t)

freq = nltk.FreqDist(clean_tokens)
 
for key,val in freq.items():
    print (str(key) + ':' + str(val))
    
freq.plot(25,cumulative=False)

