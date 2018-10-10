import urllib.request
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://movie.douban.com/tag/#/?sort=T&range=0,10&tags=%E5%8A%A8%E7%94%BB'
def open_url(url):
    #html=urllib.request(url)
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36',
        'referer': ''
    }
    html=requests.get(url,headers=headers)
    return html

html=open_url(url)
bs=BeautifulSoup(html.text,'lxml')
movie_list=bs.find('div',class_='list-wp')#.find_all('a')
print(str(bs.title))
print(movie_list)
#for i in movie_list:
#    print(i['span'])