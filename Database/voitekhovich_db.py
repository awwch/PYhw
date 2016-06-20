# -*- coding: utf-8 -*-

import pymysql

connection = pymysql.connect(host = 'localhost', user = 'guest1', password = 'n76Je4 = wx6H', db = 'guest1_voitekhovich', charset = 'utf8mb4',cursorclass = pymysql.cursors.DictCursor )
cursor = connection.cursor()

f = open('vk_database.csv','r',encoding = 'utf-8')
all_data = f.readlines() 
f.close()
f = open('langs','r',encoding = 'utf-8')
langs = f.readlines() 
f.close()
f = open('sex','r',encoding = 'utf-8')
sex = f.readlines() 
f.close()
f = open('occupation','r',encoding = 'utf-8')
oc = f.readlines() 
f.close()

try:
    cursor.execute('CREATE TABLE `users` (`id` INT(15),`name` VARCHAR(255),`bdate` DATE,`occupation` VARCHAR(255),`sex` VARCHAR(255)) DEFAULT CHARSET=utf8;')
    cursor.execute('CREATE TABLE `sex`(`id` INT(15),`sex` VARCHAR(255)) DEFAULT CHARSET=utf8;')
    cursor.execute('CREATE TABLE `occupation`(`id` INT(15),`oc_name` VARCHAR(255)) DEFAULT CHARSET=utf8;')
    cursor.execute('CREATE TABLE `langs`(`id` INT(15),`lang` VARCHAR(255)) DEFAULT CHARSET=utf8;')
    for line in all_data:
        line = line.split('\t')
        _id = line[0]
        name = line[1]
        bdate = line[2]
        occupation = line[3] 
        sex = line[4]
        cursor.execute('INSERT INTO `users` (`id`,`name`,`bdate`,`occupation`,`sex`,`langs`) VALUES ('+ _id, name, bdate, occupation, sex +');')
    for line in sex:
        line.split('\t')
        _id = line[0]
        name = line[1]
        cursor.execute('INSERT INTO `sex` (`id`,`sex`) VALUES ('+_id, name+');')
    for line in oc:
        line.split('\t')
        _id = line[0]		
        name = line[1]
        cursor.execute('INSERT INTO `occupation` (`id`,`oc_name`) VALUES ('+ _id, name +');')   
    for line in langs:
        line = line.split('\t')
        lang_id = line[0]
        lang = line[1]
        cursor.execute('INSERT INTO `langs` (`id`,`lang`) VALUES('+ lang_id, lang +');')

finally:
    connection.commit()
    cursor.close()
    connection.close()