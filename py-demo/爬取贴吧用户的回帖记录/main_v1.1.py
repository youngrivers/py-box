
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
user=input('请输入你要查询的用户名：')
if user=='':
    user='入狱身先zl'
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
    print('---'+url)
    html=url_open(url)
    bs=BeautifulSoup(html,'lxml')
    all_page=bs.find('div',class_='pager pager-search').find_all('a')
    #txt_p(all_p,all_data)
    try:
        page_num=all_page[-1]['href'].split('=')[-1]
        url_r=all_page[-1]['href'].split('pn=')[0]
        name=user+'.txt'
        with open(name,'w')as f:
            for i in range(int(page_num)):
                i=i+1
                url_i='http://tieba.baidu.com'+url_r+'pn='+str(i)
                print('开始下载：'+'pn='+str(i))
                html=url_open(url_i)
                bs=BeautifulSoup(html,'lxml')
                try:
                    all_post=bs.find('div',class_='s_post_list')
                    all_p=all_post.find_all('div',class_='p_content')
                    all_data=all_post.find_all('font',class_='p_green p_date')
                    #指针回到末尾f.seek(0,2)
                    #txt_p(all_p,all_data)#打印一页记录
                    for i in range(len(all_p)):
                        p_i=all_p[i].get_text().replace('?','-').replace('','_')
                        d_i=all_data[i].get_text()
                        try:
                            f.write(d_i+'---'+p_i+'\n')
                        except UnicodeEncodeError:
                            print('~gbk~ codec can_t encode character')
                except AttributeError:
                    print('AttributeError')
        f.close
    except IndexError:
        print('该用户已隐藏回帖记录')
if __name__=='__main__':
    get_post()
