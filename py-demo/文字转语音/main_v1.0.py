import pygame

def chinese_to_pinyin(x):
    y=''
    dic={}
    with open('unicode_d_py.txt')as f:
        for i in f.readlines():
            dic[i.split()[0]]=i.split()[1]
    for i in x:
        i=ascii(i)[3:-1]#i = str(i.encode('unicode_escape'))[-5:-1]
        try:
            y+=dic[i]+" "
        except KeyError:
            y+='xxxx'
    return y
def make_voice(x):
    pygame.mixer.init()
    vo=chinese_to_pinyin(x).split()
    for i in vo:
        print(i)
        if i=='xxxx':
            continue
        pygame.mixer.music.load('voice/'+i+'.wav')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            pass
    return None
while True:
    p_word=input('请输入你要转换为语音的文字：')
    make_voice(p_word)
