import urllib.request
import urllib.parse
import re
import time
from bs4 import BeautifulSoup
def url_open(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36')
    response=urllib.request.urlopen(req)
    html=response.read()
    return html
def download_book():
    book_name='制服下的诱惑'+'.txt'
    with open(book_name,'w')as f:
        for i in range(80):
            j=i+7375629
            url='http://www.skywx.com/yuedu_63582_'+str(j)+'.html'
            print('下载：',url)
            #url='http://www.skywx.com/yuedu_63582_7375630.html'
            html=url_open(url)
            bs=BeautifulSoup(html,'lxml')#解析页面
            print('------'+str(bs.title)[7:-8]+'------')
            all_a=bs.find('div',class_='book_middle_text').find('div',id='booktext')#.get_text()
            get_time=str(time.localtime().tm_year)+'-'+str(time.localtime().tm_mon)+'-'+str(time.localtime().tm_mday)
            #print(get_time)
            all_txt=str(all_a)[19:-6].replace('\n','').replace('<br/>','\n').replace('\xa0',' ').replace('&nbsp;',' ')
            print(all_txt)
            try:
                f.write(str(bs.title)[7:-8]+'\n')
                f.write(all_txt)
            except NameError:#UnicodeEncodeError:
                print('UnicodeEncodeError')
    f.close()
if __name__=='__main__':
    download_book()
