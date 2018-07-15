import time
import requests
import sqlite3
hehedada=dict()
index=0
f=open("bilibili_danmu.txt",'a')
room_id=str(input('plz enter the roomid'))
while True:
	index=index+1
	if index==2000:
		hehedada=dict()
		index=0
	url='http://live.bilibili.com/ajax/msg'
	form={
			'roomid': room_id,
		}
	data=requests.post(url,data=form)
	import json
	heheda=json.loads(data.text,encoding='utf-8')
	for i in heheda['data']['room']:
		if i['nickname'] in hehedada.keys():
			if i['text'] in hehedada[i['nickname']]:
				continue
			else:
				print(i['nickname']+":"+i['text'])
				f.write(i['nickname']+":"+i['text']+"\n")
				hehedada[i['nickname']].append(i['text'])
		else:
			hehedada[i['nickname']] = list()

	time.sleep(1)
