import tornado.web
import os
from url import url
settings=dict(#约定了模块和静态文件的路径
    template_path=os.path.join(os.path.dirname(__file__),'templates'),
    static_path=os.path.join(os.path.dirname(__file__),'statics')
)
application=tornado.web.Application(#请求处理集合对象
    handlers=url,
    **settings
)