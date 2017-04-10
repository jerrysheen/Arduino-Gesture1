from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import serial
x_begin=516
y_begin=507
ser = serial.Serial('/dev/cu.usbmodem1411',9600)
m = PyMouse()
x_max,y_max = m.screen_size()
while 1 :
    if(ser.inWaiting()):
            x_current,y_current = m.position()
            read = ser.readline()
            comma = read.index(',')
            end = read.index(')')
            y_move = int(read[1:comma])-y_begin
            x_move = int(read[comma+1:end])-x_begin
            y_move = y_move/20
            x_move = x_move/20
            m.move(x_current+x_move,y_current+y_move)    
