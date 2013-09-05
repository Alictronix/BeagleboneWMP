#!/usr/bin/python

#i2cdump -f -y 1 0x53
#i2cset -f -y 1 0x53 0xFE 0x04 w
#i2cdump -f -y 1 0x52"

import os
import smbus
import time
import socket

host = ''
port = 50000
backlog = 5
size = 1024
a='a'
b='b'
c='c'
wmp = smbus.SMBus(1) 
add_a = 0x53
add_b = 0x52

try:
      wmp.write_byte_data(add_a,0xFE,0x04)
except Exception:
      pass
          
print " wmp activated ...."

ya = 0
pi = 0
ro = 0

for y in range(0, 10):
    data = wmp.read_i2c_block_data(add_b,0)
    ya += (((data[3]>>2)<<8)+data[0]) 
    pi += (((data[4]>>2)<<8)+data[1])
    ro += (((data[5]>>2)<<8)+data[2])
    
ya=ya/10
pi=pi/10
ro=ro/10

print " waiting for connections ...."

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
client, address = s.accept()
print "connected to...", address 

z = 1
while True:
    data = wmp.read_i2c_block_data(add_b,0)
    
    yaw=((data[3]>>2)<<8)+data[0]-ya;
    pitch=((data[4]>>2)<<8)+data[1]-pi;
    roll=((data[5]>>2)<<8)+data[2]-ro;
    
   
    y1=str(yaw)
    y2=str(pitch)
    y3=str(roll)
  
    print yaw, y1
    print pitch, y2
    print roll, y3
    
    client.send(y1)
    if client.recv(1) == a:
        client.send(y2)
    if client.recv(1)==b:
        client.send(y3)
    if client.recv(1)==c:
        continue

client.close()
