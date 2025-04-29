from tkinter import PhotoImage ,Label , messagebox
from time import strftime
from customtkinter import *
import datetime
import requests
import re
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
import PIL.Image
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pywhatkit as kit
import pygame


class Weather():
    def __init__(self,main_window):
        self.main_window = main_window
        self.root = CTkToplevel()
        self.root.state("zoomed")
        self.root.resizable(True,True)
        self.root.config(bg="#0d0d0d")
        self.root.title("Green Hydrogen")
        self.root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\3-removebg-preview_1.ico")
        self.root.minsize(1550,800)
        
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
        self.Frame = CTkFrame(self.root,width=1550,height=1000,corner_radius=180,bg_color="#0d0d0d")
        self.Frame.place(x=-7,y=150)
        
        self.Frame2 = CTkFrame(self.root,width=300,height=70,corner_radius=90,bg_color="#0d0d0d",fg_color="#1d1d1d")
        self.Frame2.place(x=600,y=0)
        
        
        self.Frame3 = CTkScrollableFrame(self.root,width=1515,height=360,bg_color="#dbdbdb",fg_color="#dbdbdb")
        self.Frame3.place(x=0,y=430)
        
        self.shape = CTkFrame(self.root,width=300,height=70,corner_radius=90,bg_color="#dbdbdb",fg_color="black")
        self.shape.place(x=640,y=170)
        
        # ============================================== Frame 1 =================================================== 
        self.image = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\3-removebg-preview.png")
        self.sub = CTkImage(light_image=self.image,dark_image=self.image,size=(60,60))
        self.image_label = CTkLabel(self.Frame2,image=self.sub,fg_color="#1d1d1d",text="")
        self.image_label.place(x=25,y=5)
        
        self.GreenH = CTkLabel(self.Frame2,text="Green Hydorgen",text_color="white",font=("Pacifico",22,"bold"),fg_color="#1d1d1d")
        self.GreenH.place(x=105,y=10)
        
        self.Home = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\home_white.png")
        self.Home2 = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\home_black.png")

        self.sub_home = CTkImage(light_image=self.Home,size=(25,25),dark_image=self.Home2)
        self.Home_button = CTkButton(self.root,text="  Home",image=self.sub_home,bg_color="#0d0d0d",hover_color="#2b2b2b",fg_color="#0d0d0d",text_color="white",compound="left",font=("Arial Black",15,"bold"),width=110,height=50,corner_radius=90,command=self.home)
        self.Home_button.place(x=300,y=90)
        
        self.weather = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\dashboard_green.png")
        self.sub_weather = CTkImage(light_image=self.weather,size=(35,35),dark_image=self.weather)
        self.Weather_button = CTkButton(self.root,text="  Monitor",image=self.sub_weather,bg_color="#0d0d0d",hover_color="#2b2b2b",fg_color="#0d0d0d",text_color="#27AE60",compound="left",font=("Arial Black",15,"bold"),width=110,height=50,corner_radius=90)
        self.Weather_button.place(x=450,y=90)
        
        self.database = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\database_white.png")
        self.database2 = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\database_black.png")
        self.sub_database = CTkImage(light_image=self.database,size=(25,25),dark_image=self.database2)
        self.database_button = CTkButton(self.root,text="  Database",image=self.sub_database,bg_color="#0d0d0d",hover_color="#2b2b2b",fg_color="#0d0d0d",text_color="white",compound="left",font=("Arial Black",15,"bold"),width=110,height=50,corner_radius=90,command=self.Database)
        self.database_button.place(x=620,y=90)
        
        self.refresh = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\refresh_white.png")
        self.refresh2 = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\refresh_black.png")
        self.sub_refresh = CTkImage(light_image=self.refresh,size=(25,25),dark_image=self.refresh2)
        self.refresh_button = CTkButton(self.root,text="  Refresh",image=self.sub_refresh,bg_color="#0d0d0d",hover_color="#2b2b2b",fg_color="#0d0d0d",text_color="white",compound="left",font=("Arial Black",15,"bold"),width=110,height=50,corner_radius=90,command=self.Refresh)
        self.refresh_button.place(x=800,y=90)
        
        
        self.Setting = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\setting_white.png")
        self.Setting2 = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\setting_black.png")
        self.sub_Setting = CTkImage(light_image=self.Setting,size=(25,25),dark_image=self.Setting2)
        self.Setting_button = CTkButton(self.root,text="  Settings",image=self.sub_Setting,bg_color="#0d0d0d",hover_color="#2b2b2b",fg_color="#0d0d0d",text_color="white",compound="left",font=("Arial Black",15,"bold"),width=110,height=50,corner_radius=90,command=self.setting)
        self.Setting_button.place(x=970,y=90)
        
        self.Exit = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\logout_white.png")
        self.Exit2 = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\logout_black.png")
        self.sub_Exit = CTkImage(light_image=self.Exit,size=(25,25),dark_image=self.Exit2)
        self.Exit_button = CTkButton(self.root,text="  Exit",image=self.sub_Exit,bg_color="#0d0d0d",hover_color="#2b2b2b",fg_color="#0d0d0d",text_color="white",compound="left",font=("Arial Black",15,"bold"),width=110,height=50,corner_radius=90,command=self.Exit_func)
        self.Exit_button.place(x=1140,y=90)
        
        self.date_lbl = CTkLabel(self.root,font =('Arial Black',20,'bold'),text_color='white',fg_color="#0D0D0D",bg_color="#0D0D0D")
        self.hist_lbl = CTkLabel(self.root,font =('Arial Black',20,'bold'),text_color='white',fg_color="#0D0D0D",bg_color="#0D0D0D")
        
        
        # ======================================================= Frame 2 =================================================================
        
        self.city = CTkLabel(self.root,text="< Egypt \ AL Dakahlia >",font=("Arial Black",18,"bold"),bg_color="#0D0D0D",text_color="#27AE60")
        self.city.place(x=680,y=175)
        current_day = datetime.datetime.now()
        self.today = CTkLabel(self.root,text=current_day.strftime("%A"),font=('Arial Black',18,'bold'),text_color="gold",bg_color="#0D0D0D")
        self.today.place(x=750,y=205)
        
        self.sun = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\sun.png")
        self.sub_sun = CTkImage(light_image=self.sun,size=(230,230),dark_image=self.sun)
        self.sun_label = CTkLabel(self.root,image=self.sub_sun,fg_color="#dbdbdb",text="",bg_color="#dbdbdb")
        self.sun_label.place(x=73,y=190)         
        
        self.temp = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\thermometer.png")
        self.sub_temp = CTkImage(light_image=self.temp,size=(50,50),dark_image=self.temp)
        self.temp_label = CTkLabel(self.root,image=self.sub_temp,fg_color="#dbdbdb",text="",bg_color="#dbdbdb")
        self.temp_label.place(x=400,y=250)
        self.temp_lbl = CTkLabel(self.root,text =f"{int(self.current)}°C" ,font=('Arial Black',28,'bold'),text_color="#259269",fg_color="#dbdbdb")
        self.temp_lbl.place(x=470,y=260)
        
        self.wind = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\wind.png")
        self.sub_wind = CTkImage(light_image=self.wind,size=(50,50),dark_image=self.wind)
        self.wind_label = CTkLabel(self.root,image=self.sub_wind,fg_color="#dbdbdb",text="",bg_color="#dbdbdb")
        self.wind_label.place(x=750,y=250)
        self.speed_lbl = CTkLabel(self.root,text=f"{int(self.current_speed)} km\h",font=('Arial Black',28,'bold'),text_color="#259269",fg_color="#dbdbdb")
        self.speed_lbl.place(x=820,y=260)
        
        self.humudity = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\humidity.png")
        self.sub_humudity = CTkImage(light_image=self.humudity,size=(50,50),dark_image=self.humudity)
        self.humudity_label = CTkLabel(self.root,image=self.sub_humudity,fg_color="#dbdbdb",text="",bg_color="#dbdbdb")
        self.humudity_label.place(x=1150,y=250)
        self.humudity_lbl = CTkLabel(self.root,text="20%",font=('Arial Black',28,'bold'),text_color="#259269",fg_color="#dbdbdb")
        self.humudity_lbl.place(x=1220,y=260)
        
        self.sunrise = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\sunrise.png")
        self.sub_sunrise = CTkImage(light_image=self.sunrise,size=(50,50),dark_image=self.sunrise)
        self.sunrise_label = CTkLabel(self.root,image=self.sub_sunrise,fg_color="#dbdbdb",text="",bg_color="#dbdbdb")
        self.sunrise_label.place(x=400,y=350)
        self.sunrise_lbl = CTkLabel(self.root,text=f"{self.sunrise_1}",font=('Arial Black',28,'bold'),text_color="#259269",fg_color="#dbdbdb")
        self.sunrise_lbl.place(x=470,y=360)
        
        self.solar_panel = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\solar-panel.png")
        self.sub_soler_panel_1 = CTkImage(light_image=self.solar_panel,size=(50,50),dark_image=self.solar_panel)
        self.solar_panel_label_1 = CTkLabel(self.root,image=self.sub_soler_panel_1,fg_color="#dbdbdb",text="",bg_color="#dbdbdb")
        self.solar_panel_label_1.place(x=750,y=350)
        self.elec_label = CTkLabel(self.root,text=f"{int(self.power_1)} W\h",font=('Arial Black',28,'bold'),text_color="#ff5400",fg_color="#dbdbdb")
        self.elec_label.place(x=820,y=360)
        
        self.sunset = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\moonrise.png")
        self.sub_sunset = CTkImage(light_image=self.sunset,size=(50,50),dark_image=self.sunset)
        self.sunset_label = CTkLabel(self.root,image=self.sub_sunset,fg_color="#dbdbdb",text="",bg_color="#dbdbdb")
        self.sunset_label.place(x=1150,y=355)
        self.sunset_lbl = CTkLabel(self.root,text=f"{self.sunset_1}",font=('Arial Black',28,'bold'),text_color="#259269",fg_color="#dbdbdb")
        self.sunset_lbl.place(x=1220,y=360)
        
        # ============================================================== frame 3 ========================================================
        self.datavisulization_label = CTkLabel(self.Frame3,text="Data Visualization",text_color="#259269",font=("Pacifico",22,"bold"),fg_color="#dbdbdb")
        self.datavisulization_label.pack(side=TOP,pady=5)
        
        self.fig = Figure(figsize=(20, 4), dpi=100)
        self.plot = self.fig.add_subplot(111)
        self.line, = self.plot.plot([], [],label="Hydrogen Production (PPM)",color="black",linewidth=3)
        self.line3, = self.plot.plot([],[],color="r",label="Temperature (°C)",marker="o",linestyle="--")
        self.line4, = self.plot.plot([],[],color="b",label="Hydrogen Himuidity (%)",marker="o",linestyle="--")
        self.fig.patch.set_facecolor("#dbdbdb")
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.Frame3)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=TOP,fill=BOTH)          
        self.plot.grid()
        self.plot.set_title("Plot Graph",fontsize=15)
        self.plot.set_ylabel("Hydrogen Production (PPM)",fontsize=12,fontname="Arial")
        self.plot.set_xlabel("Seconds",fontsize=12,fontname="Arial")
        self.plot.legend()
        #plt.style.use("_classic_test_patch")
        

        # ======================================================== Hydrogen frame ==============================
        
        self.line1 = CTkFrame(self.Frame3,width=1300,height=5,fg_color="black")
        self.line1.pack(side=TOP,pady=5,fill=Y) 
        
        self.frame5 = CTkFrame(self.Frame3,width=1500,height=360)
        self.frame5.pack(side=BOTTOM,pady=10)
        
        self.line2 = CTkFrame(self.Frame3,width=1300,height=5,fg_color="black")
        self.line2.pack(side=BOTTOM,pady=5)
        
        self.frame_hydrogeninfo = CTkFrame(self.Frame3,width=1500,height=140,fg_color=("#dbdbdb","#2b2b2b"))
        self.frame_hydrogeninfo.pack(side=BOTTOM,pady=10,expand=True,fill=BOTH)
        
        self.info_h_label = CTkLabel(self.frame_hydrogeninfo,text="Hydrogen Information",text_color="#259269",font=("Pacifico",22,"bold"),fg_color="#dbdbdb")
        self.info_h_label.place(relx=0.5,anchor=CENTER,y=20)
        
        self.Temperature_label = CTkLabel(self.frame_hydrogeninfo,font=('Arial Black',18,'bold'),text_color="#259269",fg_color="#dbdbdb",text=f"Hydrogen Temperature:  0°C")
        self.Temperature_label.place(x=40,y=60)
        
        self.Volume_label = CTkLabel(self.frame_hydrogeninfo,text="Hydrogen Concentrate: 0 ppm",font=('Arial Black',18,'bold'),text_color="#259269",fg_color="#dbdbdb")
        self.Volume_label.place(relx=0.5,anchor=CENTER,y=120)
        
        self.Humidity_label_1 = CTkLabel(self.frame_hydrogeninfo,font=('Arial Black',18,'bold'),text_color="#259269",fg_color="#dbdbdb",text=f"Hydrogen Humidity:  0%")
        self.Humidity_label_1.place(x=1240,y=60)
       
        
        # ====================================== Photos ========================================
        self.temp1 = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\thermometer.png")
        self.sub_temp1 = CTkImage(light_image=self.temp1,size=(50,50),dark_image=self.temp1)
        
        self.wind1 = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\wind.png")
        self.sub_wind1 = CTkImage(light_image=self.wind1,size=(50,50),dark_image=self.wind1)
        
        self.solar_panel = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\solar-panel.png")
        self.sub_soler_panel_2 = CTkImage(light_image=self.solar_panel,size=(50,50),dark_image=self.solar_panel)
        
        # ========================================== days Frames ===============================================
        self.Humidity_label_2 = CTkLabel(self.frame5,text="Electricity production in the coming days",font=("Pacifico",22,"bold"),text_color="#259269",fg_color="#dbdbdb")
        self.Humidity_label_2.place(x=560,y=0)
        
        self.first_Day_frame = CTkFrame(self.frame5,width=250,height=300,corner_radius=30,fg_color="White")
        self.first_Day_frame.place(x=25,y=60)
        
        self.second_Day_frame = CTkFrame(self.frame5,width=250,height=300,corner_radius=30,fg_color="White")
        self.second_Day_frame.place(x=325,y=60)
        
        self.third_Day_frame = CTkFrame(self.frame5,width=250,height=300,corner_radius=30,fg_color="White")
        self.third_Day_frame.place(x=625,y=60)
        
        self.fourth_Day_frame = CTkFrame(self.frame5,width=250,height=300,corner_radius=30,fg_color="White")
        self.fourth_Day_frame.place(x=925,y=60)
        
        self.fifth_Day_frame = CTkFrame(self.frame5,width=250,height=300,corner_radius=30,fg_color="White")
        self.fifth_Day_frame.place(x=1225,y=60)
        
        # ===============================================================================================================
        # -------day 1--------
        
        first_day = current_day + datetime.timedelta(1)
        self.first_day_lbl = CTkLabel(self.first_Day_frame,text=first_day.strftime("%A"),font=('Arial Black',22,'bold'),text_color="Black",fg_color="White")
        self.first_day_lbl.place(relx=0.5,y=30,anchor=CENTER,)
        
        self.temp1_label = CTkLabel(self.first_Day_frame,image=self.sub_temp1,fg_color="white",text="")
        self.temp1_label.place(x=15,y=80)
        self.temp1_lbl = CTkLabel(self.first_Day_frame,text=f"{int(self.day1_temp)}°C",font=('Arial Black',25,'bold'),text_color="#259269",fg_color="White")
        self.temp1_lbl.place(relx=0.6,y=100,anchor=CENTER)
        
        self.wind1_label = CTkLabel(self.first_Day_frame,image=self.sub_wind1,fg_color="white",text="")
        self.wind1_label.place(x=15,y=160)
        self.speed1_lbl = CTkLabel(self.first_Day_frame,text=f"{int(self.day1_speed)} km\h",font=('Arial Black',25,'bold'),text_color="#259269",fg_color="White")
        self.speed1_lbl.place(relx=0.6,y=180,anchor=CENTER)
        
        self.solar_panel_label1 = CTkLabel(self.first_Day_frame,image=self.sub_soler_panel_2,fg_color="white",text="")
        self.solar_panel_label1.place(x=15,y=240)
        self.power2_label = CTkLabel(self.first_Day_frame,text=f"{int(self.power_2)} W\h",font=('Arial Black',25,'bold'),text_color="#ff5400",fg_color="White")
        self.power2_label.place(relx=0.6,y=265,anchor=CENTER)
        
        # # -------day2--------
        second_day = first_day + datetime.timedelta(1)
        self.second_day_lbl = CTkLabel(self.second_Day_frame,text=second_day.strftime("%A"),font=('Arial Black',22,'bold'),text_color="Black",fg_color="White")
        self.second_day_lbl.place(relx=0.5,y=30,anchor=CENTER,)
        
        self.temp2_label = CTkLabel(self.second_Day_frame,image=self.sub_temp1,fg_color="white",text="")
        self.temp2_label.place(x=15,y=80)
        self.temp2_lbl = CTkLabel(self.second_Day_frame,text=f"{int(self.day2_temp)}°C",font=('Arial Black',25,'bold'),text_color="#259269",fg_color="White")
        self.temp2_lbl.place(relx=0.6,y=100,anchor=CENTER)
        
        self.wind2_label = CTkLabel(self.second_Day_frame,image=self.sub_wind1,fg_color="white",text="")
        self.wind2_label.place(x=15,y=160)
        self.speed2_lbl = CTkLabel(self.second_Day_frame,text=f"{int(self.day2_speed)} km\h",font=('Arial Black',25,'bold'),text_color="#259269",fg_color="White")
        self.speed2_lbl.place(relx=0.6,y=180,anchor=CENTER)
        
        self.solar_panel_label2 = CTkLabel(self.second_Day_frame,image=self.sub_soler_panel_2,fg_color="white",text="")
        self.solar_panel_label2.place(x=15,y=240)
        self.power3_label = CTkLabel(self.second_Day_frame,text=f"{int(self.power_3)} W\h",font=('Arial Black',25,'bold'),text_color="#ff5604",fg_color="White")
        self.power3_label.place(relx=0.6,y=265,anchor=CENTER)
        
        
        # # -------day 3--------
        third_day = second_day + datetime.timedelta(1)
        self.third_day_lbl = CTkLabel(self.third_Day_frame,text=third_day.strftime("%A"),font=('Arial Black',22,'bold'),text_color="Black",fg_color="White")
        self.third_day_lbl.place(relx=0.5,y=30,anchor=CENTER)
        
        self.temp3_label = CTkLabel(self.third_Day_frame,image=self.sub_temp1,fg_color="white",text="")
        self.temp3_label.place(x=15,y=80)
        self.temp3_lbl = CTkLabel(self.third_Day_frame,text=f"{int(self.day3_temp)}°C",font=('Arial Black',25,'bold'),text_color="#259269",fg_color="White")
        self.temp3_lbl.place(relx=0.6,y=100,anchor=CENTER)
        
        self.wind3_label = CTkLabel(self.third_Day_frame,image=self.sub_wind1,fg_color="white",text="")
        self.wind3_label.place(x=15,y=160)
        self.speed3_lbl = CTkLabel(self.third_Day_frame,text=f"{int(self.day3_speed)} km\h",font=('Arial Black',25,'bold'),text_color="#259269",fg_color="White")
        self.speed3_lbl.place(relx=0.6,y=180,anchor=CENTER)
        
        self.solar_panel_label3 = CTkLabel(self.third_Day_frame,image=self.sub_soler_panel_2,fg_color="white",text="")
        self.solar_panel_label3.place(x=15,y=240)
        self.power4_label = CTkLabel(self.third_Day_frame,text=f"{int(self.power_4)} W\h",font=('Arial Black',25,'bold'),text_color="#ff5604",fg_color="White")
        self.power4_label.place(relx=0.6,y=265,anchor=CENTER)
        
        # # ------day 4---------
        fourth_day = third_day + datetime.timedelta(1)
        self.fourth_day_lbl = CTkLabel(self.fourth_Day_frame,text=fourth_day.strftime("%A"),font=('Arial Black',22,'bold'),text_color="Black",fg_color="White")
        self.fourth_day_lbl.place(relx=0.5,y=30,anchor=CENTER)
        
        self.temp4_label = CTkLabel(self.fourth_Day_frame,image=self.sub_temp1,fg_color="white",text="")
        self.temp4_label.place(x=15,y=80)
        self.temp4_lbl = CTkLabel(self.fourth_Day_frame,text=f"{int(self.day4_temp)}°C",font=('Arial Black',25,'bold'),text_color="#259269",fg_color="White")
        self.temp4_lbl.place(relx=0.6,y=100,anchor=CENTER)
        
        self.wind4_label = CTkLabel(self.fourth_Day_frame,image=self.sub_wind1,fg_color="white",text="")
        self.wind4_label.place(x=15,y=160)
        self.speed4_lbl = CTkLabel(self.fourth_Day_frame,text=f"{int(self.day4_speed)} km\h",font=('Arial Black',25,'bold'),text_color="#259269",fg_color="White")
        self.speed4_lbl.place(relx=0.6,y=180,anchor=CENTER)
        
        self.solar_panel_label4 = CTkLabel(self.fourth_Day_frame,image=self.sub_soler_panel_2,fg_color="white",text="")
        self.solar_panel_label4.place(x=15,y=240)
        self.power5_label = CTkLabel(self.fourth_Day_frame,text=f"{int(self.power_5)} W\h",font=('Arial Black',25,'bold'),text_color="#ff5604",fg_color="White")
        self.power5_label.place(relx=0.6,y=265,anchor=CENTER)
        
        # # --------day 5-------
        fifth_day = fourth_day + datetime.timedelta(1)
        self.fifth_day_lbl = CTkLabel(self.fifth_Day_frame,text=fifth_day.strftime("%A"),font=('Arial Black',22,'bold'),text_color="Black",fg_color="White")
        self.fifth_day_lbl.place(relx=0.5,y=30,anchor=CENTER)
        
        self.temp5_label = CTkLabel(self.fifth_Day_frame,image=self.sub_temp1,fg_color="white",text="")
        self.temp5_label.place(x=15,y=80)
        self.temp5_lbl = CTkLabel(self.fifth_Day_frame,text=f"{int(self.day5_temp)}°C",font=('Arial Black',25,'bold'),text_color="#259269",fg_color="White")
        self.temp5_lbl.place(relx=0.6,y=100,anchor=CENTER)
        
        self.wind5_label = CTkLabel(self.fifth_Day_frame,image=self.sub_wind1,fg_color="white",text="")
        self.wind5_label.place(x=15,y=160)
        self.speed5_lbl = CTkLabel(self.fifth_Day_frame,text=f"{int(self.day5_speed)} km\h",font=('Arial Black',25,'bold'),text_color="#259269",fg_color="White")
        self.speed5_lbl.place(relx=0.6,y=180,anchor=CENTER)
        
        self.solar_panel_label5 = CTkLabel(self.fifth_Day_frame,image=self.sub_soler_panel_2,fg_color="white",text="")
        self.solar_panel_label5.place(x=15,y=240)
        self.power6_label = CTkLabel(self.fifth_Day_frame,text=f"{int(self.power_6)} W\h",font=('Arial Black',25,'bold'),text_color="#ff5604",fg_color="White")
        self.power6_label.place(relx=0.6,y=265,anchor=CENTER) 
        
        # =============================================== third frame =====================================================
        
        
        self.x_data = []
        self.y_data = []
        self.v_data = []
        self.f_data = []
        #self.check_internet_connection()
        self.time()
        self.history()
        self.change_mode()
        self.temp = []
        self.hydrogen_list = []
        self.humuidity_list = [0]
        self.Time = "11:59:50 PM"
        #self.t1 = continuous_threading.PeriodicThread(2,self.Temperature)
        #self.t1.start()
        
        # self.update_plot()
        self.Add_data()  
        
        
        
    
    def change_mode(self):
        file = open("D:\\My Download\\Files\\Projects\\Green Hydrogen Project\\Green_H2 Version 3\\mode.txt",'r')
        self.mode(file.read())
        file.close()
        

              
    def check_internet_connection(self):
        try:
            response = requests.get('https://www.google.com', timeout=5)
            if response.status_code == 200:
               return True 
            else:
                return False
        except requests.exceptions.RequestException:
            return messagebox.showwarning("WARNING","NO Internet Connection")

      
    def is_port_open(self):
            try:
                ports = ["COM7","COM5"]
                for x in range(0,2):
                    if  serial.Serial(ports[x]).is_open == True:
                        return ports[x]             
            except serial.SerialException:
               return ports[x+1]
           
                           
    def Temperature (self):
        # try:   
                
                #port = self.is_port_open()
                ser = serial.Serial("COM5",9600)
                while True:
                    self.root.update()          
                    line = ser.readline().decode("utf-8")
                    # self.Add_data()
                    sensor_values = re.findall(r"[0-9.]*\S",line)
                    self.temperature_1 = float(sensor_values[0])
                    self.temperature_H = float(sensor_values[1])
                    self.humuidity_1 = float(sensor_values[2])
                    self.humuidity_H = float(sensor_values[3])
                    self.hydrogen = int(sensor_values[4])
                    self.hydrogen2 = int(sensor_values[5])

                    self.x_data.append(len(self.x_data)+1)                  
                    self.y_data.append(self.hydrogen)
                    self.v_data.append(self.temperature_1)
                    self.f_data.append(self.humuidity_H)
                    self.line.set_data(self.x_data, self.y_data)
                    self.line3.set_data(self.x_data, self.v_data)
                    self.line4.set_data(self.x_data, self.f_data)
                    
                    #self.plot.set_ylim(0,self.y_data)
                    #self.plot.set_xlim(0,86400)
                    self.plot.set
                    self.plot.relim()
                    self.plot.autoscale_view()
                    self.fig.canvas.draw_idle()
                    #self.root.after(1000, self.update_plot)  
                    
                    self.temp_lbl = CTkLabel(self.root ,font=('Arial Black',28,'bold'),text_color="#259269",fg_color=("#dbdbdb","#2b2b2b"))
                    self.temp_lbl.place(x=470,y=260)
                    self.temp_lbl.configure(text=f"{self.temperature_1}°C")
                   
                    self.humudity_lbl = CTkLabel(self.root,font=('Arial Black',28,'bold'),text_color="#259269",fg_color=("#dbdbdb","#2b2b2b"))
                    self.humudity_lbl.place(x=1220,y=260)
                    self.humudity_lbl.configure(text=f"{self.humuidity_1}%")
                    
                    self.Temperature_label = CTkLabel(self.frame_hydrogeninfo,font=('Arial Black',18,'bold'),text_color="#259269",fg_color=("#dbdbdb","#2b2b2b"))
                    self.Temperature_label.place(x=40,y=60)
                    
                    self.Volume_label = CTkLabel(self.frame_hydrogeninfo,font=('Arial Black',18,'bold'),text_color="#259269",fg_color=("#dbdbdb","#2b2b2b"))
                    self.Volume_label.place(relx=0.5,anchor=CENTER,y=120)
                    
                    self.Humidity_label_1 = CTkLabel(self.frame_hydrogeninfo,font=('Arial Black',18,'bold'),text_color="#259269",fg_color=("#dbdbdb","#2b2b2b"))
                    self.Humidity_label_1.place(x=1240,y=60)
                    
                    self.Temperature_label.configure(text=f"Hydrogen Temperature:  {self.temperature_H}°C")
                    self.Humidity_label_1.configure(text=f"Hydrogen Humidity:  {self.humuidity_H}%")
                    self.Volume_label.configure(text=f"Hydrogen Concentrate: {self.hydrogen} ppm")
                    
                    
                    # if 1000 < self.hydrogen2:
                    #     file = open("D:\\Python\\Green_H2 Version 3\\numbersandemails.txt", "r+") 
                    #     row = file.readlines()
                    #     start = row.index("\n")
                    #     end = row.index("**********************\n")
                        # text="""Warning!
                        # Currently, a hydrogen gas leak has been detected in the hydrogen production station. 
                        # Please go to the station and check and solve the problem as soon as possible."""
                    #     numbers = row[start+1:end]
                        
                    #     for number in numbers:
                    #         kit.sendwhatmsg_instantly(phone_no=f"+2{number.strip()}",message=text,wait_time=30,close_time=5)
                    #     pygame.init()
                    #     pygame.mixer.music.load("C:\\Users\\Computec\\Downloads\\PNG Icons\\Danger Alarm.mp3")
                    #     pygame.mixer.music.play(loops=0)
                    #     time.sleep(10)
                    #     pygame.mixer.stop()
                        
                        
                    
        
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
                    
                    test = pd.DataFrame({"month":[str_month],
                                         "precipitation":[0],
                                         "temp_max":[self.max_temp],
                                         "temp_min":[self.Min_temp],
                                         "wind":[self.current_speed]})
                    self.prediction = classifier.predict(test)[0]  
                    
                    
                    if self.prediction == "rain" or self.prediction == "snow" or self.prediction == "drizzle":  
                            self.root.update()   
                            self.sun = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\cloudy-day.png")
                            self.sub_sun = self.sun.subsample(2,2)
                            sun_label = Label(self.root,image=self.sub_sun,bg="white")
                            sun_label.place(x=73,y=190)
                                        
                    elif self.prediction == "sun":
                                self.root.update() 
                                self.sun = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\sun.png")
                                self.sub_sun = CTkImage(light_image=self.sun,size=(230,230),dark_image=self.sun)
                                self.sun_label = CTkLabel(self.root,image=self.sub_sun,fg_color=("#dbdbdb","#2b2b2b"),text="",bg_color="#dbdbdb")
                                self.sun_label.place(x=73,y=190)    
                                
                    else:  
                            self.root.update() 
                            self.sun = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\sun.png")
                            self.sub_sun = self.sun.subsample(2,2)
                            sun_label = Label(self.root,image=self.sub_sun,bg="white")
                            sun_label.place(x=73,y=190)
               
        # except:
        #     if self.check_internet_connection == FALSE:
        #        messagebox.showerror("Error","Internet Connection is Lost, Please Try Again and Check the Connection")  
                
        #     else:
        #         messagebox.showerror("Error","Connection is Lost, Please Try Again and Refresh The Window")
        #     self.t1.stop()
            
    def update_plot(self):
            import random
            self.x_data.append(len(self.x_data)+1)                  
            self.y_data.append(444+random.randint(0,10))
            self.v_data.append(39+random.randint(0,3))
            self.f_data.append(20+random.randint(0,2))
            self.line.set_data(self.x_data, self.y_data)
            self.line3.set_data(self.x_data, self.v_data)
            self.line4.set_data(self.x_data, self.f_data)
            #self.plot.set_ylim(0,2000)
            #self.plot.set_xlim(0,86400)
            self.plot.set
            self.plot.relim()
            self.plot.autoscale_view()
            self.fig.canvas.draw_idle()
            self.root.after(2000, self.update_plot)  
            
                  
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
        self.date_lbl.place(x=20,y=10)
        self.date_lbl.configure(text= self.date)
        self.date_lbl.after(1000,self.time)
    
    def history(self):
        self.hist =  strftime("%d-%m-%Y")
        self.hist_lbl.place(x=1390,y=10)
        self.hist_lbl.configure(text=self.hist)
        self.hist_lbl.after(1000,self.history)
    
    def setting(self):
        from fourth_interface import Setting
        self.root.destroy()
        self.third_window = Setting(self.main_window)
        
    def home(self):
        self.root.destroy()
        self.main_window.root.deiconify()
        
    
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
            
            
    def mode(self,mode):
        if mode == "Dark":
            set_appearance_mode("dark") 
            self.root.config(bg="#dbdbdb")
            self.Frame.configure(bg_color="#dbdbdb")
            self.Frame2.configure(fg_color="White",bg_color="#dbdbdb")
            self.GreenH.configure(text_color="black",fg_color="#ffffff")
            self.image_label.configure(fg_color="#ffffff")
            self.Home_button.configure(fg_color="#dbdbdb",text_color="black",bg_color="#dbdbdb",hover_color="white")
            self.Weather_button.configure(fg_color="#dbdbdb",text_color="#27ae60",bg_color="#dbdbdb",hover_color="white")
            self.database_button.configure(fg_color="#dbdbdb",text_color="Black",bg_color="#dbdbdb",hover_color="white")
            self.refresh_button.configure(fg_color="#dbdbdb",text_color="Black",bg_color="#dbdbdb",hover_color="white")
            self.Setting_button.configure(fg_color="#dbdbdb",text_color="Black",bg_color="#dbdbdb",hover_color="white")
            self.Exit_button.configure(fg_color="#dbdbdb",text_color="Black",bg_color="#dbdbdb",hover_color="white")
            self.date_lbl.configure(text_color='Black',fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.hist_lbl.configure(text_color='Black',fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.shape.configure(bg_color="#2b2b2b",fg_color="White")
            self.city.configure(bg_color="white")
            self.today.configure(bg_color="white")
            self.sun_label.configure(fg_color="#2b2b2b",bg_color="#2b2b2b")
            self.temp_label.configure(fg_color="#2b2b2b",bg_color="#2b2b2b")
            self.wind_label.configure(fg_color="#2b2b2b",bg_color="#2b2b2b")
            self.humudity_label.configure(fg_color="#2b2b2b",bg_color="#2b2b2b")
            self.sunrise_label.configure(fg_color="#2b2b2b",bg_color="#2b2b2b")
            self.solar_panel_label_1.configure(fg_color="#2b2b2b",bg_color="#2b2b2b")
            self.sunset_label.configure(fg_color="#2b2b2b",bg_color="#2b2b2b")
            self.temp_lbl.configure(fg_color="#2b2b2b",bg_color="#2b2b2b")
            self.speed_lbl.configure(fg_color="#2b2b2b",bg_color="#2b2b2b")
            self.humudity_lbl.configure(fg_color="#2b2b2b",bg_color="#2b2b2b")
            self.sunrise_lbl.configure(fg_color="#2b2b2b",bg_color="#2b2b2b")
            self.elec_label.configure(fg_color="#2b2b2b",bg_color="#2b2b2b")
            self.sunset_lbl.configure(fg_color="#2b2b2b",bg_color="#2b2b2b")
            self.Frame3.configure(fg_color="#2b2b2b")
            self.fig.patch.set_facecolor("#2b2b2b") 
            self.plot.set_title("Graphical Representation of the Hydrogen Production Process",color="white")
            self.plot.set_xlabel("Second ",color="white")
            #self.plot.set_ylabel("Hydrogen production (ppm) , Temperature (°C)",color="white")
            self.plot.tick_params(axis="both",colors="white")
            self.plot.legend()
            self.canvas.draw_idle()
            self.datavisulization_label.configure(fg_color="#2b2b2b")
            self.line1.configure(fg_color="white")
            self.line2.configure(fg_color="white")
            self.info_h_label.configure(fg_color="#2b2b2b")
            self.Temperature_label.configure(fg_color="#2b2b2b")
            self.Volume_label.configure(fg_color="#2b2b2b")
            self.Humidity_label_1.configure(fg_color="#2b2b2b")
            self.frame5.configure(fg_color="#2b2b2b")
            self.Humidity_label_2.configure(fg_color="#2b2b2b")
            self.first_Day_frame.configure(fg_color="#696969")
            self.second_Day_frame.configure(fg_color="#696969")
            self.third_Day_frame.configure(fg_color="#696969")
            self.fourth_Day_frame.configure(fg_color="#696969")
            self.fifth_Day_frame.configure(fg_color="#696969")
            self.first_day_lbl.configure(text_color="white",fg_color="#696969")
            self.second_day_lbl.configure(text_color="white",fg_color="#696969")
            self.third_day_lbl.configure(text_color="white",fg_color="#696969")
            self.fourth_day_lbl.configure(text_color="white",fg_color="#696969")
            self.fifth_day_lbl.configure(text_color="white",fg_color="#696969")
            self.temp1_label.configure(fg_color="#696969")
            self.temp2_label.configure(fg_color="#696969")
            self.temp3_label.configure(fg_color="#696969")
            self.temp4_label.configure(fg_color="#696969")
            self.temp5_label.configure(fg_color="#696969")
            self.temp1_lbl.configure(fg_color="#696969")
            self.temp2_lbl.configure(fg_color="#696969")
            self.temp3_lbl.configure(fg_color="#696969")
            self.temp4_lbl.configure(fg_color="#696969")
            self.temp5_lbl.configure(fg_color="#696969")
            self.wind1_label.configure(fg_color="#696969")
            self.wind2_label.configure(fg_color="#696969")
            self.wind3_label.configure(fg_color="#696969")
            self.wind4_label.configure(fg_color="#696969")
            self.wind5_label.configure(fg_color="#696969")
            self.speed1_lbl.configure(fg_color="#696969")
            self.speed2_lbl.configure(fg_color="#696969")
            self.speed3_lbl.configure(fg_color="#696969")
            self.speed4_lbl.configure(fg_color="#696969")
            self.speed5_lbl.configure(fg_color="#696969")
            self.solar_panel_label1.configure(fg_color="#696969")
            self.solar_panel_label2.configure(fg_color="#696969")
            self.solar_panel_label3.configure(fg_color="#696969")
            self.solar_panel_label4.configure(fg_color="#696969")
            self.solar_panel_label5.configure(fg_color="#696969")
            self.power2_label.configure(fg_color="#696969")
            self.power3_label.configure(fg_color="#696969")
            self.power4_label.configure(fg_color="#696969")
            self.power5_label.configure(fg_color="#696969")
            self.power6_label.configure(fg_color="#696969")    
        else:
            set_appearance_mode("light") 
            self.root.config(bg="#0d0d0d")
            self.Frame.configure(bg_color="#0d0d0d")
            self.Frame2.configure(fg_color="#1d1d1d",bg_color="#0d0d0d")
            self.GreenH.configure(text_color="white",fg_color="#1d1d1d")
            self.image_label.configure(fg_color="#1d1d1d")
            self.Home_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.Weather_button.configure(fg_color="#0d0d0d",text_color="#27ae60",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.database_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.refresh_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.Setting_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.Exit_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.date_lbl.configure(text_color='white',fg_color="#0D0D0D",bg_color="#0D0D0D")
            self.hist_lbl.configure(text_color='white',fg_color="#0D0D0D",bg_color="#0D0D0D")  
            self.shape.configure(bg_color="#dbdbdb",fg_color="black")
            self.city.configure(bg_color="#0D0D0D")
            self.today.configure(bg_color="#0D0D0D")
            self.sun_label.configure(fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.temp_label.configure(fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.wind_label.configure(fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.humudity_label.configure(fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.sunrise_label.configure(fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.solar_panel_label_1.configure(fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.sunset_label.configure(fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.temp_lbl.configure(fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.speed_lbl.configure(fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.humudity_lbl.configure(fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.sunrise_lbl.configure(fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.elec_label.configure(fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.sunset_lbl.configure(fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.Frame3.configure(fg_color="#dbdbdb")
            self.fig.patch.set_facecolor("#dbdbdb") 
            self.plot.set_title("Graphical Representation of the Hydrogen Production Process",color="Black")
            self.plot.set_xlabel("Second",color="Black")
            #self.plot.set_ylabel("Hydrogen production (ppm) , Temperature (°C)",color="Black")
            self.plot.tick_params(axis="both",colors="black")   # x ,y values axis
            self.plot.legend()
            self.canvas.draw_idle()
            self.datavisulization_label.configure(fg_color="#dbdbdb")
            self.line1.configure(fg_color="black")
            self.line2.configure(fg_color="black")
            self.info_h_label.configure(fg_color="#dbdbdb")
            self.Temperature_label.configure(fg_color="#dbdbdb")
            self.Volume_label.configure(fg_color="#dbdbdb")
            self.Humidity_label_1.configure(fg_color="#dbdbdb")
            self.frame5.configure(fg_color="#dbdbdb")
            self.Humidity_label_2.configure(fg_color="#dbdbdb")
            self.first_Day_frame.configure(fg_color="White")
            self.second_Day_frame.configure(fg_color="White")
            self.third_Day_frame.configure(fg_color="White")
            self.fourth_Day_frame.configure(fg_color="White")
            self.fifth_Day_frame.configure(fg_color="White")
            self.first_day_lbl.configure(text_color="Black",fg_color="White")
            self.second_day_lbl.configure(text_color="Black",fg_color="White")
            self.third_day_lbl.configure(text_color="Black",fg_color="White")
            self.fourth_day_lbl.configure(text_color="Black",fg_color="White")
            self.fifth_day_lbl.configure(text_color="Black",fg_color="White")
            self.temp1_label.configure(fg_color="White")
            self.temp2_label.configure(fg_color="White")
            self.temp3_label.configure(fg_color="White")
            self.temp4_label.configure(fg_color="White")
            self.temp5_label.configure(fg_color="White")
            self.temp1_lbl.configure(fg_color="White")
            self.temp2_lbl.configure(fg_color="White")
            self.temp3_lbl.configure(fg_color="White")
            self.temp4_lbl.configure(fg_color="White")
            self.temp5_lbl.configure(fg_color="White")
            self.wind1_label.configure(fg_color="White")
            self.wind2_label.configure(fg_color="White")
            self.wind3_label.configure(fg_color="White")
            self.wind4_label.configure(fg_color="White")
            self.wind5_label.configure(fg_color="White")
            self.speed1_lbl.configure(fg_color="White")
            self.speed2_lbl.configure(fg_color="White")
            self.speed3_lbl.configure(fg_color="White")
            self.speed4_lbl.configure(fg_color="White")
            self.speed5_lbl.configure(fg_color="White")
            self.solar_panel_label1.configure(fg_color="White")
            self.solar_panel_label2.configure(fg_color="White")
            self.solar_panel_label3.configure(fg_color="White")
            self.solar_panel_label4.configure(fg_color="White")
            self.solar_panel_label5.configure(fg_color="White")
            self.power2_label.configure(fg_color="White")
            self.power3_label.configure(fg_color="White")
            self.power4_label.configure(fg_color="White")
            self.power5_label.configure(fg_color="White")
            self.power6_label.configure(fg_color="White")
            
