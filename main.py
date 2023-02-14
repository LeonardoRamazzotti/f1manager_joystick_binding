import mouse
import time
import mouse_custom as m
import os
import serial 
import keymap as k

import mouse 

mouse.visible=False

port='COM4'

try:
		ser = serial.Serial(port, 9600) # open serial port
		print(ser.name)       # check which port was really used
except:
	print('Comunication Error: No Port Selected')
	

while True:

    try:
        det=ser.readline()
        print(type(det))
        print(det)
        data=det.decode()

        button=(int(data))

        print(type(button))
        print(button)

        k.key_fun(button)
        
    except:
        print("something doesen't work")
        
        break

ser.close()

