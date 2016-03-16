# -*- coding: utf-8 -*-

import re
import string
from collections import Counter

def tokenizer(text_file):
    tokens = []
    f = open(text_file,'r',encoding = 'utf-8')
    for line in f:
        tokens += line.split()
    for i in range(len(tokens)):
        tokens[i] = (tokens[i].strip(string.punctuation)).lower()
        d = re.match('(\d*\W*)*',tokens[i])
        if d != None:
            d = d.group(0)
            tokens[i] = tokens[i].replace(d,'')
    for token in tokens:
        if token == '':
            tokens.remove(token)
    return(tokens)

tokens = tokenizer('fj_wiki.xml')
f = open('freq_dict.tsv','w',encoding = 'utf-8')
all_freq = Counter(tokens).most_common()   
for freq in all_freq:
    f.write(freq[0] + '\t' + str(freq[-1]) + '\n')
f.close()