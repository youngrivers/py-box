import urllib.request#引入模块
import urllib.parse#解析模块
import urllib
import requests

head={}
head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36'
url='http://fanyi.baidu.com/gettts?lan=en&text=Well&spd=3&source=web'
req=urllib.request.Request(url)#引入访问方式
response=urllib.request.urlopen(req)
html=response.read()#.decode('utf-8')
name=response.info()['Content-Disposition'].split('=')[-1]

#r=requests.get(html,stream=True)
with open(name,'w')as code:
    code.write(str(html))
code.close()
with open('x.txt','w')as f:
    f.write(str(html))

f.close()
