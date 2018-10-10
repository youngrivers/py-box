import requests

post = "https://api.douban.com/v2/movie/top250"

data = {}
data['start'] = '0'  # 数据开始项
data['count'] = '20'
req = requests.get(post, data)

#print(req.json()['total'])
movie_list = req.json()['subjects']

for i in movie_list:
    print(i['title']+'---'+str(i['rating']['average']))
