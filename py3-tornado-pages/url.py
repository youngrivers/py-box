
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')#utf-8，兼容汉字
from handlers.index import IndexHandler#引用handlers里的文件index.py的类IndexHandler
#IndexHandler.__anthor__('ss')
url=[#列出所有目录和对应的处理类
    (r'/',IndexHandler)
]
