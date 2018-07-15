def save_file(a,b,count):
    file_name_a='a'+str(count)+'.txt'
    file_name_b='b'+str(count)+'.txt'
    a_file=open(file_name_a,"w")
    b_file=open(file_name_b,"w")
    a_file.writelines(a)
    b_file.writelines(b)
    a_file.close()
    b_file.close()
def split_file(file_name):
    f=open(file_name)
    a=[]
    b=[]
    count=1
    for each_line in f:
        if each_line[:6]!="------":
            '我们这里进行字符串分割操作'
            (role,line_spoken)=each_line.split(":",1)
            if role=='a':
                a.append(line_spoken)
            if role=='b':
                b.append(line_spoken)
        else:
            '文件的分别保存操作'
            save_file(a,b,count)
            a=[]
            b=[]
            count+=1

    save_file(a,b,count)
    f.close()
split_file("record.txt")
