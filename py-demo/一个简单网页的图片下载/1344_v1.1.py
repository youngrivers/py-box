import urllib.request
import urllib.parse
import re
import os
import time
#import BeautifulSoup
#import bs4
from bs4 import BeautifulSoup

def url_open(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36')
    response=urllib.request.urlopen(req)
    html=response.read()
    return html

def download_img():
    url='https://www.1328g.com/Html/84/'
    #url='https://www.1344w.com/Html/63/13372.html'
    html=url_open(url)
    bs=BeautifulSoup(html,'lxml')#解析页面
    print('------'+str(bs.title)[7:-8]+'------')
    all_a=bs.find('div',class_='box list channel').find_all('a')[0:30]
    get_time=str(time.localtime().tm_year)+'-'+str(time.localtime().tm_mon)+'-'+str(time.localtime().tm_mday)
    print(get_time)
    name='小说'+get_time
    os.mkdir(name)
    os.chdir(name)
    for a in all_a:
        xml=a['href'].split('/')[-1]
        html=url+xml
        print('开始下载:'+html)
        get_book(html)
    
def get_book(url):
    html=url_open(url)
    bs=BeautifulSoup(html,'lxml')
    all_word=bs.find('div',class_='content').find_all('font')#.get_text()
    all_w=str(all_word).replace('<br/>','\n')[32:-8]
    #book_name=str(bs.tltle)[7:-8].split('-')[0]+'.txt'
    book_name=str(bs.title)[7:-8].replace('?','_')+'.txt'
    try:
        with open(book_name,'w')as f:
            f.write(all_w)
        f.close()
    except FileExistsError:
        print('文件已存在时，无法创建该文件'+book_name)
    except UnicodeEncodeError:
        print('非法字符！')
if __name__=='__main__':
    download_img()
