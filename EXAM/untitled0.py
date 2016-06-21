# -*- coding: utf-8 -*-

f = open('source_post1950_wordcount.csv','r',encoding = 'utf-8')
table = f.readlines()
f.close()
table.remove(table[0])

def str_key (_dict):
    key = (str(list(_dict.keys())).strip('[]')).replace("'",'')
    return(key)
def str_value (_dict): 
    value = (str(list(_dict.values())).strip('[]')).replace("'",'')
    return(value)
def contain_counter(table,number):                
    elements = []
    el_counter = []
    i = 0
    for line in table:
        l = line.split(';')
        if l[number] not in elements:
            elements.append(l[number])
    for element in elements:
        for line in table:
            if element in line:
                i += 1
        el_count = {element:i}
        el_counter.append(el_count)
    return(el_counter)
new_table = []    
for line in table:
    line = line.split(';')
    if line[-2] != 'none':
        count = int(line[-2])
        line = [line,count]
        new_table.append(line)
        if count > 70000 and count < 100000:
            new_table.append([line,count/2])
        if count > 100000:
            new_table.append([line,count/3])
            
sp_counter = contain_counter(table,6)
dec_counter = contain_counter(table,5)