"""
    socket服务端开发
"""
import socket

# 1.创建 Socket对象
socket_server = socket.socket()

# 2.绑定 ip地址和端口
socket_server.bind(("localhost", 8888))

# 3.监听端口
socket_server.listen(1)  # listen方法内接收一个整数传参,表示接受的链接数量

# 4.等待客户端链接
# result: tuple = socket_server.accept()
# conn = result[0]        # 客户端和服务段的连接对象
# address = result[1]     # 客户端地址信息
conn, address = socket_server.accept()
# accept方法返回的是二元元组(连接对象,客户端地址信息)
# 可以通过 变量1,变量2 = socket_server.accept()的形式,直接接受二元元组内的两个元素
# accept()  是阻塞的方法, 如果没有客户端链接,会卡在这一行,不会继续执行
print(f"接收到了客户端链接,客户端信息:{address}")

# 5.接收客户端信息,要使用客户端和服务端的本次连接对象,而非socket_server
while True:
    data = conn.recv(1024).decode('UTF-8')
    # recv接受的的参数是缓冲区大小, 一般给1024即可
    # recv的返回值是一个字节数组也就是 bytes对象,不是字符串,可以通过decode方法,将字节数组转换为字符串对象
    print(f"客户端发来的消息是:{data}")

    # 6.发送回复消息
    msg = input("请输入你要和客户端回复的消息:")  # encode可以将字符串编码为字节数组对象
    if msg == 'exit':
        break
    conn.send(msg.encode('UTF-8'))

# 7.关闭链接
conn.close()
socket_server.close()
