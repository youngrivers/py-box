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

def save_img(floder,img_addrs,x):
    for each in img_addrs:
        filename=each.split('/')[-1]
        with open(filename,'wb')as f:
            try:
                img=url_open(each)
                f.write(img)
            except urllib.error.HTTPError:
                print('Not Found')
        f.close()
    print('下载已完成：'+floder)
    #os.chdir('./')返回上一级
    os.chdir('G:\\Users\\youngrivers\\Desktop\\PY Test\\一个简单网页的图片下载\\'+'图片'+x)

def download_img():
    url='https://www.6856f.com/Html/63/'
    #url='https://www.1344w.com/Html/63/'
    #url='https://www.1344w.com/Html/63/13372.html'
    html=url_open(url)
    bs=BeautifulSoup(html,'lxml')#解析页面
    print('------'+str(bs.title)[7:-8]+'------')
    all_a=bs.find('div',class_='box list channel').find_all('a')[1:20]
    get_time=str(time.localtime().tm_year)+'-'+str(time.localtime().tm_mon)+'-'+str(time.localtime().tm_mday)
    print(get_time)
    name='图片'+get_time
    try:
        os.mkdir(name)
    except FileExistsError:
        print('文件已存在时，无法创建该文件'+name)
    os.chdir(name)
    for a in all_a:
        xml=a['href'].split('/')[-1]
        html=url+xml
        print('开始下载:'+html)
        get_img(html,get_time)
    
def get_img(url,x):

    #all_img=bs.find_all('img')#获取所有图片
    html=url_open(url)
    bs=BeautifulSoup(html,'lxml')
    all_img=bs.find('div',class_='content').find_all('img')
    img_addrs=[]
    #img_addrs.append(all_img[0]['src'])
    for i in range(len(all_img)-1):
        i-=0
        img_addrs.append(all_img[i]['src'])

    floder=str(bs.title)[7:-8].split('-')[0]#截取页面标题
    try:
        os.mkdir(floder)
        os.chdir(floder)
    #for j in range(len(img_addrs)):
        #j-=0
        save_img(floder,img_addrs,x)
    except FileExistsError:
        print('文件已存在时，无法创建该文件'+floder)
if __name__=='__main__':
    download_img()
