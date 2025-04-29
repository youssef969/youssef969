import serial
import time

class IOT:
  def __init__(self):
  
    ser = serial.Serial('COM5',9600)
    time.sleep(2)
    temp = []
    hydrogen = []
    while True:
      line = ser.readline().decode("utf-8")
      self.temperature = line[36:38]
      self.humuidity = line[10:12]
      self.temperature_2 = line[41:46]
      self.humuidity_2 = line[15:20]
      self.hydrogeen = line[76:79]
      
      if self.temperature == "" or self.hydrogeen == "":
        continue
      else:
        int_hydrogen = int(self.hydrogeen)
        float_temp = float(self.temperature)
        temp.sort()
        temp.append(float_temp)
        hydrogen.append(int_hydrogen)
        self.max_temp = temp[-1]
        self.Min_temp = temp[0]
        print(sum(hydrogen))


 
