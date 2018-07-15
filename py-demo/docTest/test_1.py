f=open('record.txt')
a=[]
b=[]
count=1
for each_line in f:
    if each_line[:6]!="------":
        if each_line[:2]!="a:":
            #f=open("b1.txt","w")
            b.append(each_line.split("b:")[1])
            #f.write(str(b))
            #f.writelines(b)
        else:
            #f=open("a1.txt","w")
            a.append(each_line.split("a:")[1])
            #f.writelines(a)
    else:
        file_name_a='a'+str(count)+'.txt'
        file_name_b='b'+str(count)+'.txt'
        a_file=open(file_name_a,"w")
        b_file=open(file_name_b,"w")
        a_file.writelines(a)
        b_file.writelines(b)
        a_file.close()
        b_file.close()
        a=[]
        b=[]
        count+=1
file_name_a='a'+str(count)+'.txt'
file_name_b='b'+str(count)+'.txt'
a_file=open(file_name_a,"w")
b_file=open(file_name_b,"w")
a_file.writelines(a)
b_file.writelines(b)
a_file.close()
b_file.close()
#f.writelines(str(b))
f.close()
