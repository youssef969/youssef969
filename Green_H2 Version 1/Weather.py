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


#259269
#31c48e
class Wheather:
    def __init__(self,main_window):
        #self.root.state("zoomed")
        #self.main_window = main_window
        self.root = root
        #self.root = Toplevel()
        self.root.geometry("950x650+350+50")   # 950x550
        self.root.resizable(True,True)
        self.root.config(bg="#259269")
        self.root.title("Weather")
        self.root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\1710162623466-removebg-preview.ico")
    
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
        
       
        
        # ================================================= first_interface ========================================
        
        self.fr1 = Frame(self.root,bg="#27AE60")
        self.fr1.place(x=50,y=0,width=900,height=80)
       
        fr2 = Frame(self.root,bg="#7DCEA0")
        fr2.place(x=0,y=0,width=50,height=650)
        
        self.image = PhotoImage(file ="C:\\Users\\Computec\\Downloads\\PNG Icons\\1710162623466-removebg-preview.png")
        self.sub = self.image.subsample(5,5)
        image_label = Label(self.fr1,image=self.sub,bg="#27AE60")
        image_label.place(x=810,y=0)
        
        GreenH = Label(self.fr1,text="Green Hydorgen",fg="white",font=("Pacifico",19,"bold"),bg="#27AE60")
        GreenH.place(x=590,y=7)
        
        self.Home = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\home.png")
        self.sub_home = self.Home.subsample(5,5)
        Home_button = Button(fr2,image=self.sub_home,bd=0,bg="#7DCEA0",justify="center",activebackground="#7DCEA0",command=self.home)
        Home_button.place(x=10,y=20,width=30,height=60)
        
        self.weather = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\rainy-day 2.png")
        self.sub_weather = self.weather.subsample(5,5)
        weather_button_1 =  Button(fr2,image=self.sub_weather,bd=0,bg="#7DCEA0",justify="center",activebackground="#7DCEA0")
        weather_button_1.place(x=10,y=80,width=30,height=60)
        
        self.monitor = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Monitor.png")
        self.sub_monitor = self.monitor.subsample(5,5)
        Monitor_button =  Button(fr2,image=self.sub_monitor,bd=0,bg="#7DCEA0",justify="center",activebackground="#7DCEA0",command=self.Monitor)
        Monitor_button.place(x=10,y=140,width=30,height=60)
        
        self.database = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\database (1).png")
        self.sub_database = self.database.subsample(5,5)
        database_button = Button(fr2,image=self.sub_database,bd=0,bg="#7DCEA0",justify="center",activebackground="#7DCEA0",command=self.Database)
        database_button.place(x=10,y=200,width=30,height=60)
        
        self.Settings = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\gear.png")
        self.sub_Settings = self.Settings.subsample(5,5)
        Settings_button = Button(fr2,image=self.sub_Settings,bd=0,bg="#7DCEA0",justify="center",activebackground="#7DCEA0")
        Settings_button.place(x=10,y=260,width=30,height=60)
        
        self.refresh = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\reload.png")
        self.sub_refresh = self.refresh.subsample(5,5)
        refresh_button = Button(fr2,image=self.sub_refresh,bd=0,bg="#7DCEA0",justify="center",activebackground="#7DCEA0",command=self.Refresh)
        refresh_button.place(x=10,y=320,width=30,height=60)
        
        self.Exit = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\logout.png")
        self.sub_Exit = self.Exit.subsample(5,5)
        Exit_button = Button(fr2,image=self.sub_Exit,bd=0,bg="#7DCEA0",justify="center",activebackground="#7DCEA0",command=self.Exit_func )
        Exit_button.place(x=13,y=380,width=30,height=65)
        
    
        # ============================================ Frame ======================================================
        line = Frame(self.root,bg="white")
        line.place(x=75,y=300,width=850,height=5)
        
        self.fr3 = Frame(self.root,bg="#259269")
        self.fr3.place(x=50,y=305,width=900,height=350)
        
        line2 = Frame(self.fr3,bg="white")
        line2.place(x=25,y=220,width=850,height=5)
        #=============================================================== photo Image ====================================================
        
        # self.turbine = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\wind-turbine.png")
        # self.sub_turbine = self.turbine.subsample(3,3)
        # back_gturbine = Label(self.root,image=self.sub_turbine,bg="#259269")
        # back_gturbine.place(x=60,y=103)
        
        self.cloud = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\sun (1).png")
        self.sub_cloud = self.cloud.subsample(3,3)
        cloud_label = Label(self.root,image=self.sub_cloud,bg="#259269")
        cloud_label.place(x=770,y=90)
        
        self.temp = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\thermometer.png")
        self.sub_temp = self.temp.subsample(3,3)
        self.temp_label = Label(self.root,image=self.sub_temp,bg="#259269")
        self.temp_label.place(x=140,y=165)
        
        self.wind = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\wind.png")
        self.sub_wind = self.wind.subsample(3,3)
        self.wind_label = Label(self.root,image=self.sub_wind,bg="#259269")
        self.wind_label.place(x=360,y=165)
        
        self.humudity = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\humidity.png")
        self.sub_humudity = self.humudity.subsample(3,3)
        self.humudity_label = Label(self.root,image=self.sub_humudity,bg="#259269")
        self.humudity_label.place(x=620,y=165)
        
        self.sunrise = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\sunrise.png")
        self.sub_sunrise = self.sunrise.subsample(3,3)
        self.sunrise_label = Label(self.root,image=self.sub_sunrise,bg="#259269")
        self.sunrise_label.place(x=230,y=230)
        
        self.sunset = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\moonrise.png")
        self.sub_sunset = self.sunset.subsample(3,3)
        self.sunset_label = Label(self.root,image=self.sub_sunset,bg="#259269")
        self.sunset_label.place(x=490,y=230)
        
        self.solar_panel = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\solar-panel.png")
        self.sub_solar_panel = self.solar_panel.subsample(3,3)
        self.solar_panel_label = Label(self.root,image=self.sub_solar_panel,bg="#259269")
        self.solar_panel_label.place(x=60,y=90)


        # ================================================= Labels =======================================================  
        City = Label(self.root,text="< Egypt \ AL Dakahlia >",font=('Stincil',15,'bold'),foreground="white",bg="#259269")
        City.place(x=400,y=80)
        
        self.temp_lbl = Label(self.root,text =f"{int(self.current)}°C" ,font=('Stincil',28,'bold'),foreground="white",bg="#259269")
        self.temp_lbl.place(x=190,y=160)
        
        
        speed_lbl = Label(self.root,text=f"{int(self.current_speed)}km/h",font=('Stincil',28,'bold'),foreground="white",bg="#259269")
        speed_lbl.place(x=410,y=160)
        
        
        humudity_lbl = Label(self.root,text="50%",font=('Stincil',28,'bold'),foreground="white",bg="#259269")
        humudity_lbl.place(x=675,y=160)
        
        sunrise_lbl = Label(self.root,text=f"{self.sunrise_1}",font=('Stincil',28,'bold'),foreground="white",bg="#259269")
        sunrise_lbl.place(x=300,y=230)
        
        sunset_lbl = Label(self.root,text=f"{self.sunset_1}",font=('Stincil',28,'bold'),foreground="white",bg="#259269")
        sunset_lbl.place(x=550,y=230)
        
        elec_label = Label(self.root,text=f"{int(self.power_1)}W\h",font=('Stincil',18,'bold'),foreground="#FF5400",bg="#259269")
        elec_label.place(x=110,y=100)

        # ======================================================== Bottem Frame =================================================
        current_day = datetime.datetime.now()
        today = Label(self.root,text=current_day.strftime("%A"),font=('Stincil',15,'bold'),foreground="gold",bg="#259269")
        today.place(x=480,y=110)
        
        # ====================================== Photos ========================================
        self.temp1 = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\thermometer.png")
        self.sub_temp1 = self.temp1.subsample(5,5)
        
        self.wind1 = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\wind.png")
        self.sub_wind1 = self.wind.subsample(5,5)
        
        # ===============================================================================================================
        # -------day 1--------
        self.temp1_label = Label(self.fr3,image=self.sub_temp1,bg="#259269")
        self.temp1_label.place(x=80,y=60)
        temp1_lbl = Label(self.fr3,text=f"{int(self.day1_temp)}°C",font=('Stincil',18,'bold'),foreground="white",bg="#259269")
        temp1_lbl.place(x=115,y=58)
        
        self.wind1_label = Label(self.fr3,image=self.sub_wind1,bg="#259269")
        self.wind1_label.place(x=80,y=110)
        speed1_lbl = Label(self.fr3,text=f"{int(self.day1_speed)}km/h",font=('Stincil',18,'bold'),foreground="white",bg="#259269")
        speed1_lbl.place(x=115,y=108)
        
        self.solar_panel_label = Label(self.fr3,image=self.sub_solar_panel,bg="#259269")
        self.solar_panel_label.place(x=70,y=158)
        power2_label = Label(self.fr3,text=f"{int(self.power_2)}W\h",font=('Stincil',18,'bold'),foreground="#FF5400",bg="#259269")
        power2_label.place(x=120,y=165)
        
        first_day = current_day + datetime.timedelta(1)
        first_day_lbl = Label(self.fr3,text=first_day.strftime("%A"),font=('Stincil',15,'bold'),foreground="gold",bg="#259269")
        first_day_lbl.place(x=90,y=20)
        # -------day2--------
        self.temp2_label = Label(self.fr3,image=self.sub_temp1,bg="#259269")
        self.temp2_label.place(x=230,y=60)
        temp1_lbl = Label(self.fr3,text=f"{int(self.day2_temp)}°C",font=('Stincil',18,'bold'),foreground="white",bg="#259269")
        temp1_lbl.place(x=265,y=58)
        
        self.wind2_label = Label(self.fr3,image=self.sub_wind1,bg="#259269")
        self.wind2_label.place(x=230,y=110)
        speed1_lbl = Label(self.fr3,text=f"{int(self.day2_speed)}km/h",font=('Stincil',18,'bold'),foreground="white",bg="#259269")
        speed1_lbl.place(x=265,y=108)
        
        self.solar_panel_label = Label(self.fr3,image=self.sub_solar_panel,bg="#259269")
        self.solar_panel_label.place(x=220,y=158)
        power3_label = Label(self.fr3,text=f"{int(self.power_3)}W\h",font=('Stincil',18,'bold'),foreground="#FF5400",bg="#259269")
        power3_label.place(x=270,y=165)
        
        second_day = first_day + datetime.timedelta(1)
        second_day_lbl = Label(self.fr3,text=second_day.strftime("%A"),font=('Stincil',15,'bold'),foreground="gold",bg="#259269")
        second_day_lbl.place(x=240,y=20)
        # -------day 3--------
        self.temp3_label = Label(self.fr3,image=self.sub_temp1,bg="#259269")
        self.temp3_label.place(x=380,y=60)
        temp1_lbl = Label(self.fr3,text=f"{int(self.day3_temp)}°C",font=('Stincil',18,'bold'),foreground="white",bg="#259269")
        temp1_lbl.place(x=415,y=58)
        
        self.wind3_label = Label(self.fr3,image=self.sub_wind1,bg="#259269")
        self.wind3_label.place(x=380,y=110)
        speed1_lbl = Label(self.fr3,text=f"{int(self.day3_speed)}km/h",font=('Stincil',18,'bold'),foreground="white",bg="#259269")
        speed1_lbl.place(x=415,y=108)
        
        self.solar_panel_label = Label(self.fr3,image=self.sub_solar_panel,bg="#259269")
        self.solar_panel_label.place(x=370,y=158)
        power4_label = Label(self.fr3,text=f"{int(self.power_4)}W\h",font=('Stincil',18,'bold'),foreground="#FF5400",bg="#259269")
        power4_label.place(x=420,y=165)
        
        third_day = second_day + datetime.timedelta(1)
        third_day_lbl = Label(self.fr3,text=third_day.strftime("%A"),font=('Stincil',15,'bold'),foreground="gold",bg="#259269")
        third_day_lbl.place(x=390,y=20)
        # ------day 4---------
        self.temp1_label = Label(self.fr3,image=self.sub_temp1,bg="#259269")
        self.temp1_label.place(x=530,y=60)
        temp4_lbl = Label(self.fr3,text=f"{int(self.day4_temp)}°C",font=('Stincil',18,'bold'),foreground="white",bg="#259269")
        temp4_lbl.place(x=565,y=58)
        
        self.wind4_label = Label(self.fr3,image=self.sub_wind1,bg="#259269")
        self.wind4_label.place(x=530,y=110)
        speed1_lbl = Label(self.fr3,text=f"{int(self.day4_speed)}km/h",font=('Stincil',18,'bold'),foreground="white",bg="#259269")
        speed1_lbl.place(x=565,y=108)
        
        self.solar_panel_label = Label(self.fr3,image=self.sub_solar_panel,bg="#259269")
        self.solar_panel_label.place(x=520,y=158)
        power5_label = Label(self.fr3,text=f"{int(self.power_5)}W\h",font=('Stincil',18,'bold'),foreground="#FF5400",bg="#259269")
        power5_label.place(x=570,y=165)
        
        fourth_day = third_day + datetime.timedelta(1)
        fourth_day_lbl = Label(self.fr3,text=fourth_day.strftime("%A"),font=('Stincil',15,'bold'),foreground="gold",bg="#259269")
        fourth_day_lbl.place(x=540,y=20)
        # --------day 5-------
        self.temp5_label = Label(self.fr3,image=self.sub_temp1,bg="#259269")
        self.temp5_label.place(x=680,y=60)
        temp1_lbl = Label(self.fr3,text=f"{int(self.day5_temp)}°C",font=('Stincil',18,'bold'),foreground="white",bg="#259269")
        temp1_lbl.place(x=715,y=58)
        
        self.wind5_label = Label(self.fr3,image=self.sub_wind1,bg="#259269")
        self.wind5_label.place(x=680,y=110)
        speed1_lbl = Label(self.fr3,text=f"{int(self.day5_speed)}km/h",font=('Stincil',18,'bold'),foreground="white",bg="#259269")
        speed1_lbl.place(x=715,y=108)
        
        self.solar_panel_label = Label(self.fr3,image=self.sub_solar_panel,bg="#259269")
        self.solar_panel_label.place(x=670,y=158)
        power6_label = Label(self.fr3,text=f"{int(self.power_6)}W\h",font=('Stincil',18,'bold'),foreground="#FF5400",bg="#259269")
        power6_label.place(x=720,y=165)
        
        fifth_day = fourth_day + datetime.timedelta(1)
        fifth_day_lbl = Label(self.fr3,text=fifth_day.strftime("%A"),font=('Stincil',15,'bold'),foreground="gold",bg="#259269")
        fifth_day_lbl.place(x=690,y=20)
        
       
        self.Temperature_label = Label(self.fr3,font=('Stincil',15,'bold'),foreground="white",bg="#259269")
        self.Temperature_label.place(x=540,y=270)
        self.Temperature_label.config(text=f"Hydrogen Temperature:  {0}°C")
        
        self.Humidity_label = Label(self.fr3,font=('Stincil',15,'bold'),foreground="white",bg="#259269")
        self.Humidity_label.place(x=40,y=270)
        self.Humidity_label.config(text=f"Hydrogen Humidity:  {0}%")
        
        Volume_label = Label(self.fr3,text="Hydrogen Concentrate: 0 ppm",font=('Stincil',15,'bold'),foreground="white",bg="#259269")
        Volume_label.place(x=300,y=310)
        
        Volume_label = Label(self.fr3,text="Hydrogen Information",font=("Stincil",15,'bold'),foreground="gold",bg="#259269")
        Volume_label.place(x=320,y=225)
        
        
        self.temp = []
        self.time()
        self.history()
        self.t1 = continuous_threading.PeriodicThread(2,self.Temperature)
        self.t1.start()
        
   
    def time(self):
        self.date = strftime('%I:%M:%S %p')
        self.date_lbl = Label(self.fr1,font =('calibri',20,'bold'),foreground='white',bg="#27AE60")
        self.date_lbl.place(x=20,y=5)
        self.date_lbl.config(text= self.date)
        self.date_lbl.after(1000,self.time)
            
    def history(self):
        self.hist =  strftime("%d/%m/%Y")
        self.hist_lbl = Label(self.fr1,font=('calibri',20,'bold'),foreground="white",bg="#27AE60")
        self.hist_lbl.place(x=20,y=40)
        self.hist_lbl.config(text=self.hist)
        self.hist_lbl.after(1000,self.history)
        
    def Temperature (self):
            #try:
                ser = serial.Serial('COM5',9600)
                line = ser.readline().decode("utf-8")
                if ser.is_open == True:
                    self.temperature = line[36:38]
                    self.temp_lbl = Label(self.root,font=('Stincil',28,'bold'),foreground="white",bg="#259269")
                    self.temp_lbl.place(x=190,y=165)
                    self.temp_lbl.config(text=f"{self.temperature}°C")
                    self.humuidity = line[10:12]
                    self.humudity_lbl = Label(self.root,text=f"{self.humuidity}%",font=('Stincil',28,'bold'),foreground="white",bg="#259269")
                    self.humudity_lbl.place(x=675,y=165)
                        
                    self.temperature_2 = line[41:46]
                    self.Temperature_label = Label(self.fr3,font=('Stincil',15,'bold'),foreground="white",bg="#259269")
                    self.Temperature_label.place(x=540,y=270)
                    self.Temperature_label.config(text=f"Hydrogen Temperature:  {self.temperature_2}°C")
                    self.humuidity_2 = line[15:20]
                    self.Humidity_label = Label(self.fr3,font=('Stincil',15,'bold'),foreground="white",bg="#259269")
                    self.Humidity_label.place(x=40,y=270)
                    self.Humidity_label.config(text=f"Hydrogen Humidity:  {self.humuidity_2}%")
                    self.hydrogeen = line[76:79]
                    Volume_label = Label(self.fr3,text=f"Hydrogen Concentrate:  {self.hydrogeen} ppm",font=('Stincil',15,'bold'),foreground="white",bg="#259269")
                    Volume_label.place(x=300,y=310)

                    float_temp = float(self.temperature)
                    self.temp.sort()
                    self.temp.append(float_temp)
                    max_temp = self.temp[-1]
                    Min_temp = self.temp[0]
                    month_2 = datetime.datetime.now().month
                    str_month =str(month_2)
                    float_temp = float(self.temperature)
                    self.temp.sort()
                    self.temp.append(float_temp)
                    max_temp = self.temp[-1]
                    Min_temp = self.temp[0]
                    data=pd.read_csv("D:\\Python\\Green_H2\\data_with_city.csv")
                    classifier = RandomForestClassifier(n_estimators=100,random_state=1)
                    x=data.iloc[:,:-1]
                    y=data.iloc[:,-1]
                    x_train ,x_test  , y_train , y_test = train_test_split(x,y,test_size=0.2,shuffle=False)
                    classifier.fit(x_train,y_train)
                    
                    test = pd.DataFrame({"month":[str_month],"precipitation":[0],"temp_max":[max_temp],"temp_min":[Min_temp],"wind":[self.current_speed]})
                    self.prediction = classifier.predict(test)[0] 
                    print(self.prediction) 
                    # data = pd.read_csv("D:\\Python\\Green_H2\\seattle-weather.csv")
                    # data.drop(columns=['date'],inplace=True)
                    # mapping_dict = {'snow':"cloudy", 'rain':"cloudy", "sun":"sun", "fog":"fog"}
                    # data["desc"] = data.weather.map(mapping_dict)
                    # data.dropna(axis=0,inplace=True)
                    # data.drop(columns=["weather"],inplace=True)
                    # classifier = RandomForestClassifier(n_estimators=100,random_state=1)
                    # x=data.iloc[:,:-1]
                    # y=data.iloc[:,-1]
                    # x_train ,x_test  , y_train , y_test = train_test_split(x,y,test_size=0.2,shuffle=False)
                    # classifier.fit(x_train,y_train)
                    # test = pd.DataFrame({"precipitation":[self.humuidity],"temp_max":[max_temp],"temp_min":[Min_temp],"wind":[4.166]})
                    # prediction =classifier.predict(test)[0]
                    
                   
                    if self.prediction == 'rain'or 'snow' or 'drizzle':  
                                self.root.update()   
                                self.cloud = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\cloudy-day.png")
                                self.sub_cloud = self.cloud.subsample(3,3)
                                cloud_label = Label(self.root,image=self.sub_cloud,bg="#259269")
                                cloud_label.place(x=770,y=90)
                                
                    elif self.prediction == "sun":
                            self.root.update() 
                            self.sunny = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\sun (1).png")
                            self.sub_sunny = self.sunny.subsample(3,3)
                            sunny_label = Label(self.root,image=self.sub_sunny,bg="#259269")
                            sunny_label.place(x=770,y=90)  
                    else:  
                        self.root.update() 
                        self.cloud = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\sun (1).png")
                        self.sub_cloud = self.cloud.subsample(3,3)
                        cloud_label = Label(self.root,image=self.sub_cloud,bg="#259269")
                        cloud_label.place(x=770,y=90)  
                # else:
                #     self.t1.close()
                #     messagebox.showerror("Error","Connection lost, please Try Again")
                    
                    
            # except:
            #     self.t1.stop()
            #     messagebox.showerror("Error","Connection lost, please Try Again!")
                
                
                    
                
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
    
    
    def home(self):
        self.root.destroy()
        self.main_window.root.deiconify()
        
            
    def Monitor(self):
        self.t1.stop()
        from monitor import Monitor
        self.root.withdraw()  
        self.third_window = Monitor(self.main_window) 
        
        
    def Database(self):
        from database import Database
        self.root.withdraw()  
        self.third_window = Database(self.main_window) 
           
    def Refresh(self): 
        self.root.withdraw()  
        self.third_window = Wheather(self.main_window)
        
        
    def Exit_func(self):
        self.ques =  messagebox.askyesno("EXIT","Do you really want to Exit")
        if self.ques == 1:
            self.root.destroy()
        else: 
            return    
         
root = Tk()       
ob = Wheather(root)
root.mainloop()