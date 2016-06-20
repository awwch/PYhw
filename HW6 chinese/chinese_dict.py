# -*- coding: utf-8 -*-

import re
import lxml.html

f = open('stal.xml','r', encoding = 'utf-8')
page = f.read()
f.close()
tree = lxml.html.fromstring(page)
sentences = tree.xpath('.//se//text()')
f = open('cedict_ts.u8','r',encoding = 'utf-8')
text = f.readlines()
f.close()

def dict_parser(text):
    words = []
    transcriptions = []
    definitions = []
    for line in text:
        m = re.search('\s(\S*)\s\[',line)
        if m != None:
            sovr = (m.group().strip(' \['))
            words.append(sovr)
            m = re.search('\[.*\]',line)
            if m != None:
                transcriptions.append({sovr:m.group()})
            m = re.search('\/(.*)\/',line)
            if m != None:
                definitions.append({sovr:m.group()})
    return(words,transcriptions,definitions)

words,transcriptions,definitions = dict_parser(text)
