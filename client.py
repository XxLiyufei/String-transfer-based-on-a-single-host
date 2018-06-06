#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

import socket

s=socket.socket()  #创建socket对象
host=socket.gethostname()  #获取主机名
port=12345  #设置端口号

s.connect((host,port))
print s.recv(1024)
s.close
