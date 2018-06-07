#!/usr/bin/env python
# -*- coding=utf-8 -*-


"""
file: client.py
socket client
"""

import socket #socket模块
import sys #sys模块


def socket_client(): #创建客户端
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.AF_INET建立服务器间网络通信，socket.SOCK_STREAM为流式socket，for TCP
        s.connect(('127.0.0.1', 6666)) #连接到服务器，端口号为6666
    except socket.error as msg: #防止socket server重启后端口被占用
        print msg
        sys.exit(1)
    print s.recv(1024) #数据发送大小限定
    while 1:
        data = raw_input('请输入需要传输的字符: ')
        s.send(data)
        print s.recv(1024)
        if data == 'exit':
            break
    s.close() #关闭连接


if __name__ == '__main__':
    socket_client()
