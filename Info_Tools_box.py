import urllib.request as req
import re
ifile1 = open(r'C:\Users\lza\Desktop\lanzou_total_tools.txt', 'r', encoding='UTF-8')
encoding='UTF-8'
data1 = ifile1.readlines()
ifile1.close()

ifile2 = open(r'C:\Users\lza\Desktop\lanzou_total_books.txt', 'r', encoding='UTF-8')
encoding='UTF-8'
data2 = ifile2.readlines()
ifile2.close()

ifile3 = open(r'C:\Users\lza\Desktop\lanzou_total_music.txt', 'r', encoding='UTF-8')
encoding='UTF-8'
data3 = ifile3.readlines()
ifile3.close()

leng1 = len(data1)
leng2 = len(data2)
leng3 = len(data3)
leng = max(leng1, leng2, leng3)

jfile = open(r'C:\Users\lza\Desktop\lanzou_total_file(wanted).txt', 'w+', encoding='UTF-8')
dic = {}
dic['tools'] = {}
dic['books'] = {}
dic['music'] = {}
for idx1 in range(8, leng-3, 3):
    for idx2 in range(2):
        idx = idx1+ idx2
        if idx >= leng1-3:
            name1 = ''
            adr1 = ''
        elif data1[idx].count('<') != 0:
            name1 = data1[idx].split('<')[0]
            adr1 = data1[idx].split('<')[1].split('>')[0]
            dic['tools'][name1] = adr1
        if idx >= leng2-3:
            name2 = ''
            adr2 = ''
        elif data2[idx].count('<') != 0:
            name2 = data2[idx].split('<')[0]
            adr2 = data2[idx].split('<')[1].split('>')[0]
            dic['books'][name2] = adr2
        if idx >= leng3-3:
            name3 = ''
            adr3 = ''
        elif data3[idx].count('<') != 0:
            name3 = data3[idx].split('<')[0]
            adr3 = data3[idx].split('<')[1].split('>')[0]
            dic['music'][name3] = adr3

    jfile.write('<tr> \
    <td><a href = "%s" target="blank">%s</a></td> \
    <td><a href = "%s" target="blank">%s</a></td> \
    <td><a href = "%s" target="blank">%s</a></td> \
    </tr>\n' % (adr1, name1, adr2, name2, adr3, name3 ))
jfile.close()
