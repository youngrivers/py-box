import tornado.ioloop
import tornado.httpserver
import tornado.options
from application import application
from tornado.options import define,options
#tornado.options.define()访问本服务器端口
define('port',default=8080,help='run on the given port',type=int)

def main():
    tornado.options.parse_command_line()  # 解析命令行，此处自动加载
    http_server = tornado.httpserver.HTTPServer(application)  # 单线程服务器
    http_server.listen(options.port)  # 建立了单线程的http服务

    print('服务运行与http://127.0.0.1:%s'%options.port)
    print('ctrl+c退出服务运行')
    tornado.ioloop.IOLoop.instance().start()  # 接收来自http的请求
if __name__=='__main__':
    main()