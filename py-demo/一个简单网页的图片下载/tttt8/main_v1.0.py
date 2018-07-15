import urllib.request
import time
import os
from bs4 import BeautifulSoup
def dir_img():
    get_time=str(time.localtime().tm_year)+'-'+str(time.localtime().tm_mon)+'-'+str(time.localtime().tm_mday)
    print(get_time)
    name='图片'+get_time
    try:
        os.mkdir(name)
    except FileExistsError:
        print('文件已存在时，无法创建该文件'+name)
    os.chdir(name)
def open_url(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400')
    response=urllib.request.urlopen(req)
    html=response.read()
    return html
def save_img(path,post_content):#下载图片
    for content in post_content:
        img_url=content['src']
        img=open_url(img_url)
        filename=img_url.split('/')[-1]
        #print(filename+'---'+img_url)
        print(filename)
        with open(filename,'wb') as f:
            f.write(img)
        f.close
    os.chdir(path)
def page_url(path,pageList):#获取网页内图片地址
    for i in range(1,int(pageList)+1):
        page_url='http://www.tttt8.club/zatu/l-p-vision-no-03/'+str(i)
        bs=BeautifulSoup(open_url(page_url),'lxml')
        post_content=bs.find(id='post_content').find_all('img')
        print('---'+page_url+'---')
        save_img(path,post_content)
def content_img(content):#进入标题网页
    for i in range(len(content)):
        title=content[i].find('a').get_text().strip()
        img_url=content[i].find('a')['href']
        img_url_j=open_url(img_url)
        bs_j=BeautifulSoup(img_url_j,'lxml')
        pageList=bs_j.find('div',class_='pagelist').find_all('a')[-1].get_text()
        try:
            os.mkdir(title)#创建图片文件夹
        except FileExistsError:
            print('文件已存在时，无法创建该文件。')
        os.chdir(title)
        path=os.getcwd()
        page_url(path,pageList)
def get_img():
    url='http://www.tttt8.club/category/zatu/'
    html=open_url(url)
    bs=BeautifulSoup(html,'lxml')
    pages=bs.find('div',class_='pagination').find_all('a')[-1]
    page=pages['href'].split('/')[-1]
    print(page)
    dir_img()
    #for i in range(1,int(page)+1):
    for i in range(2,3):
        url='http://www.tttt8.club/category/zatu/page/'+str(i)
        print('strat download---'+url)
        html=open_url(url)
        bs_i=BeautifulSoup(html,'lxml')
        content=bs_i.find(id='post_container').find_all('h2')
        #imgs=bs_i.find(id='content-main').find_all('img')
        content_img(content)
if __name__=='__main__':
    get_img()
