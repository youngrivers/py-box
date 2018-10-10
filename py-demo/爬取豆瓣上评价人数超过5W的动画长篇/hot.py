import requests

post = "https://api.douban.com/v2/movie/in_theaters"
city='深圳'
data={}
data['start']='0'#数据开始项
data['count']='20'
data['city']=city
req=requests.get(post,data)

#print(req.json()['total'])
movie_list = req.json()['subjects']

for i in movie_list:
    print(i['title']+'---'+str(i['rating']['average']))
