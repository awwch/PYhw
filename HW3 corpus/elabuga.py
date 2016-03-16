# -*- coding: utf-8 -*-
import urllib.request
import re
import lxml.html
import os
import subprocess

all_links = [] #все найденные ссылки
saved_links = [] # все просмотренные ссылки
fNames = [] #список файлов, содержащих информацию со страниц
#скачиваем главную страницу:
mp = 'http://www.elabuga-rt.ru/'
con = urllib.request.urlopen(mp)
page = con.read()
page = page.decode()
all_links.append(mp)
f = open('main page.txt','w',encoding = 'utf-8')
f.write(page)
saved_links.append(mp)
f.close()
#в файле со скаченной главной страницей ищем ссылки:
f = open('main page.txt','r',encoding = 'utf-8')
f2 = open('all_links.txt','w',encoding = 'utf-8')#файл со всеми ссылками
mainPage = f.readlines()
for line in mainPage:
    m = re.search(r'(http:\/\/\S*)?\/\S*\.html',line)
    if m != None:
        m = 'http://elabuga-rt.ru/' + m.group() + '\n'
        m = m.split('\n')
        for link in m:
            if link not in all_links and link not in saved_links and link != '':
                all_links.append(link)
                f2.write(link + '\n')
f2.close() 
f.close()
#сохраняем статьи, на которые ведут ссылки с главной страницы:
f = open('all_links.txt','r',encoding = 'utf-8') #файл со ссылками с главной страницы
links = f.readlines()
links = list(set(links))
i = 0
folder_names = []#имена папок
#массивы для указания директорий:
years = []
months = []

for element in links:
    if element not in saved_links:#проверяем, проходили ли по данной ссылке
        i+=1
        adress = element
        try:#открываем страницу
            con = urllib.request.urlopen(adress) 
            page = con.read()   
            page = page.decode()
            c = con.getcode()
        except urllib.error.HTTPError:
            continue
        except UnicodeEncodeError:
            continue
        fName = 'fine_page'+str(i) #имена файлов        
        #ищем нужную информацию:
        tree = lxml.html.fromstring(page)
        date = tree.xpath('.//p[@class="under_head"]/text()')
        title = tree.xpath('.//h1/text()')
        text = tree.xpath('.//div[@class="itemFullText ftt"]/*/text()')
        text1 = tree.xpath('.//div[@class="itemFullText"]/*/text()')
        intro = tree.xpath('.//div[@class="itemIntroText int"]/p/text()')
        intro1 = tree.xpath('.//div[@class="itemIntroText"]/p/text()')
        topic = tree.xpath('.//p[@class="under_head"]/a/text()')
        
        p = os.getcwd()
        #создаём названия директорий:
        for d in date:
            y=re.search('\.\d{4}',d)
            if y != None:
                y = y.group()
                y = y.strip('.')
                years.append(y)
                if y not in folder_names:
                    folder_names.append(y)
                    os.mkdir(p+'\\'+y)
                    print(folder_names)                   
                m = re.search('\.\d{2}',d)
                if m != None:
                    m = m.group()
                    m = m.strip('.')
                    months.append(m)
                    if m not in folder_names:
                        folder_names.append(m)
                    #создаём директории и проверяем их наличие:
                    if os.path.exists(p+'\\'+y+'\\'+m) == False:
                        os.mkdir(p+'\\'+y+'\\'+m)
                    if os.path.exists(p+'\\'+y+'\\'+m+'\\'+'fine_text') == False:
                        os.mkdir(p+'\\'+y+'\\'+m+'\\'+'fine_text')
                    if os.path.exists(p+'\\'+y+'\\'+m+'\\'+'mystem_txt') == False:
                        os.mkdir(p+'\\'+y+'\\'+m+'\\'+'mystem_txt')
                    if os.path.exists(p+'\\'+y+'\\'+m+'\\'+'mystem_xml') == False:
                        os.mkdir(p+'\\'+y+'\\'+m+'\\'+'mystem_xml')
                    #сохраняем неразмеченный текст:    
                    os.chdir(p+'\\'+y+'\\'+m+'\\'+'fine_text')                       
                    if date != None and title != None and text != None or text1 != None and intro != None or intro1 !=None:                    
                        f2 = open(fName+'.txt','a',encoding = 'utf-8')
                        f2.write('\n'+'@au'+ ' '+ 'Noname')
                        for t in title:
                            f2.write('\n'+'@ti' + ' ' + t)
                        for d in date:
                            f2.write('\n'+'@da'+ ' '+d)
                        for tp in topic:
                            tp = tp.strip('Печать')
                            f2.write('\n'+'@topic'+ ' ' + tp)
                        f2.write('\n'+'@url'+' '+adress)                    
                        for o in intro:
                            f2.write(o)
                        for o1 in intro1:
                            f2.write(o1)
                        for c in text:
                            f2.write(c)
                        for c1 in text1:
                            f2.write(c1)
                        fNames.append(fName)
                        f2.close() 
                        os.chdir(p)
                        subprocess.call(['D:/mystem.exe','-e UTF-8','-dicg',p+'\\'+y+'\\'+m+'\\'+'fine_text'+'\\'+fName+'.txt', p+'\\'+y+'\\'+m+'\\'+'mystem_txt'+'\\' +fName + '.txt'])
                        subprocess.call(['D:/mystem.exe','-e UTF-8','-dicg','--format','xml',p+'\\'+y+'\\'+m+'\\'+'fine_text'+'\\'+fName+'.txt', p+'\\'+y+'\\'+m+'\\'+'mystem_xml'+'\\' +fName + '.xml'])        
        f.close()        
        f = open('all_links.txt','a',encoding = 'utf-8') #сохраняем ссылки
        try:
            f.write(adress)
        except TypeError:
            continue
        saved_links.append(adress) #записываем ссылки, по которым прошли
        f.close() 
        page = page.split('\n')
        for line in page:
            m = re.search(r'(http:\/\/\S*)?\/\S*\.html',line)
            n = re.search(r'meta name="description"',line)
            if m != None and n != None:
                m = 'http://elabuga-rt.ru/' + m.group() + '\n'
                m = m.split('\n')
                for link in m:
                    if link not in all_links and link != '':
                        all_links.append(link)
                                
