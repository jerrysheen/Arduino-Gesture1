from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import serial
x_begin = 516
y_begin = 507
ser = serial.Serial('/dev/cu.usbmodem1411',9600)
m = PyMouse()

try:
    while 1:
        if(ser.inWaiting()):
            x_current,y_current = m.position()
            read = ser.readline()
            if read.find('(') == -1 : 
                comma = read.index(',')
                end = read.index(')')
                x_move = int(read[comma+1:end])-x_begin
                y_move = int(read[1:comma])-y_begin
                x_move = x_move/20
                y_move = y_move/20
                m.move(x_current+x_move,y_current+y_move)
            elif read == 'DOWN\r\n' :
               count = 0
               while count < 5:
                   m.scroll(1,0,0)
                   time.sleep(0.05)
                   count = count + 1
            elif read == 'UP\r\n' :
                count = 0
                while count <5:
                    m.scroll(-1,0,0)
                    time.sleep(0.05)
                    count = count + 1
            elif read == 'CLICK\r\n' :
                m.click(current_x,current_y,1)
except KeyboardInterrupt :
    print("stop")
