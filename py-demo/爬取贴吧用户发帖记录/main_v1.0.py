import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
user=input('请输入你要查询的用户名：')

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
        u_word=bs.find('div',class_='ihome_section').find_all('a',locate="thread_author#ihome_v1")
        u_time=bs.find('div',class_='ihome_section').find_all('div',class_='n_post_time')
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
            for i in range(len(all_word)):
                f.write(all_time[i]+'：'+all_word[i]+'\n')

        f.close()
    except AttributeError:
        print('用户隐藏了动态')
        pass
if str(bs.title)[7:-8]=='贴吧404':
    print('你输入的用户名有误！请重新输入!')
    user=input('请输入你要查询的用户名：')
else:
    main(bs)
