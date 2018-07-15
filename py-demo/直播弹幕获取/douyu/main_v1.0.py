import urllib.request
import requests
import socket
import multiprocessing#多进程
from bs4 import BeautifulSoup
from danmu import DanMuClient
import time
from time import localtime
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostbyname("openbarrage.douyutv.com")
port=8601
client.connect((host,port))
import re
path=re.compile(b'txt@=(.+?)/cid@')
uid_path=re.compile(b'nn@=(.+?)/txt@')
level_path=re.compile(b'level@=([1-9][0-9]?)/egtt@')

def open_url(url):
    req=urllib.request.urlopen(url)
    response=req.read()
def get_url(url):
    html=open_url(url)
    bs=BeautifulSoup(html,'lxml')
    all_chat=bs.find('div',class_="chat-cont-wrap").find_all('li')
#dm=DanMuClient(url)
def get_name(room_id):
    url='https://www.douyu.com/'+room_id
    r=requests.get(url)
    bs=BeautifulSoup(r.text,'lxml')
    all_chat=bs.find('a',class_='zb-name').string

def start(room_id):
    msg='type@=loginreq/usename@=rieuse/password@=douyu/roomid@={}/\0',format(room_id)
    
def keeplive():
    while True:
        msg='type@=keeplive/tick@=' + str(int(time.time())) + '/\x00'
        print('init live')
        sendmsg(msg)
        time.sleep(15)
def sendmsg(x):
    msg=x.encode('utf-8')
if __name__=='__main__':
    room_id=input('请输入直播间ID：')
    if room_id=='':
        room_id='pangpang'
    p1=multiprocessing.Process(target=start,args=(room_id))
    p2=multiprocessing.Process(target=keeplive)
    p1.start()
    p2.start()
