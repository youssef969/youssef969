from tkinter import *
import continuous_threading
import serial


def Temperature ():
    ser = serial.Serial('COM5',9600)
    line = ser.readline().decode("utf-8")
    temperature = line[36:41]
    dep = Label(root,text=f"temperature = {temperature}")
    dep.place(x=150,y=40)
    humuidity = line[10:15]
    dep2 = Label(root,text=f"humuidity = {humuidity}")
    dep2.place(x=150,y=80)

    
   
    
    
root = Tk()      
t1 = continuous_threading.PeriodicThread(2,Temperature)
t1.start()
root.mainloop()