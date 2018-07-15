def tower(n,x,y,z):
    if n==1:
        print(x,"-->",z)
    else:
        tower(n-1,x,z,y)#将前n-1个盘子从x移动到y上
        print(x,"-->",z)#将最底下的最后一个盘子从x移动到z上
        tower(n-1,y,x,z)#将y上的n-1个盘子移动到z上
n=int(input("请输入汉罗塔层数："))
tower(n,"X","Y","Z")
