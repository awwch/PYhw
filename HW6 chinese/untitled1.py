# -*- coding: utf-8 -*-

import re
import string
import lxml.html

f = open('stal.xml','r', encoding = 'utf-8')
page = f.read()
f.close()
tree = lxml.html.fromstring(page)
sentences = tree.xpath('.//se//text()')
f = open('cedict_ts.u8','r',encoding = 'utf-8')
text = f.readlines()
f.close()

def chains(sentences):
    result = []
    chains = []
    definitions = []
    i= 0
    for sentence in sentences:
        for line in text:        
            if str(sentence) == '\n':
                continue
            sentence = str(sentence).strip(string.punctuation)
            s = re.findall(sentence,line)
            if s != None and str(sentence) not in result:
                result.append(str(sentence))
            else:
                while len(sentence) != 0: 
                    sentence = sentence.strip(sentence[-1])
                    if sentence == '':
                        continue
                    s = re.findall(sentence,line)
                    if s != None and sentence not in result:
                        result.append(sentence)
    for r in result:
        while len(r) > 0:
            r = r.strip(r[-1])
            s = re.findall(r,text[i])
            if s != None and r not in chains:
                chains.append(r)            
    for chain in chains:
        for line in text:
            if chain in line and chain not in definitions:
                definitions.append(chain)                
    return(definitions)

def find_in_dict(definitions):
    voc = []
    for definition in definitions:
        for line in text:
            if definition in line and {definition:line} not in voc:
                voc.append({definition:line})
    return(voc)

definitions = chains(sentences)
full_definitions = find_in_dict(definitions)