# nlp_url_summarizer
### URL articles text summarizer using Web Crawling and NLP (written in Python)

## Getting started
### 1. Open command line (Terminal on Mac)
- pip install beautifulsoup4
- pip install -U nltk
- pip install -U numpy
- pip install -U setuptools
- pip install -U sumy

### 2. Open Python command line
- import nltk
- nltk.download("stopwords")

### 3. Run the process and enter any URL
- python url_summarizer.py

### 4. Changes Made
Folowing are the additions made:
1) Summary Obtained is stored in a txt file
2) The output.txt file is read by a python script that plots the most frequent words in a bar graph format with associated count.

### 5. Uses
The graph plot can be used to analyse the the article summary that can be used to check for the content quality and there is a scope of implementing it for Fake NEWS detection by comparing data of two NEWS sources having same article.
