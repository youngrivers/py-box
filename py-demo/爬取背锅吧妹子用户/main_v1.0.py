
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def open_url(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36')
    reponse=urllib.request.urlopen(req)
    html=reponse.read()
    return html
def get_user():#获取锅巴的用户>=7级
    user=[]
    pn=65510
    for i in range(1,pn):
        page=i
        url='http://tieba.baidu.com/bawu2/platform/listMemberInfo?word=%B1%B3%B9%F8&pn='+str(i)
        html=open_url(url)
        bs=BeautifulSoup(html,'lxml')
        user_member=bs.find('div',class_='forum_info_section member_wrap clearfix bawu-info').find_all('div',class_='name_wrap')
        for i in range(len(user_member)):
            user_a=user_member[i].find('a').get_text()
            user_span=user_member[i].find('span')['class']
            level=user_span[1][-1]
            if int(level)>=7:
                #user_name=user_a.encode('utf-8')
                data={}
                data['un']=user_a
                data['fr']='home'
                data=urllib.parse.urlencode(data)
                url_name='http://tieba.baidu.com/home/main?'+data
                html_name=open_url(url_name)
                bs_name=BeautifulSoup(html_name,'lxml')
                user_info=bs_name.find('div',class_='userinfo_userdata')
                try:
                    user_info_span=user_info.find('span')['class']
                    user_sex=user_info_span[1].split('_')[-1]
                    if user_sex=='female':
                        print('---找到一个！---',page)
                        print(user_a,level)
                        print(url_name)
                        print(user_sex)
                        user.append(user_a)
                except AttributeError:
                    print("'NoneType' object has no attribute 'find'")
    return user
def open_user():
    user=get_user()
    name='锅巴小姐姐.txt'
    with open(name,'w')as f:
        f.write(user)
    f.close()
if __name__=='__main__':
    open_user()
