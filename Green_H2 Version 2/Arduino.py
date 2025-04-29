import serial
import time
import re

class IOT:
  def __init__(self):
  
    ser = serial.Serial('COM5',9600)
    time.sleep(2)
    temp = []
    hydrogen_list = []
    humuidity_list = []
    while True:
      
        line = ser.readline().decode("utf-8")
        
        self.sensor_value = re.findall(r"[0-9.]*\S",line)
        self.temperature_1 = float(self.sensor_value[0])
        self.temperature_H = float(self.sensor_value[1])
        self.humuidity_1 = float(self.sensor_value[2])
        self.humuidity_H = float(self.sensor_value[3])
        self.hydrogen = int(self.sensor_value[4])
       
        
        temp.sort()
        temp.append(self.temperature_1)
        hydrogen_list.append(self.hydrogen)
        humuidity_list.append(self.humuidity_1)
        self.max_temp = temp[-1]
        self.Min_temp = temp[0]
        self.hydrogen_production = sum(hydrogen_list)
        self.Avg_humuidity = sum(humuidity_list) / len(humuidity_list)
        
       
        print(line)
        
        
  
# ob = IOT()
      
        


 
