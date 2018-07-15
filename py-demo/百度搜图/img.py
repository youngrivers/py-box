import urllib.request
import urllib.parse
import re
import os
from bs4 import BeautifulSoup

x=input("请输入你要搜索的图片：")
if x=='':
    x='处女膜'
else:
    pass
data={}
data['tn']='baiduimage'
data['ipn']='r'
data['ct']='201326592'
data['cl']='2'
data['lm']='-1'
data['datat']='-1'
data['fm']='redatault'
data['fr']=''
data['dataf']='1'
data['fmq']='1523859336640_R'
data['pv']=''
data['ic']='0'
data['nc']='1'
data['z']=''
data['datae']='1'
data['datahowtab']='0'
data['fb']='0'
data['width']=''
data['height']=''
data['face']='0'
data['idatatype']='2'
data['ie']='utf-8'
data['word']=x
data=urllib.parse.urlencode(data)#转换
#data=urllib.parse.urlencode(data).encode('utf-8')

def get_html(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36')
    response=urllib.request.urlopen(req)
    html=response.read()
    #html=html.decode('utf-8')
    return html

def get_img():
    html=get_html(url).decode('utf-8')
'''with open('x.txt','w')as f:
    for data in html:
        f.write(data)

f.close()'''


def download_img():
    url='https://image.baidu.com/search/index?'+str(data)
    html=get_html(url)
    bs=BeautifulSoup(html,'lxml')
    all_img=bs.find('div',id='imgContainer')#.find_all('img')
    floder='图片'
    print(all_img)
    #os.mkdir(x+floder)
    #os.chdir(x+floder)

if __name__=='__main__':
    download_img()
