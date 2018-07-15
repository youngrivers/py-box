#coding:utf-8
'''
import tornado.httpserver#实现客户端和服务器端的互通
import tornado.ioloop#实现非阻塞socket循环
import tornado.options#命令行解析模块
import tornado.web#提供web框架和异步功能

from tornado.options import define,options
#tornado.options.define()访问本服务器端口
define('port',default=8000,help='run on the given port',type=int)
class IndexHandler(tornado.web.RequestHandler):#接收客户端的请求并处理
    def get(self):
        greeting=self.get_argument('greeting','Hello')#得到url中传递的参数
        self.write(greeting+', welcome you to read :www.xxx.com')#向客户端返回信息
if __name__=='__main__':
    tornado.options.parse_command_line()#解析命令行，此处自动加载
    app=tornado.web.Application(handlers=[(r"/",IndexHandler)])#类实例化
    http_server=tornado.httpserver.HTTPServer(app)#单线程服务器
    http_server.listen(options.port)#建立了单线程的http服务
    tornado.ioloop.IOLoop.instance().start()#接收来自http的请求
'''