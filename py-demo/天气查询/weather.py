from tkinter import *#init
from tkinter import messagebox#弹出框
import urllib.request
import requests

def weather():
    #city=input('---')
    city=entry.get()
    if city=='':
        messagebox.showinfo('提示','请输入要查询的城市')
    else :
        city=urllib.request.quote(city)#转码
        host='http://jisutqybmf.market.alicloudapi.com/weather/query'
        querys='city='+city
        url = host + '?' + querys
        appcode = '86839ca85a304814bffcbde75336ff52'

        header={'Authorization':'APPCODE ' + appcode}
        req=requests.get(url,headers=header).json()
        #print(req['result'])
        info=req['result']
        list_details.delete(0,END)#删除一次
        list_details.insert(0,"天气:%s"%info['weather'])
        list_details.insert(1,"最高温度:%s"%info['temphigh'])
        list_details.insert(2,"最低温度:%s"%info['templow'])
        list_details.insert(3,"空调指数:%s"%info['index'][0]['detail'])
        list_details.insert(4,"运动指数:%s"%info['index'][1]['detail'])
        list_details.insert(5,"-:%s"%info['aqi']['aqiinfo']['affect'])
        list_details.insert(6,"-:%s"%info['aqi']['aqiinfo']['measure'])

root=Tk()#窗口
root.title('天气查询')
root.geometry('410x300+500+300')#窗口大小及位置
lable=Label(root,text='请输入要查询的城市名字：')#标签控件
lable.grid(row=0,column=0)#栅格布局
entry=Entry(root,font=('微软雅黑',15))#输入控件
entry.grid(row=0,column=1)
list_details=Listbox(root,font=('微软雅黑',10),width=50,height=10)
list_details.grid(row=1,columnspan=2)#合并
button_left=Button(root,text='查询',width='10',command=weather)#鼠标点击事件
button_left.grid(row=2,column=0,sticky='W')#sticky 对齐方式
button_left=Button(root,text='退出',width='10',command=root.quit)
button_left.grid(row=2,column=1,sticky='E')
#weather()
root.mainloop()#消息loop