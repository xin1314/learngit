import sqlite3
conn = sqlite3.connect('mrsoft.db')
cursor = conn.cursor()
# cursor.execute('create table user (id int(10) primary key, name varchar(20))')  # 创建新表


# # 添加用户信息
# cursor.execute('insert into user (id, name) values ("1", "MRSOFT")')
# cursor.execute('insert into user (id, name) values ("2", "Andy")')
# cursor.execute('insert into user (id, name) values ("3", "明日科技小助手")')
# print(cursor.rowcount)
#
# cursor.close()
# conn.commit()
# conn.close()

#
# # select查询,cursor游标会不断往后走，到了最后一条信息后返回None
cursor.execute('select * from user')  # 执行查询语句
result1 = cursor.fetchone()  # 使用fetchone方法查询一条数据
result2 = cursor.fetchmany(2)  # 使用fetchmany方法查询多条数据
result3 = cursor.fetchall()  # 使用fetchall方法查询所有数据
# print(result1)
print(result1)
print(result3)

cursor.execute('select * from user where id > ?', (1, ))  # 执行查询语句
result4 = cursor.fetchall()
print(result4)
#
cursor.close()
conn.close()