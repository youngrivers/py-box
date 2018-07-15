import re
import os

re_p=re.compile(r'\d+')#匹配数字
os.chdir('voice')
for i in range(len(os.listdir())):
    s=str(os.listdir()[i])[-5]
    if re_p.match(s)==None:#判断包含数字
        print(os.listdir()[i])
        os.rename(os.listdir()[i],str(os.listdir()[i]).split('.')[0]+'5'+'.wav')
    '''
    if type(re_p.match(s))=='_sre.SRE_Match':
        print(os.listdir()[i])
        os.rename(os.listdir()[i],str(os.listdir()[i])[0:-2])
        '''

