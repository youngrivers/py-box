MVC模式：（model,view,controller）
--
基本框架

- **handlers**
python程序,处理前端的请求，操作数据库
- **methods**
读写数据库的函数，被handlers使用
- **statics**
静态文件，css,js,图片
- **templates**
html文件
- **url.py**
设置网站的目录结构
- **application.py**
对网站系统的基本配置，建立网站的请求处理集合
- **server.py**
将tornado服务器运行起来，包括前面的对象属性设置