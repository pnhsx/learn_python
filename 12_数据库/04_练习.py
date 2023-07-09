from pymysql import Connect

conn = Connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    autocommit=True
)

conn.select_db('py_sql')
cursor = conn.cursor()
cursor.execute("select * from orders")
result = cursor.fetchall()

f = open('./orders.txt', 'a', encoding='utf-8')
for element in result:
    data = f'{{"date":"{element[0]}","order_id":"{element[1]}","money":{element[2]},"provice":"{element[3]}"}}'
    f.write(data)
    f.write('\n')

conn.close()
f.close()
