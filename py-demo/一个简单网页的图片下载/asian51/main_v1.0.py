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
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36')
    response=urllib.request.urlopen(req)
    html=response.read()
    return html
def save_img(title,img_url):
    img=open_url(img_url)
    filename=img_url.split('/')[-1]
    print(title+'---'+filename+'---'+img_url)
    with open(filename,'wb') as f:
        try:
            f.write(img)
        except TypeError:
            print('TypeError')
    f.close
def get_img():
    url='http://www.asian51.com/category/lolita/page/1'
    html=open_url(url)
    bs=BeautifulSoup(html,'lxml')
    pages=bs.find('div',class_='wp-pagenavi').find_all('a')[-1]
    page=pages['href'].split('/')[-1]
    print(page)
    dir_img()
    for i in range(1,int(page)+1):
    #for i in range(1):
        url='http://www.asian51.com/category/lolita/page/'+str(i)
        print('strat download---'+url)
        html=open_url(url)
        bs_i=BeautifulSoup(html,'lxml')
        content=bs_i.find(id='content-main').find_all('h2')
        imgs=bs_i.find(id='content-main').find_all('img')
        for j in range(len(content)):
            title=content[j].get_text().strip()
            img_url=imgs[j]['src']
            save_img(title,img_url)
if __name__=='__main__':
    get_img()