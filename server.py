#!/usr/bin/env python
# -*- coding=utf-8 -*-


"""
file: service.py
socket service
"""


import socket #socket模块
import threading #threading模块
import time #time模块
import sys #sys模块


def socket_service(): #创建服务端
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#socket.AF_INET建立服务器间网络通信，socket.SOCK_STREAM为流式socket，for TCP
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #（一般不会立即关闭而经历TIME_WAIT的过程）后想继续重用该socket
        s.bind(('127.0.0.1', 6666)) #将套接字绑定到地址，在AF_NET下，以元组(host，port)的形式表示地址
        s.listen(10) #开始监听TCP传入连接，s.listen(backlog)格式，backlog指定在拒绝连接之前，OS可以挂起的最大连接数
    except socket.error as msg: # 防止socket server重启后端口被占用（socket.error: [Errno 98] Address already in use）
        print msg
        sys.exit(1)
    print '等待连接...'

    while 1:
        conn, addr = s.accept() #连接地址
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()

def deal_data(conn, addr): #接收数据及显示数据
    print '接收到新连接来自 {0}'.format(addr)
    conn.send('欢迎进入本服务器')
    while 1:
        data = conn.recv(1024) #接收数据大小限定
        print '{0} 接收到来自客户端的数据为 {1}'.format(addr, data)
        #time.sleep(1)
        if data == 'exit' or not data:
            print '{0} 连接关闭'.format(addr)
            conn.send('连接已关闭')
            break
        conn.send('已传送字符串为：{0}'.format(data))
    conn.close()


if __name__ == '__main__':
    socket_service()
