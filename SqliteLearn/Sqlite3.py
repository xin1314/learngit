import sqlite3
conn = sqlite3.connect('mrsoft.db')
cursor = conn.cursor()
# cursor.execute('create table user (id int(10) primary key, name varchar(20))')
# cursor.close()
# conn.close()

cursor.execute('insert into user (id, name) values ("1", "MRSOFT")')
cursor.execute('insert into user (id, name) values ("2", "Andy")')
cursor.execute('insert into user (id, name) values ("3", "明日科技小助手")')
