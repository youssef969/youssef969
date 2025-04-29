from tkinter import * 
from tkinter import messagebox 
from time import strftime
import datetime
import requests
import re
import datetime
import serial
import continuous_threading
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split 




class Wheather:
    def __init__(self,root):
        
        self.root = root
        
        self.root.state("zoomed")
        self.root.resizable(True,True)
        self.root.config(bg="#0d0d0d")
        self.root.title("Green Hydrogen")
        self.root.minsize(1550,800)
        self.root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\1710162623466-removebg-preview.ico")
        self.t1 = continuous_threading.PeriodicThread()
        self.t1.start()
        
    def is_port_open(self,port):
                try:
                        ser = serial.Serial(port)
                        ser.close()
                        return True
                except serial.SerialException:
                        return False

    def Temperature (self):
                if self.is_port_open('COM5'):
                    
                        ser = serial.Serial('COM5',9600)
                        line = ser.readline().decode("utf-8")
                        print(line)
                        
                        
                        #     sensor_values = re.findall(r"[0-9.]*\S",line)
                        #     self.temperature_1 = float(sensor_values[0])
                        #     self.temperature_H = float(sensor_values[1])
                        #     self.humuidity_1 = float(sensor_values[2])
                        #     self.humuidity_H = float(sensor_values[3])
                        #     self.hydrogen = int(sensor_values[4])
                        
                        #     self.temp_lbl = Label(self.root,font=('Arial Black',28,'bold'),foreground="#259269",bg="White")
                        #     self.temp_lbl.place(x=530,y=260)
                        #     self.temp_lbl.config(text=f"{self.temperature_1}°C")
                        
                        #     self.humudity_lbl = Label(self.root,font=('Arial Black',28,'bold'),foreground="#259269",bg="White")
                        #     self.humudity_lbl.place(x=1280,y=260)
                        #     self.humudity_lbl.config(text=f"{self.humuidity_1}%")
                                
                        
                        #     self.Temperature_label = Label(self.root,font=('Arial Black',18,'bold'),foreground="#259269",bg="white")
                        #     self.Temperature_label.place(x=180,y=720)
                        #     self.Temperature_label.config(text=f"Hydrogen Temperature:  {self.temperature_H}°C")
                        
                        #     self.Humidity_label = Label(self.root,font=('Arial Black',18,'bold'),foreground="#259269",bg="white")
                        #     self.Humidity_label.place(x=980,y=720)
                        #     self.Humidity_label.config(text=f"Hydrogen Humidity:  {self.humuidity_H}%")
                        
                        #     Volume_label = Label(self.root,text=f"Hydrogen Concentrate:  {self.hydrogen} ppm",font=('Arial Black',18,'bold'),foreground="#259269",bg="white")
                        #     Volume_label.place(x=580,y=760)
                        
                        #     self.temp.sort()
                        #     self.temp.append(self.temperature_1)
                        #     self.hydrogen_list.append(self.hydrogen)
                        #     self.humuidity_list.append(self.humuidity_1)
                        #     max_temp = self.temp[-1]
                        #     Min_temp = self.temp[0]
                        #     # self.hydrogen_production = sum(self.hydrogen)
                        #     # self.Avg_humuidity = sum(self.humuidity_list) / len(self.humuidity_list)
                        #     month_2 = datetime.datetime.now().month
                        #     str_month =str(month_2)
                        #     data=pd.read_csv("D:\\Python\\Green_H2\\data_with_city.csv")
                        #     classifier = RandomForestClassifier(n_estimators=100,random_state=1)
                        #     x=data.iloc[:,:-1]
                        #     y=data.iloc[:,-1]
                        #     x_train ,x_test  , y_train , y_test = train_test_split(x,y,test_size=0.2,shuffle=False)
                        #     classifier.fit(x_train,y_train)
                        
                        #     test = pd.DataFrame({"month":[str_month],"precipitation":[0],"temp_max":[max_temp],"temp_min":[Min_temp],"wind":[self.current_speed]})
                        #     prediction = classifier.predict(test)[0] 
                        #     print(prediction) 
                        
                        #     if prediction == "rain" or prediction == "snow" or prediction == "drizzle":  
                        #             self.root.update()   
                        #             self.sun = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\cloudy-day.png")
                        #             self.sub_sun = self.sun.subsample(2,2)
                        #             sun_label = Label(self.root,image=self.sub_sun,bg="white")
                        #             sun_label.place(x=73,y=190)
                                                
                        #     elif prediction == "sun":
                        #                 self.root.update() 
                        #                 self.sun = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\sun.png")
                        #                 self.sub_sun = self.sun.subsample(2,2)
                        #                 sun_label = Label(self.root,image=self.sub_sun,bg="white")
                        #                 sun_label.place(x=73,y=190)
                                        
                        #     else:  
                        #             self.root.update() 
                        #             self.sun = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\sun.png")
                        #             self.sub_sun = self.sun.subsample(2,2)
                        #             sun_label = Label(self.root,image=self.sub_sun,bg="white")
                        #             sun_label.place(x=73,y=190)
                        # except serial.SerialException:
                        #         messagebox.showerror("Error","Connection is Lost, Please Try Again and Refresh The Window")
                        #         self.t1.close()
root = Tk()
                       
ob = Wheather(root)
root.mainloop()