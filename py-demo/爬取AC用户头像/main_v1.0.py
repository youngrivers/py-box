import urllib.request
import os
import time
import random
from bs4 import BeautifulSoup

def url_open(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36')
    response=urllib.request.urlopen(req)
    html=response.read()
    return html
def save_icon(url,title):
    name=title+'.'+url.split('.')[-1]
    print(name)
    with open(name,'wb')as f:
        img=url_open(url)
        f.write(img)
    f.close()
def get_icon():
    r_6=str(random.random()*10000000)[0:6]#随机得到一个6位数
    url='http://www.acfun.cn/u/'+r_6+'.aspx#'
    get_time=str(time.localtime().tm_year)+'-'+str(time.localtime().tm_mon)+'-'+str(time.localtime().tm_mday)
    print(get_time)
    '''
    name='头像'+get_time
    os.mkdir(name)
    os.chdir(name)
    '''
    try:
        html=url_open(url)
        bs=BeautifulSoup(html,'lxml')
        title=str(bs.title)[7:-8].split('-')[0]
        print(title)
        cover=bs.find('div',class_='cover').find('div')['style']#.find('div',class_="img")
        icon_url=str(cover).split(')')[0][16:-1]
        print(icon_url)
        save_icon(icon_url,title)
    except urllib.error.HTTPError:
        print('HTTP Error 404')

if __name__=='__main__':
    get_icon()
