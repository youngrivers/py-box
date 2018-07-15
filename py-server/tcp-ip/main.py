import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建一个socket
s.connect(('www.sina.com.cn',80))#建立连接
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')#发送数据,返回首页
buffer=[]#接收数据
while True:
    d=s.recv(1024)#1次1K
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)
#print(data)
s.close()#关闭连接
header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('sina.html','wb')as f:
    f.write(html)
