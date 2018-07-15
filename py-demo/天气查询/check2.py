
import urllib.request
import json
import pickle
city_file=open("main_city.pkl","rb")#导入
city=pickle.load(city_file)

password=input("请输入城市：")
name1=city[password]
file1=urllib.request.urlopen("http://www.weather.com.cn/data/cityinfo/"+name1+".html")#打开网页
weatherHTML=file1.read().decode("utf-8")#读入打开的URL
#weatherJSON=json.JSONDecoder().decode(weatherHTML)#创建JSON
weatherINFO=weatherJSON["weatherinfo"]#打印信息
print("城市：",weatherINFO["city"])
print("天气：",weatherINFO["weather"])
print("最高温度：",weatherINFO["temp2"])
print("最低温度：",weatherINFO["temp1"])
