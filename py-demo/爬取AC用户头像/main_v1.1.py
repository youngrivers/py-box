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
    if url.split('/')[-1]=='avatar.jpg':
        print(name+':没有头像')
    else:
        with open(name,'wb')as f:
            img=url_open(url)
            f.write(img)
        f.close()
        print('下载成功：'+title)
def get_icon():
    all_url=[]
    for i in range(2110):
        x=str(random.random()*100000000)[0:6]
        all_url.append('http://www.acfun.cn/u/'+x+'.aspx#')
    get_time=str(time.localtime().tm_year)+'-'+str(time.localtime().tm_mon)+'-'+str(time.localtime().tm_mday)
    print(get_time)
    name='头像'+get_time
    os.mkdir(name)
    os.chdir(name)
    for i in range(len(all_url)):
        try:
            html=url_open(all_url[i])
            
            bs=BeautifulSoup(html,'lxml')
            title=str(bs.title)[7:-8].split('-')[0]
            #print(title)
            try:
                cover=bs.find('div',class_='cover').find('div')['style']#.find('div',class_="img")
                icon_url=str(cover).split(')')[0][16:-1]
                print('下载中：'+icon_url)
                save_icon(icon_url,title)
            except AttributeError:
                print('找不到用户：'+title)
        except urllib.error.HTTPError:
            print('HTTP Error 404')
        except ValueError:
            print('未知错误！'+all_url[i])
if __name__=='__main__':
    get_icon()
