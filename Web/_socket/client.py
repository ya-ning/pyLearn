#!/usr/bin/python3
import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

s.connect((host, port))
msg = s.recv(1024)
s.close()
print(msg.decode('utf-8'))
