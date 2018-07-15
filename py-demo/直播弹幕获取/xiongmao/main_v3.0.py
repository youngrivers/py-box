import requests
import json
import time
import socket
import re
import multiprocessing
import sqlite3
path_level=re.compile(b'"level":"(.+?)"')
path_name=re.compile(b'"nickName":"(.+?)"')
path_content=re.compile(b'"content":"(.+?)"')

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

r=requests.get('http://www.panda.tv/ajax_chatinfo?roomid=10027')
hehe=json.loads(r.text)

IP_ADDRESS=hehe['data']['chat_addr_list'][0].split(':')[0]
PORT=hehe['data']['chat_addr_list'][0].split(':')[1]

client.connect((IP_ADDRESS,int(PORT)))

def keeplive():
	while True:
		msg=b'\x00\x06\x00\x00'
		print('keep live')
		client.send(msg)
		time.sleep(60)

def start(hehe):
	sqlite3.connect('{}')
	rid = str(hehe['data']['rid']).encode('utf-8')
	appid = str(hehe['data']['appid']).encode('utf-8')
	authtype = str(hehe['data']['authtype']).encode('utf-8')
	sign = str(hehe['data']['sign']).encode('utf-8')
	ts = str(hehe['data']['ts']).encode('utf-8')
	msg = b'u:' + rid + b'@' + appid + b'\nk:1\nt:300\nts:' + ts + b'\nsign:' + sign + b'\nauthtype:' + authtype
	msgLen = len(msg)
	sendMsg = b'\x00\x06\x00\x02'+ int.to_bytes(msgLen, 2, 'big') + msg
	client.sendall(sendMsg)
	message=client.recv(1024)
	print(message)
	while True:
		try:
			hehe=client.recv(1024)
			level=path_level.findall(hehe)[0].decode('unicode_escape')
			name=path_name.findall(hehe)[0].decode('unicode_escape')
			content=path_content.findall(hehe)[0].decode('unicode_escape')
			print("lv:" +level+ ">>>>>>>>" + name + ":" + content)
		except:
			continue

if __name__=="__main__":
	p1=multiprocessing.Process(target=start,args=(hehe,))
	p2=multiprocessing.Process(target=keeplive)
	p1.start()
	p2.start()
