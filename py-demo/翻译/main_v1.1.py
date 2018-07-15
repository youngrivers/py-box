import urllib.request#引入模块
import urllib.parse#解析模块
import json
import time

while True:
    content=input("请输入要翻译的内容(输入q!退出程序)：")
    if content=='q!':
        break
    elif content=='':
        content='我爱你'

    head={}
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36'

    url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"#打开网页
    data={}
    data['i']=content
    data['from']='AUTO'
    data['to']='AUTO'
    data['smartresult']='dict'
    data['client']='fanyideskweb'
    data['salt']='1524149755032'
    data['sign']='eb6439dc2b9db1ad5646895dcde6d9e9'
    data['doctype']='json'
    data['version']='2.1'
    data['keyfrom']='fanyi.web'
    data['action']='FY_BY_CLICKBUTTION'
    data['typoResult']='false'
    data=urllib.parse.urlencode(data).encode('utf-8')#编码转换

    req=urllib.request.Request(url,data,head)#引入访问方式
    #req.add_header(key,value)#key=User-Agent

    response=urllib.request.urlopen(req)
    html=response.read().decode('utf-8')

    target=json.loads(html)
    print("翻译结果为：%s"%(target[trans_result][5][0]["dst"]))
    time.sleep(5)
