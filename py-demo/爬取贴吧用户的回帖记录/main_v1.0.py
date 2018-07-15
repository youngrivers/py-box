import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
user=input('请输入你要查询的用户名：')
if user=='':
    user='入狱身先zl'
num=2
data={}
data['ie']='utf-8'
data['kw']=''
data['qw']=''
data['rn']='10'
data['un']=user
#data['only_thread']=''
data['sm']='1'
#data['sd']=''
#data['ed']=''
#data['pn']=num
data=urllib.parse.urlencode(data)#.encode('utf-8')
def url_open(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36')
    response=urllib.request.urlopen(req)
    html=response.read()
    return html
def get_post():
    url='http://tieba.baidu.com/f/search/ures?'+str(data)
    html=url_open(url)
    bs=BeautifulSoup(html,'lxml')
    all_post=bs.find('div',class_='s_post_list')
    all_p=all_post.find_all('div',class_='p_content')
    all_data=all_post.find_all('font',class_='p_green p_date')
    name=user+'.txt'
    with open(name,'w')as f:
        for i in range(len(all_p)):
            p_i=all_p[i].get_text()
            d_i=all_data[i].get_text()
            f.write(d_i+'---'+p_i+'\n')
    f.close
if __name__=='__main__':
    get_post()
