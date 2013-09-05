#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt
import socket

host = '192.168.7.2'
port = 50000
size = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
 
plt.ion() # set plot to animated
 
y1data = [0] * 50
y2data = [0] * 50
y3data = [0] * 50
ax1=plt.axes() 
 
# make plot
line1, = plt.plot(y1data)
line2, = plt.plot(y2data)
line3, = plt.plot(y3data)
plt.ylim([10,40])
 
# start data collection
while True: 
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
    ymin = -5000
    ymax = 5000
    
    plt.ylim([ymin,ymax])
    y1data.append(y1)
    del y1data[0]
    y2data.append(y2)
    del y2data[0]
    y3data.append(y3)
    del y3data[0]

    line1.set_xdata(np.arange(len(y1data)))
    line1.set_ydata(y1data)  # update the data
    line2.set_xdata(np.arange(len(y2data)))
    line2.set_ydata(y2data)
    line3.set_xdata(np.arange(len(y3data)))
    line3.set_ydata(y3data)
    
    plt.legend(['yaw','pitch','roll'], loc='upper left')
    plt.draw() # update the plot
