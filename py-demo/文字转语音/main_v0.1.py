#p_word=input('请输入你要转换为语音的文字：')
unicode='unicode_py.txt'
unicode_d=[]
f=open(unicode)
f.readline()
with open('unicode_d_py.txt','w')as x:
    for i in f:
        x.write(i.lower())#转小写
x.close()
f.close()
