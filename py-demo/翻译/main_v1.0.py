
import urllib.request#引入模块
import urllib.parse#解析模块
import json
import time

while True:
    content=input("请输入要翻译的内容(输入q!退出程序)：")
    if content=='q!':
        break
    if content=='':
        content='好'
    head={}
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36'

    #url="http://fanyi.baidu.com/v2transapi"#打开网页
    url='http://fanyi.baidu.com/sug'
    data={}
    '''
    data['from']='zh'
    data['to']='en'
    data['query']=content
    data['transtype']='realtime'
    data['simple_means_flag']='3'
    data['sign']='538559.840846'
    data['token']='a95002e110cfa1a8f2676c4b30b0b14b'
    '''
    data['kw']=content
    data=urllib.parse.urlencode(data).encode('utf-8')#编码转换

    req=urllib.request.Request(url,data,head)#引入访问方式
    #req.add_header(key,value)#key=User-Agent

    response=urllib.request.urlopen(req)
    html=response.read().decode('utf-8')

    target=json.loads(html)
    print("翻译结果为：%s"%(target['data'][0]['v'])+'\n')
    try:
        print("更多：%s"%(target['data'][1]['v']))
    except IndexError:
        print('IndexError')
    time.sleep(5)
