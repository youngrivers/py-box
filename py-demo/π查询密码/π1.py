pwds=[]
for num in range(1000000):
    pwds.append("0"*(6-len(str(num)))+str(num))
with open("π.txt")as f:
    pai=f.read()

print(len(pai),pai[0:110])
stat=[]
for pwd in pwds:
    stat.append([pwd,pai.index(pwd)-1])
    if len(stat)%1000==1:
        print(stat[-1])
with open("π_stat.txt","w")as f:
    for data in stat:
        f.write(data[0]+":"+str(data[1]+"\n"))
f.close()
