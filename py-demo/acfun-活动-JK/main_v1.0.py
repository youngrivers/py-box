import urllib.request
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver

def url_open(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36')
    response=urllib.request.urlopen(req)
    html=response.read()
    return html
def download_img():
    jk_url=[]
    url='http://www.acfun.cn/v/as21'
    browser = webdriver.Firefox()
    browser.get(url)#获取网页
    #js='var q=document.documentElement.scrollTop=10000'
    js='window.scrollTo(0,document.body.scrollHeight)'
    for t in range(10):
        time.sleep(t)
        browser.execute_script(js)#将页面滚动条拖到底部
    all_url=browser.find_elements_by_css_selector('.article-list a')
    #all_url=browser.find_elements_by_css_selector('.atc-content div')#['href']
    #all_url=bs.find('div',class_='article-list')#.find_all('div',class_='article-item clearfix')
    #print(len(all_url),all_url[0].get_attribute('data-id'))
    for i in range(0,len(all_url)):
        if i%2==0:
            jk_url.append(all_url[i].get_attribute('href'))
    print(jk_url)
    browser.close()
    name='JK制服大作战'
    try:
        os.mkdir(name)
    except FileExistsError:
        print('文件已存在时，无法创建该文件'+name)
    os.chdir(name)
    for url in jk_url:
        html=url_open(url)
        bs=BeautifulSoup(html,'lxml')
        try:
            up_name=bs.find('a',class_='upname').get_text()
            all_imgs=bs.find('div',class_='article-content').find_all('img')#['src']
            img_addrs=[]
            for j in all_imgs:
                img_addrs.append(j['src'])
            print('开始下载---'+up_name)
            try:
                os.mkdir(up_name)
                os.chdir(up_name)
                save_img(up_name,img_addrs)
            except FileExistsError:
                print('文件已存在时，无法创建该文件'+up_name)
        except AttributeError:
            print('NoneType object has no attribute get_text')

def save_img(up_name,img_addrs):
    for each in img_addrs:
        filename=each.split('/')[-1]
        with open(filename,'wb')as f:
            img=url_open(each)
            f.write(img)
    print('下载已完成:'+up_name)
    os.chdir('G:\\Users\\youngrivers\\Desktop\\PY Test\\acfun-活动-JK\\'+'JK制服大作战')
if __name__=='__main__':
    download_img()
