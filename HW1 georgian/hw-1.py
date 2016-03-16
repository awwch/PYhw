f = open('new.csv', 'r', encoding='utf-8')
f1 = open('alph.txt', 'w', encoding = 'utf-8')
letters = {} 
for line in f:
    line = line.replace('\ufeff', '')
    word = line.split() 
    geoletter = word[0] 
    letters[geoletter]=word[2]
f1.write(str(letters))
f1.close()
f.close()

transtext = open('song.txt', 'r', encoding = 'utf-8')
final = open('transtext.txt', 'w', encoding = 'utf-8')
for line in transtext: 
    for letter in line: 
        if letter in letters: 
            final.write(letters[letter]) 
        else: 
            final.write(letter) 
final.close() 
transtext.close()
