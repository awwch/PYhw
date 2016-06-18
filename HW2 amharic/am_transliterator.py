# -*- coding: utf-8 -*-
import re

pair = {}
all_pairs = []
am_letters = []
sounds = []
cons = []
lines = []

f = open('alph.csv', 'r', encoding='utf-8')
table = f.readlines()
f.close()
row1 = table[0].replace('\n','')
for vows in row1:
    vows = (row1.split('\t'))
    vows.remove('')
table.remove(table[0])
for line in table:
    m = re.match('.{1,2}\t',line)
    if m != None:      
        cons.append((m.group()).replace('\t',''))
        line = line.replace(m.group(),'')
    line = (line.replace('\t','')).replace('\n','')
    lines.append(line) 
for c in cons: 
    for v in vows:
        sounds.append(c+v)
for line in lines:
    while len(line) > 0:
        for letter in line:
            am_letters.append(letter)
            line = line.replace(letter,'')
f = open('translit_alph.csv','w',encoding = 'utf-8')
for i in range(len(sounds)):
    pair = {sounds[i]:am_letters[i]}
    all_pairs.append(pair)
    f.write(sounds[i] + '\t' + am_letters[i] + '\n')
f.close()
    
text = 'አማርኛ'
result = ''

for line in text:    
    for letter in line:        
        i = 0 
        for a in am_letters:
            if letter == ((str(list(all_pairs[i].values()))).strip('[]')).replace("'",''):
                result += ((str(list(all_pairs[i].keys()))).strip('[]')).replace("'",'')
            i += 1    