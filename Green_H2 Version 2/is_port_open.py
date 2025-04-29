import serial
import re
from tkinter import messagebox

def is_port_open():
            try:
                ports = ["COM7","COM5"]
                for x in range(2):
                    if  serial.Serial(ports[x]).is_open == True:
                        return ports[x]
                    else:
                        break              
            except:
               return ports[x+1]
           
            
             


print(serial.Serial("COM7").is_open)        





