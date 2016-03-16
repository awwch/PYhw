# -*- coding: utf-8 -*-

import os
import re

def wiki_extr(path):
    WEpath = path+r'\WikiExtractor.py'+' '+path+'\\fjwiki-20160305-pages-meta-current.xml -b 500K -o extracted'
    return(WEpath)

def fine_text(path):
    f = open(path+'\\extracted\\AA\\wiki_00','r',encoding = 'utf-8')
    f2 = open('fj_wiki.xml','w',encoding = 'utf-8')
    text = f.readlines()
    for line in text:
        m = re.match('^<.*>',line)
        n = re.match('^</.*>',line)
        if m != None:
            m = m.group(0)
            line = line.replace(m,'')
        if n != None:
            n = n.group(0)
            line = line.replace(n,'')
        f2.write(line)
    f.close()
    f2.close()
    return(f,f2)

os.system(wiki_extr(os.getcwd())) 
fine_text(os.getcwd())
