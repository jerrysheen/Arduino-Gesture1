from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import serial

ser = serial.Serial('/dev/cu.usbmodem1411',9600)
m = PyMouse()
k = PyKeyboard()
x_max,y_max = m.screen_size()
try:
    while 1 :
        if(ser.inWaiting()):
             x_current,y_current = m.position()
             x_move = x_max/20
             y_move = y_max/20
             string = ser.readline()
             if string == 'DOWN\r\n' :
                 count = 0
                 while count < 5:
                     m.scroll(1,0,0)
                     time.sleep(0.05)
                     count  = count + 1
                 print('DOWN')
                 time.sleep(1)
             elif string == 'UP\r\n'   :
                 count = 0 
                 while count < 5:
                     m.scroll(-1,0,0)
                     time.sleep(0.05)
                     count = count + 1
                 print('UP')
                 time.sleep(1)

except KeyboardInterrupt:
    print("stop")

