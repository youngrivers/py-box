import urllib.request
import os
from bs4 import BeautifulSoup

def open_url(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36')
    response=urllib.request.urlopen(req)
    html=response.read()
    return html

def save_voice(title,url_voice):
    #urllib.urlretrieve('http://music.baidu.com/data/music/file?link=&song_id=1128053', 'C:/BingYu.mp3')
    print('开始下载：'+url_voice)
    voice_name=title+'.mp3'
    data=open_url(url_voice)
    with open(voice_name,'wb')as f:
        f.write(data)
    print('下载完成---'+title)

def get_voice(url):
    html=open_url(url)
    bs=BeautifulSoup(html,'lxml')
    title=str(bs.title)[7:-8].split('-')[0]
    url_voice=bs.find('audio')['src']
    save_voice(title,url_voice)

def download_voices():
    url='http://www.256br.com/html/part/53.html'
    html=open_url(url)#获取主页
    bs=BeautifulSoup(html,'lxml')
    name=str(bs.title)[7:-8].split('_')[0]
    name='录音精品'
    try:
        os.mkdir(name)
    except FileExistsError:
        print('已创建文件夹---'+name)
        os.chdir(name)
    page=bs.find('div',class_='page').find_all('a')[-1]['href'].split('_')[-1].split('.')[0]
    print('共发现页数---'+page)
    url_list=bs.find('div',class_='list').find_all('td',class_='listtitletxt')
    print('找到项目数：---'+str(len(url_list)-6))
    for i in range(6,len(url_list)):
        voices_url=url_list[i].find_all('a')[1]['href']
        voices_url_ture='http://www.256br.com'+str(voices_url)
        print('进入页面---'+voices_url_ture)
        get_voice(voices_url_ture)

if __name__=='__main__':
    #name='录音精品'
    #os.chdir(name)
    download_voices()
