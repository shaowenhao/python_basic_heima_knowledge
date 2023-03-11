# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 3/2/2023 3:27 PM
# 文件名称: pymsql.PY

from pymysql import Connection

#构建数据库链接
conn = Connection(
    host="140.231.89.72",
    port = 3307,
    user = "root",
    password = "123456"
)
info = conn.get_server_info()
print(info)

cursor = conn.cursor() #获取游标对象

#选择数据库
conn.select_db("siemens")

#执行sql
# cursor.execute("create table test_pymysql(id int);")

# sql查询
# cursor.execute("select * from sdl_10431")
# results = cursor.fetchall()
# print(results)
#
# for r in results:
#     print(r)

cursor.execute("insert into test_pymysql values(111)")
conn.commit()

conn.close()