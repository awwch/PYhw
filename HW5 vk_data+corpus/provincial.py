# -*- coding: utf-8 -*-

import vk
import time
import os
#import subprocess

def folder_maker(post):
    os.chdir('C:\Users\Ania\Desktop\вшэ\PYhw\HW5 vk_data+corpus\posts')
    os.mkdir(str(i))
    os.chdir(str(os.getcwd()) + '\\' + str(i))
    f = open('post.txt','w',encoding = 'utf-8')
    f.write(post)
    #subprocess.call(['D:/mystem.exe','-e UTF-8','-dicg',str(os.getcwd())+'\\'+'post.txt', str(os.getcwd())+'\\'+'parsed.txt'])
    os.chdir('C:\Users\Ania\Desktop\вшэ\PYhw\HW5 vk_data+corpus\posts')
    return(os.getcwd())
    
session = vk.Session(access_token='012eb3834a7edaafc3997ff62c2ce65d165510668bf8cf4f600df1f100c07af541eed2cfe0a8d9532d106')
vkapi = vk.API(session)

uid = []
info = []
names = []
sex = []
bdate = []
occupation = []
personal = []
walls = []
posts = []

get_users = vkapi.users.search(hometown = 'Териберка', count = 1000)
get_users.remove(get_users[0])
for _object in get_users:
    uid.append(_object.get('uid'))
       
for _id in uid:
    info.append(vkapi.users.get(user_ids = _id,fields = ['sex', 'bdate','home_town','occupation','relation','personal']))    
    walls.append(vkapi.wall.get(owner_id = _id, owners_only = 1, filter = 'owner', count = 100))    
    time.sleep(2)
i = 0  
for wall in walls:
    wall.remove(wall[0])
    for wall[i] in wall:
        if type(wall[i].get('text')) != 'NoneType' and len(wall[i].get('text')) > 0:
            posts.append(wall[i].get('text'))    
            i += 1
    i = 0
    
for _object in info:
    for fields in _object:
        names.append(fields.get('first_name') + ' ' + fields.get('last_name'))
        sex.append(str(fields.get('sex')))
        bdate.append(fields.get('bdate'))
        occupation.append(fields.get('occupation'))
        personal.append(fields.get('personal'))

oc_type = []
oc_name = []
oc_id = []
all_ocupations = []
for o in occupation:
    if o == None:
        oc_type.append('empty')
        oc_name.append('empty')
        oc_id.append('empty')
    else:
        oc_type.append(o.get('type'))
        oc_name.append(o.get('name'))
        oc_id.append(o.get('id'))
    if o != None:
        if (str(o.get('id')) + '\t' + o.get('name')) not in all_ocupations and str(o.get('id')) != 'None':
            all_ocupations.append(str(o.get('id')) + '\t' + o.get('name'))

langs = []
all_langs = []
for p in personal:
    if p == None:
        langs.append('empty')
    else:
        try:
            langs.append(p.get('langs'))
        except AttributeError:
            langs.append('empty')                
for l in langs:
    if l != 'empty' and l != None:
        for i in range(len(l)):
            if l[i] not in all_langs:
                all_langs.append(l[i])

f = open('vk_database.csv','w',encoding = 'utf-8')
for i in range(len(names)):
    f.write(str(uid[i]) + '\t' + names[i] + '\t' + str(bdate[i]) + '\t' + oc_type[i] + '\t' + sex[i] + '\n')
f.close()

f = open('sex.csv','w',encoding = 'utf-8')
f.write('1' + '\t' + 'f' + '\n' + '2' + '\t' + 'm')
f.close()

f = open('occupation.csv','w',encoding = 'utf-8')
for i in range(len(all_ocupations)):
    f.write(all_ocupations[i] + '\n')
f.close()

f = open('langs.csv','w',encoding = 'utf-8')
i = 1
for lang in all_langs:
    f.write(str(i) + '\t' + lang + '\n')
    i += 1
f.close()

i = 1    
for post in posts:
    if len(post) > 0:
        folder_maker(post)    
        i+=1
os.chdir('C:\Users\Ania\Desktop\вшэ\PYhw\HW5 vk_data+corpus')
