from tkinter import Toplevel
from tkinter import messagebox
from tkinter import ttk 
from customtkinter import *
from time import strftime
import pymysql
import pandas as pd 
import time 
from data import Data
import datetime
import sys
import PIL.Image
from CTkTable import *
import pywhatkit as kit
from threading import Thread
from statistics import mean

class Database:
    def __init__(self,main_window):
        self.main_window = main_window
        self.root = CTkToplevel()
        self.root.state("zoomed")
        self.root.resizable(True,True)
        self.root.config(bg="#0d0d0d")
        self.root.title("Green Hydrogen")
        self.root.minsize(1550,800)
        self.root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\3-removebg-preview_1.ico")
    
        # ============================================== Frames ==================================================
        self.Frame = CTkFrame(self.root,width=1550,height=1000,corner_radius=180,bg_color="#0d0d0d")
        self.Frame.place(x=-7,y=150)
        
        self.Frame2 = CTkFrame(self.root,width=300,height=70,corner_radius=90,bg_color="#0d0d0d",fg_color="#1d1d1d")
        self.Frame2.place(x=600,y=0)
        
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
        self.Home_button = CTkButton(self.root,text="  Home",image=self.sub_home,bg_color="#0d0d0d",hover_color="#2b2b2b",fg_color="#0d0d0d",text_color="#27AE60",compound="left",font=("Arial Black",15,"bold"),width=110,height=50,corner_radius=90,command=self.home)
        self.Home_button.place(x=300,y=90)
        
        self.weather = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\dashboard_white.png")
        self.weather2 = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\dashboard_black.png")
        self.sub_weather = CTkImage(light_image=self.weather,size=(35,35),dark_image=self.weather2)
        self.Weather_button = CTkButton(self.root,text="  Monitor",image=self.sub_weather,bg_color="#0d0d0d",hover_color="#2b2b2b",fg_color="#0d0d0d",text_color="white",compound="left",font=("Arial Black",15,"bold"),width=110,height=50,corner_radius=90,command=self.Monitor)
        self.Weather_button.place(x=450,y=90)
        
        self.database = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\database (1).png")
        self.database2 = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\database (1).png")
        self.sub_database = CTkImage(light_image=self.database,size=(25,25),dark_image=self.database2)
        self.database_button = CTkButton(self.root,text="  Database",image=self.sub_database,bg_color="#0d0d0d",hover_color="#2b2b2b",fg_color="#0d0d0d",text_color="white",compound="left",font=("Arial Black",15,"bold"),width=110,height=50,corner_radius=90)
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
        
         
        
        self.Export_button = CTkSegmentedButton(self.root,values=("XLSX","CSV","XLS"),fg_color="#dbdbdb",background_corner_colors=("#2b2b2b","#2b2b2b","#2b2b2b","#2b2b2b"),command=self.export,unselected_color="#dbdbdb",text_color="Black",corner_radius=30,selected_color="#27ae60",selected_hover_color="#696969")
        self.Export_button.place(x=750,y=190)
        
        self.export_label = CTkLabel(self.root,text="Export To:",fg_color="#2b2b2b",text_color="#dbdbdb",font=("Pacifico",22,"bold"))
        self.export_label.place(x=550,y=180)
        
        self.line1 = CTkFrame(self.root,width=1300,height=5,fg_color="white",corner_radius=90,background_corner_colors=("white","white","white","white"))
        self.line1.place(relx=0.5,anchor=CENTER,y=270)
        
        # ===================================================================================================================================
        
        self.database_frame = CTkScrollableFrame(self.root,fg_color="Black",width=1450,height=770)
        self.database_frame.place(x=25,y=300)
        
        self.Time = "11:59:59 PM"
        self.time()
        self.history()
        self.show_data()
        self.change_mode()
        Thread(target=self.report_on())
        
    def report(self):
        while True:
            self.root.update()
            day = str(datetime.datetime.now().day)
            month = datetime.datetime.now().strftime("%B")
            hour = str(datetime.datetime.now().hour)
            minuit =str(datetime.datetime.now().minute)
            h_production = self.table.get_column(6)[1:-1]
            soler_production = self.table.get_column(5)[1:-1]
            avg_temperature = self.table.get_column(0)[1:-1]
            if  day == "30" and hour == "23" and minuit == "50" :           
                file = open("D:\\Python\\Green_H2 Version 3\\numbersandemails.txt", "r+") 
                row = file.readlines()
                start = row.index("\n",2)
                e_mails = row[start+1:]
                text =  f"""In the current month, quantities of hydrogen production were recorded in the last 30 days. Green hydrogen was produced in quantity amounting to {str(sum(h_production))} ppm, and the average production of electricity from solar panels was recorded, estimated at {str(mean(soler_production))} W\h."""
                for e_mail in e_mails:
                    kit.send_hmail("awadallayossef@gmail.com","pjin qhau qvhx usqt",F"Monthly Report on Hydrogen Production for {month}",text,e_mail.strip())
                break
            else:   
                    continue
                    #time.sleep(30)
    def report_on(self):
        day = str(datetime.datetime.now().day)
        if day =="30":
            self.report()
        else:
            return
        
    def show_data(self):
        conn = pymysql.connect( host="localhost", user="root", password="123456", database="Green_hydrogen")
        cursor = conn.cursor()
        query = "SELECT * FROM Production"
        cursor.execute(query)
        data = cursor.fetchall()
        new_data = list(data)
        columns = [('Max Temperature (°C)', 'Min Temperature (°C)', 'Precipitation (%)', 'Wind (Km\h)', 'Weather', 'Solar Panel (W\h)', 'Hydrogen Production (PPM)')]
        self.values =  columns + new_data
        self.table = CTkTable(self.database_frame , values=self.values , header_color="#27ae60" , hover_color="#106a43" , color_phase="vertical" , font=("Ariel black",15,"bold"))
        self.table.pack(expand=True, fill="both", padx=20, pady=10)
        
        
        
    def export(self,value):
        conn = pymysql.connect( host="localhost", user="root", password="123456", database="Green_hydrogen")
        cursor = conn.cursor()
        query = "SELECT * FROM Production"
        cursor.execute(query)
        data = cursor.fetchall()
        print(data)
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(data, columns=columns)
        if value == "CSV":
            df.to_csv("C:\\Users\\Computec\\Desktop\\Hydrogen_production.csv", index=False)
            messagebox.showinfo("Export","Successfully converted to CSV file")
        elif value == "XLSX":
            df.to_csv("C:\\Users\\Computec\\Desktop\\Hydrogen_production.xlsx", index=False)
            messagebox.showinfo("Export","Successfully converted to XLSX file")
        else:
            df.to_csv("C:\\Users\\Computec\\Desktop\\Hydrogen_production.xls", index=False)
            messagebox.showinfo("Export","Successfully converted to XLS file")   
        conn.close()
            
        
    def change_mode(self):
        file = open("D:\\My Download\\Files\\Projects\\Green Hydrogen Project\\Green_H2 Version 3\\mode.txt",'r')
        self.mode(file.read())
        file.close()
        
    def mode(self,mode):
        if mode == "Dark"  :                                     
            set_appearance_mode("dark") 
            self.root.config(bg="#dbdbdb")
            self.Frame.configure(bg_color="#dbdbdb")
            self.Frame2.configure(fg_color="White",bg_color="#dbdbdb")
            self.GreenH.configure(text_color="black",fg_color="#ffffff")
            self.image_label.configure(fg_color="#ffffff")
            self.Home_button.configure(fg_color="#dbdbdb",text_color="black",bg_color="#dbdbdb",hover_color="white")
            self.Weather_button.configure(fg_color="#dbdbdb",text_color="Black",bg_color="#dbdbdb",hover_color="white")
            self.database_button.configure(fg_color="#dbdbdb",text_color="#27ae60",bg_color="#dbdbdb",hover_color="white")
            self.refresh_button.configure(fg_color="#dbdbdb",text_color="Black",bg_color="#dbdbdb",hover_color="white")
            self.Setting_button.configure(fg_color="#dbdbdb",text_color="Black",bg_color="#dbdbdb",hover_color="white")
            self.Exit_button.configure(fg_color="#dbdbdb",text_color="Black",bg_color="#dbdbdb",hover_color="white")
            self.date_lbl.configure(text_color='Black',fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.hist_lbl.configure(text_color='Black',fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.database_frame.configure(fg_color="#dbdbdb")
            self.Export_button.configure(fg_color="#dbdbdb",background_corner_colors=("#2b2b2b","#2b2b2b","#2b2b2b","#2b2b2b"),unselected_color="#dbdbdb",text_color="Black",unselected_hover_color="#696969")
            self.export_label.configure(fg_color="#2b2b2b",text_color="#dbdbdb")
            self.line1.configure(fg_color="white")
        else:
            set_appearance_mode("light") 
            self.root.config(bg="#0d0d0d")
            self.Frame.configure(bg_color="#0d0d0d")
            self.Frame2.configure(fg_color="#1d1d1d",bg_color="#0d0d0d")
            self.GreenH.configure(text_color="white",fg_color="#1d1d1d")
            self.image_label.configure(fg_color="#1d1d1d")
            self.Home_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.Weather_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.database_button.configure(fg_color="#0d0d0d",text_color="#27ae60",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.refresh_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.Setting_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.Exit_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.date_lbl.configure(text_color='white',fg_color="#0D0D0D",bg_color="#0D0D0D")
            self.hist_lbl.configure(text_color='white',fg_color="#0D0D0D",bg_color="#0D0D0D")
            self.database_frame.configure(fg_color="black")
            self.Export_button.configure(fg_color="#2b2b2b",background_corner_colors=("#dbdbdb","#dbdbdb","#dbdbdb","#dbdbdb"),unselected_color="#2b2b2b",text_color="#dbdbdb",unselected_hover_color="#AFAFAF")
            self.export_label.configure(text_color="#2b2b2b",fg_color="#dbdbdb")
            self.line1.configure(fg_color="black")

    def time(self):
        self.date = strftime('%I:%M:%S %p')
        self.date_lbl.place(x=20,y=10)
        self.date_lbl.configure(text= self.date)
        self.date_lbl.after(1000,self.time)
    
    def history(self):
        self.hist =  strftime("%d-%m-%Y")
        self.hist_lbl.place(x=1350,y=10)
        self.hist_lbl.configure(text=self.hist)
        self.hist_lbl.after(1000,self.history)
        
    
    def Add_data (self):
        from Second_interface import Weather 
        while True:
            self.root.update()
            Time_now = strftime('%I:%M:%S %p')
            if self.Time == Time_now: 
                con = pymysql.connect( host="localhost", user="root", password="123456", database="Green_hydrogen")
                cur = con.cursor()   
                cur.execute("insert into Production values (%s,%s,%s,%s,%s,%s,%s)",(Weather(self.root).max_temp,
                                                                                    Weather(self.root).Min_temp,
                                                                                    int(Weather(self.root).Avg_humuidity),
                                                                                    Data().current_speed,
                                                                                    Weather(self.root).prediction,
                                                                                    Data().power_1,
                                                                                    Weather(self.root).hydrogen_production))
                con.commit()
                con.close()   
                messagebox.showinfo("Information","Production Data, Has Now Been Added to the Database")
            else:
                continue 
            time.sleep(1)

            
    
    def setting(self):
        from fourth_interface import Setting
        self.root.destroy()
        self.third_window = Setting(self.main_window)
    
    def home(self):
        self.root.destroy()
        self.main_window.root.deiconify()
    
    def Refresh(self):
        self.root.withdraw()
        self.second_window = Database(self.main_window)
    
    def Monitor(self):
        from Second_interface import Weather
        self.root.destroy()
        self.third_window = Weather(self.main_window)
        
        
        
    def Exit_func(self):
            self.ques =  messagebox.askyesno("EXIT","Do You Really Want to Exit?")
            if self.ques == 1:
                self.root.destroy()
                sys.exit()
            else: 
                return
            
# root = CTk()
# ob = Database(root)
# root.mainloop()