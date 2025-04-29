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
import sys
from Arduino import IOT
import time 
from data import Data
import pymysql


class Weather:
    def __init__(self,main_window):
        self.main_window = main_window
        #self.root = root
        self.root = Toplevel()
        self.root.state("zoomed")
        self.root.resizable(True,True)
        self.root.config(bg="#0d0d0d")
        self.root.title("Green Hydrogen")
        self.root.minsize(1550,800)
        self.root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\3-removebg-preview_1.ico")
        
        # =============================================== Weather API ==================================================
        
        api2 = "https://api.open-meteo.com/v1/forecast?latitude=31.037933&longitude=31.381523&current=wind_speed_10m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,wind_speed_10m_max&timezone=Africa%2FCairo&forecast_days=14"
        json_data = requests.get(api2).json()
        self.current = json_data["daily"]['temperature_2m_max'][0]
        self.day1_temp = json_data['daily']['temperature_2m_max'][1]
        self.day2_temp = json_data['daily']['temperature_2m_max'][2]
        self.day3_temp = json_data['daily']['temperature_2m_max'][3]
        self.day4_temp = json_data['daily']['temperature_2m_max'][4]
        self.day5_temp = json_data['daily']['temperature_2m_max'][5]
       
        self.current_sunrise = json_data["daily"]["sunrise"][0]
        self.day1_sunrise = json_data['daily']['sunrise'][1]
        self.day2_sunrise = json_data['daily']['sunrise'][2]
        self.day3_sunrise = json_data['daily']['sunrise'][3]
        self.day4_sunrise = json_data['daily']["sunrise"][4]
        self.day5_sunrise = json_data['daily']['sunrise'][5]
        
        self.current_sunset = json_data["daily"]["sunset"][0]
        self.day1_sunset = json_data['daily']['sunset'][1]        
        self.day2_sunset = json_data['daily']['sunset'][2]
        self.day3_sunset = json_data['daily']['sunset'][3]
        self.day4_sunset = json_data['daily']["sunset"][4]
        self.day5_sunset = json_data['daily']['sunset'][5]
        
        self.current_speed = json_data["daily"]["wind_speed_10m_max"][0]
        self.day1_speed = json_data['daily']["wind_speed_10m_max"][1]
        self.day2_speed = json_data['daily']["wind_speed_10m_max"][2]
        self.day3_speed = json_data['daily']["wind_speed_10m_max"][3]
        self.day4_speed = json_data['daily']["wind_speed_10m_max"][4]
        self.day5_speed = json_data['daily']["wind_speed_10m_max"][5]
        
        self.sunrise_1=self.Sunset(self.current_sunrise,self.current_sunset)[0]
        self.sunrise_2=self.Sunset(self.day1_sunrise,self.day1_sunset)[0]
        self.sunrise_3=self.Sunset(self.day2_sunrise,self.day2_sunset)[0]
        self.sunrise_4=self.Sunset(self.day3_sunrise,self.day3_sunset)[0]
        self.sunrise_5=self.Sunset(self.day4_sunrise,self.day4_sunset)[0]
        self.sunrise_6=self.Sunset(self.day5_sunrise,self.day5_sunset)[0]
        
        self.sunset_1=self.Sunset(self.current_sunrise,self.current_sunset)[1]
        self.sunset_2=self.Sunset(self.day1_sunrise,self.day1_sunset)[1]
        self.sunset_3=self.Sunset(self.day2_sunrise,self.day2_sunset)[1]
        self.sunset_4=self.Sunset(self.day3_sunrise,self.day3_sunset)[1]
        self.sunset_5=self.Sunset(self.day4_sunrise,self.day4_sunset)[1]
        self.sunset_6=self.Sunset(self.day5_sunrise,self.day5_sunset)[1]
        
        self.power_1 = self.Solar_Panel_Elec(self.sunrise_1,self.sunset_1,self.current)
        self.power_2 = self.Solar_Panel_Elec(self.sunrise_2,self.sunset_2,self.day1_temp)
        self.power_3 = self.Solar_Panel_Elec(self.sunrise_3,self.sunset_3,self.day2_temp)
        self.power_4 = self.Solar_Panel_Elec(self.sunrise_4,self.sunset_4,self.day3_temp)
        self.power_5 = self.Solar_Panel_Elec(self.sunrise_5,self.sunset_5,self.day4_temp)
        self.power_6 = self.Solar_Panel_Elec(self.sunrise_6,self.sunset_6,self.day5_temp)
        
        
       
    
        # ============================================== Frames ==================================================
        self.Frame = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Rectangle 1.png")
        frame_label = Label(self.root,image=self.Frame,bg="#0d0d0d")
        frame_label.place(x=0,y=150)
        
        self.Frame2 = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Rectangle 1 (1).png")
        frame_label = Label(self.root,image=self.Frame2,bg="#0d0d0d")
        frame_label.place(x=600,y=0)
        
        self.line = Frame(self.root,bg="black")
        self.line.place(x=75,y=460,width=1400,height=5)
        
        self.line2 = Frame(self.root,bg="black")
        self.line2.place(x=75,y=670,width=1400,height=5)
        
        # ============================================== Frame 1 =================================================== 
        self.image = PhotoImage(file ="C:\\Users\\Computec\\Downloads\\PNG Icons\\3-removebg-preview.png")
        self.sub = self.image.subsample(4,4)
        image_label = Label(self.root,image=self.sub,bg="#1d1d1d")
        image_label.place(x=630,y=2)
        
        GreenH = Label(self.root,text="Green Hydorgen",fg="white",font=("Pacifico",22,"bold"),bg="#1d1d1d")
        GreenH.place(x=730,y=5)
        
        self.Home = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\home.png")
        self.sub_home = self.Home.subsample(3,3)
        self.Home_button = Button(self.root,text="  Home",image=self.sub_home,bd=0,bg="#0d0d0d",fg="white",justify="center",activebackground="#0d0d0d",compound="left",font=("Arial Black",12,"bold"),activeforeground="white",cursor="hand2",command=self.home)
        self.Home_button.place(x=300,y=90,width=110,height=50)
        
        self.weather = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\monitoring 2.png")
        self.sub_weather = self.weather.subsample(3,3)
        self.Weather_button = Button(self.root,text="  Monitor",image=self.sub_weather,bd=0,bg="#0d0d0d",fg="#27AE60",justify="center",activebackground="#0d0d0d",compound="left",font=("Arial Black",12,"bold"),activeforeground="#27AE60",cursor="hand2")
        self.Weather_button.place(x=450,y=90,width=140,height=50)
        
        self.database = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\database.png")
        self.sub_database = self.database.subsample(3,3)
        self.database_button = Button(self.root,text="  Database",image=self.sub_database,bd=0,bg="#0d0d0d",fg="white",justify="center",activebackground="#0d0d0d",compound="left",font=("Arial Black",12,"bold"),activeforeground="white",cursor="hand2",command=self.Database)
        self.database_button.place(x=630,y=90,width=140,height=50)
        
        self.refresh = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\reload.png")
        self.sub_refresh = self.refresh.subsample(3,3)
        self.refresh_button = Button(self.root,text="  Refresh",image=self.sub_refresh,bd=0,bg="#0d0d0d",fg="white",justify="center",activebackground="#0d0d0d",compound="left",font=("Arial Black",12,"bold"),activeforeground="white",cursor="hand2",command=self.Refresh)
        self.refresh_button.place(x=800,y=90,width=140,height=50)
        
        self.Setting = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\gear.png")
        self.sub_Setting = self.Setting.subsample(3,3)
        self.Setting_button = Button(self.root,text="  Settings",image=self.sub_Setting,bd=0,bg="#0d0d0d",fg="white",justify="center",activebackground="#0d0d0d",compound="left",font=("Arial Black",12,"bold"),activeforeground="white",cursor="hand2")
        self.Setting_button.place(x=970,y=90,width=140,height=50)
        
        self.Exit = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\logout.png")
        self.sub_Exit = self.Exit.subsample(3,3)
        self.Exit_button = Button(self.root,text="  Exit",image=self.sub_Exit,bd=0,bg="#0d0d0d",fg="white",justify="center",activebackground="#0d0d0d",compound="left",font=("Arial Black",12,"bold"),activeforeground="white",cursor="hand2",command=self.Exit_func)
        self.Exit_button.place(x=1140,y=90,width=140,height=50)
        
        # ======================================================= Frame 2 =================================================================
        self.city_bg = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Rectangle 1 (3).png")
        city_bg_label = Label(self.root,image=self.city_bg,bg="white")
        city_bg_label.place(x=650,y=170)
        city = Label(self.root,text="< Egypt \ AL Dakahlia >",font=("Arial Black",11,"bold"),bg="#0D0D0D",fg="#27AE60",activebackground="#0D0D0D",activeforeground="#27AE60")
        city.place(x=675,y=175)
        current_day = datetime.datetime.now()
        today = Label(self.root,text=current_day.strftime("%A"),font=('Arial Black',11,'bold'),foreground="gold",bg="#0D0D0D")
        today.place(x=730,y=200)
        
        self.sun = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\sun.png")
        self.sub_sun = self.sun.subsample(2,2)
        sun_label = Label(self.root,image=self.sub_sun,bg="white")
        sun_label.place(x=73,y=190)
        
        self.temp = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\thermometer.png")
        self.sub_temp = self.temp.subsample(2,2)
        self.temp_label = Label(self.root,image=self.sub_temp,bg="white")
        self.temp_label.place(x=450,y=250)
        self.temp_lbl = Label(self.root,text =f"{int(self.current)}°C" ,font=('Arial Black',28,'bold'),foreground="#259269",bg="White")
        self.temp_lbl.place(x=530,y=260)
        
        self.wind = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\wind.png")
        self.sub_wind = self.wind.subsample(2,2)
        self.wind_label = Label(self.root,image=self.sub_wind,bg="white")
        self.wind_label.place(x=800,y=250)
        speed_lbl = Label(self.root,text=f"{int(self.current_speed)} km\h",font=('Arial Black',28,'bold'),foreground="#259269",bg="White")
        speed_lbl.place(x=880,y=260)
        
        self.humudity = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\humidity.png")
        self.sub_humudity = self.humudity.subsample(2,2)
        self.humudity_label = Label(self.root,image=self.sub_humudity,bg="white")
        self.humudity_label.place(x=1200,y=250)
        humudity_lbl = Label(self.root,text="20%",font=('Arial Black',28,'bold'),foreground="#259269",bg="White")
        humudity_lbl.place(x=1280,y=260)
        
        self.sunrise = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\sunrise.png")
        self.sub_sunrise = self.sunrise.subsample(2,2)
        self.sunrise_label = Label(self.root,image=self.sub_sunrise,bg="white")
        self.sunrise_label.place(x=450,y=350)
        sunrise_lbl = Label(self.root,text=f"{self.sunrise_1}",font=('Arial Black',28,'bold'),foreground="#259269",bg="White")
        sunrise_lbl.place(x=530,y=360)
        
        self.solar_panel = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\solar-panel.png")
        self.sub_soler_panel_1 = self.solar_panel.subsample(2,2)
        self.solar_panel_label = Label(self.root,image=self.sub_soler_panel_1,bg="white")
        self.solar_panel_label.place(x=800,y=350)
        elec_label = Label(self.root,text=f"{int(self.power_1)} W\h",font=('Arial Black',28,'bold'),foreground="#FF5400",bg="White")
        elec_label.place(x=880,y=360)
        
        self.sunset = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\moonrise.png")
        self.sub_sunset = self.sunset.subsample(2,2)
        self.sunset_label = Label(self.root,image=self.sub_sunset,bg="white")
        self.sunset_label.place(x=1200,y=355)
        sunset_lbl = Label(self.root,text=f"{self.sunset_1}",font=('Arial Black',28,'bold'),foreground="#259269",bg="White")
        sunset_lbl.place(x=1270,y=360)
        
        
        
        # ============================================================== frame 3 ========================================================
        
        
        # ====================================== Photos ========================================
        self.temp1 = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\thermometer.png")
        self.sub_temp1 = self.temp1.subsample(4,4)
        
        self.wind1 = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\wind.png")
        self.sub_wind1 = self.wind.subsample(4,4)
        
        self.solar_panel = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\solar-panel.png")
        self.sub_soler_panel_2 = self.solar_panel.subsample(4,4)
        
        # ===============================================================================================================
        # -------day 1--------
        first_day = current_day + datetime.timedelta(1)
        first_day_lbl = Label(self.root,text=first_day.strftime("%A"),font=('Arial Black',28,'bold'),foreground="gold",bg="White")
        first_day_lbl.place(x=170,y=470)
        
        self.temp1_label = Label(self.root,image=self.sub_temp1,bg="white")
        self.temp1_label.place(x=130,y=530)
        temp1_lbl = Label(self.root,text=f"{int(self.day1_temp)}°C",font=('Arial Black',25,'bold'),foreground="#259269",bg="White")
        temp1_lbl.place(x=190,y=520)
        
        self.wind1_label = Label(self.root,image=self.sub_wind1,bg="white")
        self.wind1_label.place(x=130,y=570)
        speed1_lbl = Label(self.root,text=f"{int(self.day1_speed)} km\h",font=('Arial Black',25,'bold'),foreground="#259269",bg="White")
        speed1_lbl.place(x=190,y=560)
        
        self.solar_panel_label = Label(self.root,image=self.sub_soler_panel_2,bg="white")
        self.solar_panel_label.place(x=130,y=610)
        power2_label = Label(self.root,text=f"{int(self.power_2)} W\h",font=('Arial Black',25,'bold'),foreground="#FF5400",bg="White")
        power2_label.place(x=190,y=600)
        
        # -------day2--------
        second_day = first_day + datetime.timedelta(1)
        second_day_lbl = Label(self.root,text=second_day.strftime("%A"),font=('Arial Black',28,'bold'),foreground="gold",bg="White")
        second_day_lbl.place(x=415,y=470)
        
        self.temp2_label = Label(self.root,image=self.sub_temp1,bg="white")
        self.temp2_label.place(x=400,y=530)
        temp1_lbl = Label(self.root,text=f"{int(self.day2_temp)}°C",font=('Arial Black',25,'bold'),foreground="#259269",bg="White")
        temp1_lbl.place(x=460,y=520)
        
        self.wind2_label = Label(self.root,image=self.sub_wind1,bg="white")
        self.wind2_label.place(x=400,y=570)
        speed1_lbl = Label(self.root,text=f"{int(self.day2_speed)} km\h",font=('Arial Black',25,'bold'),foreground="#259269",bg="White")
        speed1_lbl.place(x=460,y=560)
        
        self.solar_panel_label = Label(self.root,image=self.sub_soler_panel_2,bg="white")
        self.solar_panel_label.place(x=400,y=610)
        power3_label = Label(self.root,text=f"{int(self.power_3)} W\h",font=('Arial Black',25,'bold'),foreground="#FF5400",bg="White")
        power3_label.place(x=460,y=600)
        
        
        # -------day 3--------
        third_day = second_day + datetime.timedelta(1)
        third_day_lbl = Label(self.root,text=third_day.strftime("%A"),font=('Arial Black',28,'bold'),foreground="gold",bg="White")
        third_day_lbl.place(x=680,y=470)
        
        self.temp3_label = Label(self.root,image=self.sub_temp1,bg="white")
        self.temp3_label.place(x=650,y=530)
        temp1_lbl = Label(self.root,text=f"{int(self.day3_temp)}°C",font=('Arial Black',25,'bold'),foreground="#259269",bg="White")
        temp1_lbl.place(x=710,y=520)
        
        self.wind3_label = Label(self.root,image=self.sub_wind1,bg="white")
        self.wind3_label.place(x=650,y=570)
        speed1_lbl = Label(self.root,text=f"{int(self.day3_speed)} km\h",font=('Arial Black',25,'bold'),foreground="#259269",bg="White")
        speed1_lbl.place(x=710,y=560)
        
        self.solar_panel_label = Label(self.root,image=self.sub_soler_panel_2,bg="white")
        self.solar_panel_label.place(x=650,y=610)
        power4_label = Label(self.root,text=f"{int(self.power_4)} W\h",font=('Arial Black',25,'bold'),foreground="#FF5400",bg="White")
        power4_label.place(x=710,y=600)
        
        # ------day 4---------
        fourth_day = third_day + datetime.timedelta(1)
        fourth_day_lbl = Label(self.root,text=fourth_day.strftime("%A"),font=('Arial Black',28,'bold'),foreground="gold",bg="White")
        fourth_day_lbl.place(x=920,y=470)
        
        self.temp1_label = Label(self.root,image=self.sub_temp1,bg="white")
        self.temp1_label.place(x=900,y=530)
        temp4_lbl = Label(self.root,text=f"{int(self.day4_temp)}°C",font=('Arial Black',25,'bold'),foreground="#259269",bg="White")
        temp4_lbl.place(x=960,y=520)
        
        self.wind4_label = Label(self.root,image=self.sub_wind1,bg="white")
        self.wind4_label.place(x=900,y=570)
        speed1_lbl = Label(self.root,text=f"{int(self.day4_speed)} km\h",font=('Arial Black',25,'bold'),foreground="#259269",bg="White")
        speed1_lbl.place(x=960,y=560)
        
        self.solar_panel_label = Label(self.root,image=self.sub_soler_panel_2,bg="white")
        self.solar_panel_label.place(x=900,y=610)
        power5_label = Label(self.root,text=f"{int(self.power_5)} W\h",font=('Arial Black',25,'bold'),foreground="#FF5400",bg="White")
        power5_label.place(x=960,y=600)
        
        # --------day 5-------
        fifth_day = fourth_day + datetime.timedelta(1)
        fifth_day_lbl = Label(self.root,text=fifth_day.strftime("%A"),font=('Arial Black',28,'bold'),foreground="gold",bg="White")
        fifth_day_lbl.place(x=1170,y=470)
        
        self.temp5_label = Label(self.root,image=self.sub_temp1,bg="white")
        self.temp5_label.place(x=1150,y=530)
        temp1_lbl = Label(self.root,text=f"{int(self.day5_temp)}°C",font=('Arial Black',25,'bold'),foreground="#259269",bg="White")
        temp1_lbl.place(x=1210,y=520)
        
        self.wind5_label = Label(self.root,image=self.sub_wind1,bg="white")
        self.wind5_label.place(x=1150,y=570)
        speed1_lbl = Label(self.root,text=f"{int(self.day5_speed)} km\h",font=('Arial Black',25,'bold'),foreground="#259269",bg="White")
        speed1_lbl.place(x=1210,y=560)
        
        self.solar_panel_label = Label(self.root,image=self.sub_soler_panel_2,bg="white")
        self.solar_panel_label.place(x=1150,y=610)
        power6_label = Label(self.root,text=f"{int(self.power_6)} W\h",font=('Arial Black',25,'bold'),foreground="#FF5400",bg="White")
        power6_label.place(x=1210,y=600) 
        
        # =============================================== third frame =====================================================
        info_h_label = Label(self.root,text="Hydrogen Information",font=("Arial Black",20,'bold'),foreground="gold",bg="white")
        info_h_label.place(x=600,y=680)
        
        self.Temperature_label = Label(self.root,font=('Arial Black',18,'bold'),foreground="#259269",bg="white")
        self.Temperature_label.place(x=180,y=720)
        self.Temperature_label.config(text=f"Hydrogen Temperature:  0°C")
        
        self.Humidity_label = Label(self.root,font=('Arial Black',18,'bold'),foreground="#259269",bg="white")
        self.Humidity_label.place(x=980,y=720)
        self.Humidity_label.config(text=f"Hydrogen Humidity:  0%")
        
        Volume_label = Label(self.root,text="Hydrogen Concentrate: 0 ppm",font=('Arial Black',18,'bold'),foreground="#259269",bg="white")
        Volume_label.place(x=580,y=760)
        
        self.check_internet_connection()
        self.Time = "11:59:59 PM"
        self.time()
        self.history()
        self.temp = []
        self.hydrogen_list = []
        self.humuidity_list = [0]
        self.t1 = continuous_threading.PeriodicThread(1,self.Temperature)
        self.t1.start()
        self.Add_data()
        
        
        
    def check_internet_connection(self):
        try:
            response = requests.get('https://www.google.com', timeout=5)
            if response.status_code == 200:
                print("True") 
            else:
                return False
        except requests.exceptions.RequestException:
            return messagebox.showwarning("WARNING","NO Internet Connection")
      
    def is_port_open(self):
            try:
                ports = ["COM6","COM5"]
                for x in range(0,2):
                    if  serial.Serial(ports[x]).is_open == True:
                        return ports[x]             
            except serial.SerialException:
               return ports[x+1]
           
                           
    def Temperature (self):
        try:   
                port = self.is_port_open()
                ser = serial.Serial(f"{port}",9600)
                while True:
                    self.root.update()          
                    line = ser.readline().decode("utf-8")
                    
                    sensor_values = re.findall(r"[0-9.]*\S",line)
                    self.temperature_1 = float(sensor_values[0])
                    self.temperature_H = float(sensor_values[1])
                    self.humuidity_1 = float(sensor_values[2])
                    self.humuidity_H = float(sensor_values[3])
                    self.hydrogen = int(sensor_values[4])
                    self.hydrogen2 = int(sensor_values[5])
                    
                    
                    self.temp_lbl = Label(self.root,font=('Arial Black',28,'bold'),foreground="#259269",bg="White")
                    self.temp_lbl.place(x=530,y=260)
                    self.temp_lbl.config(text=f"{self.temperature_1}°C")
                   
                    self.humudity_lbl = Label(self.root,font=('Arial Black',28,'bold'),foreground="#259269",bg="White")
                    self.humudity_lbl.place(x=1280,y=260)
                    self.humudity_lbl.config(text=f"{self.humuidity_1}%")
                        
                    
                    self.Temperature_label = Label(self.root,font=('Arial Black',18,'bold'),foreground="#259269",bg="white")
                    self.Temperature_label.place(x=180,y=720)
                    self.Temperature_label.config(text=f"Hydrogen Temperature:  {self.temperature_H}°C")
                    
                    self.Humidity_label = Label(self.root,font=('Arial Black',18,'bold'),foreground="#259269",bg="white")
                    self.Humidity_label.place(x=980,y=720)
                    self.Humidity_label.config(text=f"Hydrogen Humidity:  {self.humuidity_H}%")
                    
                    Volume_label = Label(self.root,text=f"Hydrogen Concentrate: {self.hydrogen} ppm",font=('Arial Black',18,'bold'),foreground="#259269",bg="white")
                    Volume_label.place(x=580,y=760) # 895
                    print(self.hydrogen2)
                    if 50 < self.hydrogen2:
                        print("Help")
                        url = "https://calling.api.sinch.com/calling/v1/callouts"
                        payload="{\n  \"method\": \"ttsCallout\",\n  \"ttsCallout\": {\n    \"cli\": \"+447520652429\",\n    \"domain\": \"pstn\",\n    \"destination\": {\n      \"type\": \"number\",\n      \"endpoint\": \"+201096923909\"\n    },\n    \"locale\": \"en-US\",\n    \"prompts\": \"#tts[There is a hydrogen gas leak. Please go to the hydrogen field to fix the problem]\"\n  }\n}"
                        headers = {
                        'Content-Type': 'application/json',
                        'Authorization': 'Basic YjgxNGE1OGUtMTkxMy00ZGZhLTgzN2YtZDJjMDE5YmRkYjIyOkxTeGdjTWcyaVVpaXB4SUg1anM1aWc9PQ=='
                        }
                        response = requests.request("POST", url, headers=headers, data=payload)
        
                    self.temp.sort()
                    self.temp.append(self.temperature_1)
                    self.hydrogen_list.append(self.hydrogen)
                    self.humuidity_list.append(self.humuidity_1)
                    self.max_temp = self.temp[-1]
                    self.Min_temp = self.temp[0]
                    self.hydrogen_production = sum(self.hydrogen_list)
                    self.Avg_humuidity = sum(self.humuidity_list) / len(self.humuidity_list)
                    month_2 = datetime.datetime.now().month
                    str_month =str(month_2)
                    data=pd.read_csv("D:\\Python\\Green_H2\\data_with_city.csv")
                    classifier = RandomForestClassifier(n_estimators=100,random_state=1)
                    x=data.iloc[:,:-1]
                    y=data.iloc[:,-1]
                    x_train ,x_test  , y_train , y_test = train_test_split(x,y,test_size=0.2,shuffle=False)
                    classifier.fit(x_train,y_train)
                    
                    test = pd.DataFrame({"month":[str_month],"precipitation":[0],"temp_max":[self.max_temp],"temp_min":[self.Min_temp],"wind":[self.current_speed]})
                    self.prediction = classifier.predict(test)[0]  
                    
                    if self.prediction == "rain" or self.prediction == "snow" or self.prediction == "drizzle":  
                            self.root.update()   
                            self.sun = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\cloudy-day.png")
                            self.sub_sun = self.sun.subsample(2,2)
                            sun_label = Label(self.root,image=self.sub_sun,bg="white")
                            sun_label.place(x=73,y=190)
                                        
                    elif self.prediction == "sun":
                                self.root.update() 
                                self.sun = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\sun.png")
                                self.sub_sun = self.sun.subsample(2,2)
                                sun_label = Label(self.root,image=self.sub_sun,bg="white")
                                sun_label.place(x=73,y=190)
                                
                    else:  
                            self.root.update() 
                            self.sun = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\sun.png")
                            self.sub_sun = self.sun.subsample(2,2)
                            sun_label = Label(self.root,image=self.sub_sun,bg="white")
                            sun_label.place(x=73,y=190)
                
        except: 
            messagebox.showerror("Error","Connection is Lost, Please Try Again and Refresh The Window")
            self.t1.close()
            
                
    def Add_data (self):
        while True:
            self.root.update()
            Time_now = strftime('%I:%M:%S %p')
            if self.Time == Time_now: 
                con = pymysql.connect( host="localhost", user="root", password="123456", database="Green_hydrogen")
                cur = con.cursor()   
                cur.execute("insert into Production values (%s,%s,%s,%s,%s,%s,%s)",(self.max_temp,
                                                                                    self.Min_temp,
                                                                                    int(self.Avg_humuidity),
                                                                                    Data().current_speed,
                                                                                    self.prediction,
                                                                                    Data().power_1,
                                                                                    self.hydrogen_production))
                con.commit()
                con.close()   
                self.temp.clear()
                self.hydrogen_list.clear()
                self.humuidity_list.clear()
                messagebox.showinfo("Information","Production Data, Has Now Been Added to the Database")
                
            else:
                continue 
            time.sleep(1)
            
   
  
    def Sunset(self,sunrise,sunset):
        result1 = re.findall(r"[0-9]+:[0-9]+",sunset)
        sunset_1 = result1[0]

        result2 = re.findall(r"[0-9]+:[0-9]+",sunrise)
        sunrise_1 = result2[0]
        return sunrise_1 ,sunset_1
        
    
    def Solar_Panel_Elec(self,sunrise,sunset,temperature):
        self.sunset_var = datetime.datetime.strptime(sunset,"%H:%M").time()    # time format
        self.sunrise_var = datetime.datetime.strptime(sunrise,"%I:%M").time()   # time format
        time1 = datetime.timedelta(hours=self.sunrise_var.hour,minutes=self.sunrise_var.minute)
        time2 = datetime.timedelta(hours=self.sunset_var.hour,minutes=self.sunset_var.minute)
        duration = time2-time1
        hours = duration.total_seconds()/3600.0 
            
        if temperature <= 24:
            elec = hours * 10.0   
        elif temperature > 24 :
            diff = temperature - 24   # subtract current temp from 24
            amount_of_inefficiency = 1 - (diff * 0.004) # multiply diff in amount of inefficiency and subtract from 1 to have the final result 
            elec = 10.0 * hours * amount_of_inefficiency
        return elec
    
    
    def time(self):
        self.date = strftime('%I:%M:%S %p')
        self.date_lbl = Label(self.root,font =('Arial Black',20,'bold'),foreground='white',bg="#0D0D0D")
        self.date_lbl.place(x=20,y=10)
        self.date_lbl.config(text= self.date)
        self.date_lbl.after(1000,self.time)
    
    def history(self):
        self.hist =  strftime("%d-%m-%Y")
        self.hist_lbl = Label(self.root,font=('Arial Black',20,'bold'),foreground="white",bg="#0D0D0D")
        self.hist_lbl.place(x=1350,y=10)
        self.hist_lbl.config(text=self.hist)
        self.hist_lbl.after(1000,self.history)
    
    def home(self):
        self.root.destroy()
        self.main_window.root.deiconify()
        sys.exit()
    
    def Database(self):
        from Third_interface import Database
        self.root.destroy()
        self.third_window = Database(self.main_window)
        
        
    def Refresh(self):
        self.root.withdraw()
        self.second_window = Weather(self)
        
        
    def Exit_func(self):
            self.ques =  messagebox.askyesno("EXIT","Do You Yeally Want to Exit?")
            if self.ques == 1:
                self.root.destroy()
                sys.exit()
            else: 
                return