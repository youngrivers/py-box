#将000000~999999存到字典中，初始化出现的位置为正无穷（用10亿+1代替）
dic={}
for num in range(1000000):
    dic["0"*(6-len(str(num)))+str(num)]=10000001

#读取π
with open("π.txt")as f:
    pai=f.read()

#输出字符串π的长度和π的前109位
print(len(pai),pai[0:110])

sta=[]
#p=1,跳过了3.
p=1
#p允许的最大数值
p_max=len(pai)-1000000
'''
倒序查找，开始时从第1000001位向第一位检索，检索到第一位时，若字典中仍存在无穷大
，则从2000001位向1000001位检索，以此类推，直到字典中不存在无穷大或者p大于p_max
'''
while 9000001 in dic.values() and p<p_max:
    for i in range(p+1000000,p,-1):
        pwd=pai[i:i+6]
        if i<dic[pwd]:
            dic[pwd]=i-1
        if i%100000==0:
            print(i)
    p=p+1000000

with open("p_stat_copy.txt","w")as f:
    for item in dic.items():
        f.write(item[0]+":"+str(item[1])+"\n")
f.close()
