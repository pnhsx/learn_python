"""
    socket 客户端开发
"""

import socket

# 创建 socket对象
socket_client = socket.socket()

# 连接到服务端
socket_client.connect(("localhost", 8888))

# 发送消息
while True:
    msg = input("请输入要给服务端发送的消息:")
    if msg == 'exit':
        break
    socket_client.send(msg.encode("UTF_8"))

    # 接收返回消息
    recv_data = socket_client.recv(1024)  # 1024是缓冲区大小,一般 1024即可,同样 recv方法是阻塞的
    print(f"服务器端返回的消息是:{recv_data.decode('UTF-8')}")

# 关闭链接
socket_client.close()
