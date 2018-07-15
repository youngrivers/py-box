
import urllib.request
import os

def url_open(url):
    req=urllib.request.Request(url)
    #req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36')
    response=urllib.request.urlopen(req)
    html=response.read()
    return html

def get_pages(url):
    html=url_open(url).decode('utf-8')

    a=html.find('current-comment-page')+23
    b=html.find(']',a)

    return html[a:b]
    
def find_pages(url):
    html=url_open(url).decode('utf-8')
    img_addrs=[]
    a=html.find('img src=')

    while a!=-1:
        b=html.find('.jpg',a,a+255)#限定范围
        if b!=-1:
            img_addrs.append(html[a+9:b+4])
        else:
            b=a+9
        a=html.find("img src=",b)
    return imgs_addrs
'''
    for each in img_addrs:
        print(each)
'''

def save_imgs(folder,img_addrs):
    for each in imgs_addrs:
        filename=each.split('/')[-1]
        with open('filename','wb')as f:
            img=url_open(each)
            f.write(img)

def download_mm(floder="OOXX",pages=10):
    os.mkdir(floder)#创建文件夹
    os.chdir(floder)#进入文件夹

    url="http://jandan.net/ooxx/"
    page_num=int(get_pages(url))

    for i in range(pages):
        page_num-=i
        page_url=url+'page-'+str(page_num)+"#comments"
        img_addrs=find_imgs(pages_url)


if __name__=='__main__':
    download_mm()
