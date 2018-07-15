import sqlite3
conn=sqlite3.connect('test.db')#连接到SQLite数据库
cursor=conn.cursor()# 创建一个Cursor
try:
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')#创建user表
    cursor.execute('insert into user (id ,name) values(\'1\',\'kite\')')#插入一条记录
except sqlite3.OperationalError:
    pass
cursor.close()#关闭Cursor
conn.commit()#提交事务
conn.close()#关闭Connection

#查询
conn=sqlite3.connect('test.db')
cursor=conn.cursor()
cursor.execute('select * from user where id=?',('1',))# 执行查询语句
values=cursor.fetchall()# 获得查询结果集
print(values)
cursor.close()
conn.close()