import urllib.request
from bs4 import BeautifulSoup

def open_url(url):
    #box_headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36'}
    #request = urllib.request.Request(url, headers=box_headers)
    #response = urllib.request.urlopen(request)
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def save_url():
    url="http://pare.gq/"
    #url='https://www.douyu.com/g_LOL'
    #url = 'https://www.882su.com/'
    html=open_url(url)
    bs=BeautifulSoup(html,'lxml')
    url_info=bs.find('div',class_='meinv')
    url_a=bs.find_all('a')
    print(url_info)
    print(len(url_a))
    #print(bs.title,bs.title.string.split('_')[0])
    print(bs.title)

if __name__ == "__main__":
    save_url()
    
