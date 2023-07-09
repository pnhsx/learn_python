"""
pymysql 库的基础操作
"""

from pymysql import Connect

# 构建到 MySQL数据库的链接
coon = Connect(
    host='localhost',        # 主机名 (IP)
    port=3306,               # 端口
    user='root',             # 账号
    password='123456'        # 密码
)
print(coon.get_server_info())

# 执行非查询性质SQL
cursor = coon.cursor()  # 获取游标对象

# 选择数据库
coon.select_db("text")

# 执行SQL
# cursor.execute("create table text_pymysql(id int)")

# cursor.execute("select * from student")
cursor.execute("drop table text_pymysql")

result = cursor.fetchall()
for i in result:
    print(i)

# 关闭链接
coon.close()
