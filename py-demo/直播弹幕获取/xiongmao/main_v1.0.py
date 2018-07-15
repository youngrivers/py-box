
import urllib.request
from bs4 import BeautifulSoup


url=input('请输入直播间地址：')
if url=='':
    url='https://www.panda.tv/20641'
else:
    pass

req=urllib.request.Request(url)
req.add_header('user-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36')
req=urllib.request.urlopen(req)
print(req.info())

response=req.read()
html=response.decode('utf-8')
bs=BeautifulSoup(response,'lxml')
chat_wd=bs.find('div',class_="room-chat-box")
#all_chat=chat_wd.find_all('li',class_='room-chat-item room-chat-message room-chat-special-  ')
room_title=str(bs.title)[7:-8].split('_')[0]
print(room_title)
