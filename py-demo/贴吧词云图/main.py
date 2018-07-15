from wordcloud import WordCloud
from bs4 import BeautifulSoup
import urllib.request
import jieba
import matplotlib.pyplot as plt     #数学绘图库

def open_url(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36')
    response=urllib.request.urlopen(req)
    html=response.read()
    return html

def get_word_img():
    #url='https://tieba.baidu.com/f?kw=%B1%B3%B9%F8&fr=ala0&tpl=5'
    url='https://tieba.baidu.com/p/5778244716'
    html=open_url(url)
    bs=BeautifulSoup(html,'lxml')
    text=[]
    main_content=bs.find('div',class_='p_postlist').find_all('div',class_='d_post_content_main ')#[1]
    for data in main_content:
        cc=data.find('cc').get_text().strip().replace('🐯','虎')
        text.append(cc)
    text=str(text)#.decode('utf-8')
    cut_word(text)

def cut_word(text):
    cut_text=jieba.cut(text)
    result=' '.join(cut_text)
    print(result)
    draw_wordcloud(result)

def draw_wordcloud(result):
    wc=WordCloud(
        font_path='font/king.ttf',
        background_color='black',
        #mask=color_mask,
        width=800,
        height=600,
        #mode='RGBA',
        #colormap='pink',
        max_words=200,
        max_font_size=100,
        random_state=30
    )
    wc.generate(result) # 产生词云
    #wc.to_file('cloud.jpg') #保存图片

    # 显示图片
    plt.figure("cloud") #指定所绘图名称
    plt.imshow(wc) # 以图片的形式显示词云
    plt.axis("off") # 关闭图像坐标系
    plt.show()

if __name__=='__main__':
    get_word_img()