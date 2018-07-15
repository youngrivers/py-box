
#-*- coding:utf-8 -*-

import urllib.request
import sys
import unicodedata
from bs4 import BeautifulSoup

url='https://tieba.baidu.com/p/5660210537'

req=urllib.request.urlopen(url)
response=req.read()
html=response.decode('utf-8')

bs=BeautifulSoup(response,'lxml')#.prettify()
#unicodedata.name(bs)
get_all=bs.find_all('div',class_='d_post_content j_d_post_content ')
all_txt=[]
for data in get_all:
    answer=data.get_text()#encode('utf-8')
    answer=answer.strip()#删除左右空格
    try:#跳过不能识别的
        print(answer)
        all_txt.append(answer)
    except UnicodeEncodeError:
        print('UnicodeEncodeError')
        all_txt.append('字符不能识别!')
print(all_txt)
title=str(bs.title)[7:-8].split('【')[0]

with open('main.txt','w')as f:
    f.write('贴名：'+title+'\r\n')
    i=0  
    for t in all_txt:
        i=i+1
        f.write(str(i)+'楼：'+t+'\r\n')
f.close()
#w_txt()
