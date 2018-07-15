import socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#创建一个socket
s.bind(('127.0.0.1',9999))
#s.listen(5)
print('Waiting for connection...')
while True:
    #sock,addr=s.accept()
    #t=threading.Thread(target=tcplink, args=(sock, addr))
    #t.start()
    data,addr=s.recvfrom(1024)
    print('Recevied from %s:%s'%addr)
    reply='Hello,%s'%data.decode('utf-8')
    s.sendto(reply.encode('utf-8'),addr)

def tcplink(sock,addr):
    print('Accept new connection form %s:%s...'%addr)
    sock.send(b'welcome!')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(('hello,%s'%data.decode('utf-8')).encode('utf-8'))
        sock.close()
        print('Connection from %s:%s closed'%addr)