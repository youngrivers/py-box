import os
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
url_s=input('请输入网页：例如(https://tieba.baidu.com/p/5653680140)---')
all_author=[]
def get_user(url):#根据输入的网页获得回复的用户名
    req=urllib.request.urlopen(url)
    response=req.read()
    html=response.decode('utf-8')
    bs=BeautifulSoup(response,'lxml')
    get_author=bs.find_all('div',class_='d_author')
    get_all=bs.find_all('div',class_='d_post_content j_d_post_content ')
    title=str(bs.title)[7:-8].split('【')[0]
    name=title+'_c'+'.txt'
    for data in get_author:
        author=data.get_text()#encode('utf-8')
        author=author.splitlines(False)#删除换行
        new_author=[]
        for data in author:#删除列表中的空格
            if data==''or data==' ':
                #print('删除列表中的空格')
                pass
            else:
                new_author.append(data)
        new_author=new_author[0]
        all_author.append(new_author)
    os.mkdir(title)
    os.chdir(title)
    return all_author
def put_user():
    get_user(url_s)
    for i in all_author:
        user=i
        make(user)
def make(user):
    data={}
    if user=='':
        data['un']='黑十字会v'
    else:
        data['un']=user
    name=data['un']+'.txt'
    data['fr']='home'
    data=urllib.parse.urlencode(data)
    url='http://tieba.baidu.com/home/main?'+data
    req=urllib.request.urlopen(url)
    response=req.read()
    bs=BeautifulSoup(response,'lxml')
    def main(bs):
        try:
            ihome=bs.find('div',class_='ihome_forum_group ihome_section clearfix')
            def tiezi():#帖子内容
                u_word=bs.find('div',class_='content_wrap').find_all('a',locate="thread_author#ihome_v1")
                u_time=bs.find('div',class_='content_wrap').find_all('div',class_='n_post_time')
                all_word=[]
                for i in range(len(u_word)):
                    word=u_word[i].get_text()
                    try:
                        print(word)
                        all_word.append(word)
                    except UnicodeEncodeError:
                        print('UnicodeEncodeError')
                        all_word.append('UnicodeEncodeError')
                all_time=[]
                for i in u_time:
                    all_time.append(i.get_text())
                with open(name,'w')as f:
                    n_name=name.split('.')[0]
                    f.write('用户名：'+n_name+'\n\n')
                    f.write('关注的吧：')
                    try:#判断是否关注
                        print(all_focus[0])
                        for i in all_focus:
                            f.write(i+',')
                        f.write('\n\n')
                    except IndexError:
                        f.write('关注的吧的列表为空!'+'\n\n')
                    for i in range(len(all_word)):
                        f.write(all_time[i]+'：'+all_word[i]+'\n')

                f.close()
            all_focus=[]
            if type(ihome)==type(bs.find('div')):
                print('Flase')
                u_focus=ihome.find_all('a',locate="like_forums#ihome_v1")
                for i in u_focus:
                    all_focus.append(i.get_text())
                tiezi()
            else:
                print('True')
                print(user)
                tiezi()
        except AttributeError:
            print('用户隐藏了动态')
            pass
    if str(bs.title)[7:-8]=='贴吧404':
        print('你输入的用户名有误！请重新输入!')
        #user=input('请输入你要查询的用户名：')
        pass
    else:
        main(bs)
put_user()
