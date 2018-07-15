import urllib.request
import urllib.parse
import csv
import os
import time
from bs4 import BeautifulSoup

job = input('请输入你要查询的工作：')
if job == '':
    job = 'python'
else:
    pass


def url_job(index):
    url = 'https://search.51job.com/list/'
    data = {}
    data['lang'] = 'c'
    data['stype'] = 1
    data['postchannel'] = 0000
    data['workyear'] = 99
    data['cotype'] = 99
    data['degreefrom'] = 99
    data['jobterm'] = 99
    data['companysize'] = 99
    data['lonlat'] = 0, 0
    data['radius'] = -1
    data['ord_field'] = 0
    data['confirmdate'] = 9
    data['fromType'] = ''
    data['dibiaoid'] = 0
    data['address'] = ''
    data['line'] = ''
    data['specialarea'] = 00
    data['from'] = ''
    data['welfare'] = ''
    data = urllib.parse.urlencode(data)
    url = url+'040000,000000,0000,00,9,99,'+job+',2,'+str(index)+'.html?'+data
    return url


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36')
    res = urllib.request.urlopen(req)
    html = res.read()
    # print(url)
    return html


def get_job():
    url = url_job(1)
    html = open_url(url)
    bs = BeautifulSoup(html, 'lxml')
    #print(str(bs.title)[7:-8].split('-')[0])
    pages = bs.find(id='resultList').find_all('div', class_='rt')[1].get_text()  # .find('span',class_='dw_c_orange').get_text()
    num = str(pages).split('/')[1]
    rows = []
    now = str(time.localtime().tm_year) + \
        str(time.localtime().tm_mon)+str(time.localtime().tm_mday)
    filename = job+'-'+now+'.csv'
    for item in range(1,int(num)):#得到不同网页
        print('------打印：'+str(item)+'------')
        url = url_job(item)
        html = open_url(url)
        bs = BeautifulSoup(html, 'lxml')
        el = bs.find(id='resultList').find_all('div', class_='el')
        for i in range(1, len(el)):
            row = []
            job_name = el[i].find_all('span')[0].find('a')['title']
            cp_name = el[i].find_all('span')[1].find('a')['title']
            work_place = el[i].find_all('span')[2].get_text()
            job_money = el[i].find_all('span')[3].get_text()
            push_time = el[i].find_all('span')[4].get_text()
            row.append(job_name)
            row.append(cp_name)
            row.append(work_place)
            row.append(job_money)
            row.append(push_time)
            rows.append(row)
        with open(filename, 'w', newline='')as f:
            header = ['职位名', '公司名', '工作地点', '薪资', '发布时间']
            #writer = csv.writer(f)
            writer = csv.DictWriter(f, header)
            writer.writeheader()
            writer = csv.writer(f)
            for item in rows:
                writer.writerow(item)


def get_csv(filename):
    pass


if __name__ == '__main__':
    get_job()
