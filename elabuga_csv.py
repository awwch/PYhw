# -*- coding: utf-8 -*-
import os
import re
table = open('elabuga.csv','w',encoding = 'utf-8')
table.write('path;author;sex;birthday;header;created;sphere;genre_fi;type;topic;chronotop;style;audience_age;audience_level;audience_size;source;publication;publisher;publ_year;medium;country;region;language\n')
sources = []
headers = []
dates = []
years = []
topics = [] 
paths = []
for root, dirs, files in os.walk(".", topdown=True):
    for name in files:
        f_name = os.path.join(root, name)
        path = f_name
        paths.append(path)
for path in paths:
    if path  == '.\elabuga_csv.py' or path == '.\elabuga.csv' or path == '.\\all_links.txt' or path == '.\\elabuga.csv' or path == '.\\elabuga.py' or path == '.\\elabuga_csv.py' or path == '.\\main page.txt':
        paths.remove(path)

for path in paths:        
    f = open(path,'r',encoding = 'utf-8')
    doc = f.readlines()
    
    table.write(path+';')
    author = 'Noname'
    table.write(author+';')
    sex = ''
    table.write(sex+';')
    birthday = ''
    table.write(birthday+';')
    
    for line in doc:
        header = re.search('^@ti.*$',line)
        created = re.search('(\d{2}\.){2}\d{4} \d{2}:\d{2}',line)
        if header != None:
            header = str(header.group())
            header = header.strip('@ti')
        else:
            header = ''
        if header != '' and header not in headers:
            table.write(header+';')
            headers.append(header)
        
        if created != None:
            created = str(created.group())
            publ_year = re.search('\d{4}',created)
            if publ_year != None:
                publ_year = str(publ_year.group())
                publ_year = publ_year.strip('\n')
                publ_year = publ_year.strip('\t')
                publ_year = publ_year.strip('')
                publ_year = publ_year.strip(' ')
                publ_year = publ_year.strip(';')
            else:
                publ_year = ''
            if publ_year != '' and publ_year not in years:
                years.append(publ_year)
        else:
            created = ''
        if created != '' and created not in dates:
            created = created.strip('@da')
            created = created.strip('\n')
            created = created.strip('\t')
            created = created.strip('')
            created = created.strip(' ')
            created = created.strip(';')
            table.write(created+';')
            dates.append(created)
    
    for header in headers:
        #table.write(header+';')
        headers.remove(header)
    for created in dates:
        #table.write(created+';')
        dates.remove(created)
    #table.write(''+';')    
    
    sphere = 'публицистика'
    table.write(sphere+';')
    genre_fi = ''
    table.write(genre_fi+';')
    t = ''
    table.write(t+';')
    
    for line in doc:
        topic = re.search('^@topic.*$',line)
        if topic != None:
            topic = str(topic.group())
            topic = topic.strip('@topic')
            topic = topic.strip('\n')
            topic = topic.strip(' ')
        else:
            topic = ''
            
        if topic!='' and topic not in topics:
            topics.append(topic)
            
    for topic in topics:
        table.write(topic+';')
        topics.remove(topic)   
    
    chronotop = ''
    table.write(chronotop + ';')
    style = 'нейтральный'
    table.write(style+';')
    audience_age = 'н-возраст'
    table.write(audience_age+';')
    audience_level = 'н-уровень'
    table.write(audience_level+';')
    audience_size = 'городская'
    table.write(audience_size+';')
    
    for line in doc:
        source = re.search('^@url.*\n',line)
        if source != None:
            source = str(source.group())
            source = source.strip('@url')
            source = source.strip('\n')
        else:
            source = ''
        if source!= '' and source not in sources:
            sources.append(source)
            
    for source in sources:
        table.write(source+';')
        sources.remove(source)
     
    publication = 'Новая Кама'
    table.write(publication+';')
    publisher = ''
    table.write(publisher + ';')
    
    for year in years:
        table.write(year+';')
        years.remove(year)
    
    medium = 'газета'
    table.write(medium+';')
    country = 'Россия'
    table.write(country+';')
    region = 'Республика Татарстан'
    table.write(region+';')
    language = 'ru'
    table.write(language+'\n')
    
table.close()
