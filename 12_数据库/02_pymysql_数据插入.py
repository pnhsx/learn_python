"""
pymysql 数据插入
"""

from pymysql import Connect

# 构建到 MySQL数据库的链接
coon = Connect(
    host='localhost',       # 主机名 (IP)
    port=3306,              # 端口
    user='root',            # 账号
    password='123456',      # 密码
    autocommit=True         # 自动提交 (确认)
)
print(coon.get_server_info())

# 执行非查询性质SQL
cursor = coon.cursor()  # 获取游标对象

# 选择数据库
coon.select_db("text")

# 执行SQL
cursor.execute("insert into student values(10002,'周杰伦',29,'男');")

# 通过 commit 确认
# coon.commit()

# 关闭链接
coon.close()
