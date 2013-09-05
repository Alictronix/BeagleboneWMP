#!/usr/bin/env python
import socket

host = '192.168.7.2'
port = 50000
size = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

while 1:
    yaw = s.recv(size)
    s.send('a')
    pitch = s.recv(size)
    s.send('b')
    roll = s.recv(size)
    s.send('c')
    print yaw, pitch, roll
    y1=int(yaw)
    y2=int(pitch)
    y3=int(roll)
    
    print y1,y2,y3
   
s.close()
