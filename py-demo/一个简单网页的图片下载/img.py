import urllib.request
import urllib.parse
import re
import os
#import BeautifulSoup
#import bs4
from bs4 import BeautifulSoup


def url_open(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36')
    response=urllib.request.urlopen(req)
    html=response.read()
    return html

def save_img(floder,img_addrs):
    for each in img_addrs:
        filename=each.split('/')[-1]
        with open(filename,'wb')as f:
            img=url_open(each)
            f.write(img)

def download_img():
    url='http://www.46ek.com/html/article/85569.html'
    html=url_open(url)
    bs=BeautifulSoup(html,'lxml')#解析页面
    all_img=bs.find_all('img')#获取所有图片
    img_addrs=[]
    #img_addrs.append(all_img[0]['src'])
    for i in range(len(all_img)-1):
        i-=0
        img_addrs.append(all_img[i]['src'])

    floder=str(bs.title)[7:-8].split('】')[1]#截取页面标题
    os.mkdir(floder)
    os.chdir(floder)
    for j in range(len(img_addrs)):
        j-=0
        save_img(floder,img_addrs)
        
if __name__=='__main__':
    download_img()
