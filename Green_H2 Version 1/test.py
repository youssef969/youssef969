import serial
import continuous_threading

import serial

def is_port_open(port):
    try:
        ser = serial.Serial(port)
        ser.close()
        return True
    except serial.SerialException:
        return False


if is_port_open('COM5'):
    try:
        ser = serial.Serial('COM5',9600)
        line = ser.readline().decode("utf-8")
        print(line)
    except serial.SerialException:
        print("HELLO MAMA")   
else:
    try:
        ser = serial.Serial('COM7',9600)
        line = ser.readline().decode("utf-8")
        print(line)
    except serial.SerialException:
        print("HELLO MAMA")   

 
    
    
    
