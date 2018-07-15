import urllib.request
from bs4 import BeautifulSoup

url='https://tieba.baidu.com/p/5653680140'
url=input('请输入网页：例如(https://tieba.baidu.com/p/5653680140)---')

req=urllib.request.urlopen(url)
response=req.read()
html=response.decode('utf-8')
bs=BeautifulSoup(response,'lxml')
get_author=bs.find_all('div',class_='d_author')
get_all=bs.find_all('div',class_='d_post_content j_d_post_content ')
all_txt=[]
all_author=[]
title=str(bs.title)[7:-8].split('【')[0]
name=title+'.txt'
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
for data in get_author:
    author=data.get_text()#encode('utf-8')
    author=author.splitlines(False)#删除换行
    new_author=[]
    for data in author:#删除列表中的空格
        if data==''or data==' ':
            #print('删除列表中的空格')
            pass
        else:
            new_author.append(data)
    new_author=new_author[0]
    all_author.append(new_author)
print(all_author)
with open(name,'w')as f:
    f.write('贴名：'+title+'\r\n')
    for i in range(len(all_author)):
        f.write(str(i+1)+'楼-'+all_author[i]+'：'+all_txt[i]+'\r\n')
    
f.close()
