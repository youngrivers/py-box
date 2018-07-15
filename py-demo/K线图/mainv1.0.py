import time
import urllib.request
import json
get_time=str(time.time()*1000).split('.')[0]
url='http://img1.money.126.net/data/hs/kline/day/history/2018/0000001.json?callback=loadStockData&t='+get_time;
response=urllib.request.urlopen(url)
html=response.read().decode('utf-8')
#data=json.JSONDecoder().decode(html)
#data=json.loads(html)
data=dict(str(html)[14:-2])
#s_data=data[loadStockData]