#ищем и сохраняем страницы в найденном:
for link in all_links:
    if link not in saved_links:
        adress = link
        try:
            con = urllib.request.urlopen(adress)
            page = con.read()
            page = page.decode()
            c = con.getcode()
        except urllib.error.HTTPError:
            continue
        except UnicodeEncodeError:
            continue
        except UnicodeDecodeError:
            continue
        #if len(all_links)>len(fNames):
        i = len(fNames)+1           
        fName = 'fine_page'+str(i)
        try:
            tree = lxml.html.fromstring(page)
        except ValueError:
            continue
        date = tree.xpath('.//p[@class="under_head"]/text()')
        title = tree.xpath('.//h1/text()')
        text = tree.xpath('.//div[@class="itemFullText ftt"]/*/text()')
        text1 = tree.xpath('.//div[@class="itemFullText"]/*/text()')
        intro = tree.xpath('.//div[@class="itemIntroText int"]/p/text()')
        intro1 = tree.xpath('.//div[@class="itemIntroText"]/p/text()')
        topic = tree.xpath('.//p[@class="under_head"]/a[@*]/text()')           
        p = os.getcwd()       
        for d in date:
            y=re.search('\.\d{4}',d)
            if y != None:
                y = y.group()
                y = y.strip('.')
                if y not in folder_names:
                    folder_names.append(y)
                    os.mkdir(p+'\\'+y)
                    print(folder_names)
                m = re.search('\.\d{2}',d)
                if m != None:
                    m = m.group()
                    m = m.strip('.')
                    if m not in folder_names:
                        folder_names.append(m)
                    if os.path.exists(p+'\\'+y+'\\'+m) == False:
                        os.mkdir(p+'\\'+y+'\\'+m)    
                    if os.path.exists(p+'\\'+y+'\\'+m+'\\'+'fine_text') == False:
                        os.mkdir(p+'\\'+y+'\\'+m+'\\'+'fine_text')
                    if os.path.exists(p+'\\'+y+'\\'+m+'\\'+'mystem_txt') == False:
                        os.mkdir(p+'\\'+y+'\\'+m+'\\'+'mystem_txt')
                    if os.path.exists(p+'\\'+y+'\\'+m+'\\'+'mystem_xml') == False:
                        os.mkdir(p+'\\'+y+'\\'+m+'\\'+'mystem_xml')                        
                    os.chdir(p+'\\'+y+'\\'+m+'\\'+'fine_text')
                    if date != None and title != None and text != None or text1 != None and intro != None or intro1 !=None:            
                        f = open(fName+'.txt','a',encoding = 'utf-8')
                        f.write('\n'+'@au'+ ' '+ 'Noname')
                        for t in title:
                            f.write('\n'+'@ti'+ ' ' + t)
                        for d in date:
                            f.write('\n'+'@da' + ' ' + d)
                        for tp in topic:
                            tp = tp.strip('Печать')
                            f.write('\n'+'@topic'+ ' ' + tp)
                        f.write('\n'+'@url'+' '+adress)
                        for o in intro:
                            f.write(o)
                        for o1 in intro1:
                            f.write(o1)
                        for c in text:
                            f.write(c)
                        for c1 in text1:
                            f.write(c1)
                        f.close()
                    os.chdir(p)
                    subprocess.call(['D:/mystem.exe','-e UTF-8','-dicg',p+'\\'+y+'\\'+m+'\\'+'fine_text'+'\\'+fName+'.txt', p+'\\'+y+'\\'+m+'\\'+'mystem_txt'+'\\' +fName + '.txt'])
                    subprocess.call(['D:/mystem.exe','-e UTF-8','-dicg','--format','xml',p+'\\'+y+'\\'+m+'\\'+'fine_text'+'\\'+fName+'.txt', p+'\\'+y+'\\'+m+'\\'+'mystem_xml'+'\\' +fName + '.xml'])                
            f = open('all_links.txt','a',encoding = 'utf-8')
            try:
                f.write(adress + '\n')
            except TypeError:
                continue
            f.close
            fNames.append(fName)
            page = str(page)
            page = page.split('\n')
            for line in page:
                m = re.search(r'(http:\/\/\S*)?\/\S*\.html',line)
                if m != None:
                    m = 'http://elabuga-rt.ru/' + m.group() + '\n'
                    m = m.split('\n')
                    for link in m:
                        if link not in all_links and link != '':
                            all_links.append(link)
                            m = re.search(r'(http:\/\/\S*)?\/\S*\.html',line)
                            if m != None:
                                m = 'http://elabuga-rt.ru/' + m.group() + '\n'
                                m = m.split('\n')
                                for link in m:
                                    if link not in all_links and link not in saved_links and link != '':
                                        all_links.append(link)
            saved_links.append(adress)