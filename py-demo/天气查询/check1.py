

with open("main_city.txt",'r')as f:
    all_txt=f.read()

a=[]
b=[]
for line in all_txt.split(','):
    a.append(line.split(":")[0]+"\n")
    b.append(line.split(":")[1]+'\n')
main_city_a=open("main_city_a.txt","w")
main_city_a.writelines(a)
main_city_a.close()


main_city_b=open("main_city_b.txt","w")
main_city_b.writelines(b)
main_city_b.close()
f.close()

