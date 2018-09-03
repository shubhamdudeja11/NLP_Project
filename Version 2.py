# -*- coding: utf-8 -*-
"""
Created on Wed May 09 12:43:08 2018

@author: Shubham Dudeja
"""

from bs4 import BeautifulSoup
from text_summarizer import FrequencySummarizer
import requests

def getTextFromURL(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")
	text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
	return text

def summarizeURL(url, total_pars):
	url_text = getTextFromURL(url).replace(u"Â", u"").replace(u"â", u"")

	fs = FrequencySummarizer()
	final_summary = fs.summarize(url_text.replace("\n"," "), total_pars)
	return " ".join(final_summary)

message=("Enter the Url seperated by space\n ")
print(message)
url_list = map(str,raw_input().split())

# prepairing Summary List
final_summary_list=[]

#Printing Final Summary of Each URL
for url in url_list:
    print url
    final_summary = summarizeURL(url, 5)
    final_summary_list.append(final_summary)
    print final_summary_list

#Saving List In text files

u=len(final_summary_list)

for index,each in enumerate(final_summary_list):
    each.encode('utf8')
    with open('Output'+str(index+1)+'.txt','w+') as output:
        output.write(each)
        each.encode('ascii','ignore')
