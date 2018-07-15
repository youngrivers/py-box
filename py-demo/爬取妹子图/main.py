import os
import re
import urllib.request
import requests
from bs4 import BeautifulSoup
class imgs():
    def url_open(url):
        req=urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36')
        response=urllib.request.urlopen(req)
        if response.getcode()==200:
            html=response.read()
        else:
            pass
        s=requests.session()
        s.get(url)
        s.cookies.clear()#删除cookies
        return html

    def request(self,url): ##这个函数获取网页的response 然后返回
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36',
                'referer':''#伪造一个访问来源 "http://www.mzitu.com/100260/2"
            }
            content = requests.get(url, headers=headers)
            return content
        
    def main(self,url):
        html=self.request(url)
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a',href=re.compile('[0~9]'))
        for a in all_a:
            title=a.get_text()
            print('开始下载：',title)
            path = str(title).replace("?", '_')
            self.mkdir(path)#调用
            href=a['href']+'/'
            self.get_img(href)
            
        #os.chdir(os.pardir)# 递归调用后切记返回上一层目录
        '''for b in hr:
            html=url_open(b)
            all_bs=BeautifulSoup(html,'lxml').find('div',class_='content').find('img')['src']
            save_img(all_bs)'''
        
    def get_img(self,href):#获取图片的地址
        html=self.request(href)
        max_img=BeautifulSoup(html.text,'lxml').find('div',class_='pagenavi').find_all('span')[-2].get_text()
        print(max_img)
        for page in range(1,int(max_img)+1):
            page_url=href+str(page)
            self.get_html(page_url)
        
    def get_html(self,page_url):#真实url
        html=self.request(page_url)
        all_bs=BeautifulSoup(html.text,'lxml').find('div',class_='content').find('img')['src']
        self.save_img(all_bs)

    def save_img(self,all_bs):#保存图片
        name=all_bs.split('/')[-1]
        with open(name,'wb')as f:
            image=self.request(all_bs)
            f.write(image.content)
        f.close()
        
    def mkdir(self,path):#创建文件夹
        path = path.strip()
        #os.getcwd()#返回工作目录
        #os.chdir(os.pardir)
        #title='妹子图'
        isExists=os.path.exists(path)
        if not isExists:#判断当前目录存在文件夹
            print('创建文件夹：',path)
            os.makedirs(path)
            os.chdir(path)
            return True
        else:
            print('文件夹已经存在了！')
            return False
def main_all():
    url='http://www.mzitu.com/all/'   
    Imgs=imgs()
    Imgs.main(url) 
main_all()
