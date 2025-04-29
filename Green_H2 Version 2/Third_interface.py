from tkinter import * 
from tkinter import messagebox
from customtkinter import *
from tkinter import ttk 
from time import strftime
import pymysql
import pandas as pd 
import time 

from data import Data
import datetime
import sys


class Database:
    def __init__(self,main_window):
        self.main_window = main_window
        self.root = Toplevel()
        
        self.root.state("zoomed")
        self.root.resizable(True,True)
        self.root.config(bg="#0d0d0d")
        self.root.title("Green Hydrogen")
        self.root.minsize(1550,800)
        self.root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\3-removebg-preview_1.ico")
    
        # ============================================== Frames ==================================================
        self.Frame = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Rectangle 1.png")
        frame_label = Label(self.root,image=self.Frame,bg="#0d0d0d")
        frame_label.place(x=0,y=150)
        
        self.Frame2 = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Rectangle 1 (1).png")
        frame_label = Label(self.root,image=self.Frame2,bg="#0d0d0d")
        frame_label.place(x=600,y=0)
        
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
        
        self.weather = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\monitoring.png")
        self.sub_weather = self.weather.subsample(3,3)
        self.Weather_button = Button(self.root,text="  Monitor",image=self.sub_weather,bd=0,bg="#0d0d0d",fg="white",justify="center",activebackground="#0d0d0d",compound="left",font=("Arial Black",12,"bold"),activeforeground="white",cursor="hand2",command=self.Monitor)
        self.Weather_button.place(x=450,y=90,width=140,height=50)
        
        self.database = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\database (1).png")
        self.sub_database = self.database.subsample(3,3)
        self.database_button = Button(self.root,text="  Database",image=self.sub_database,bd=0,bg="#0d0d0d",fg="#27AE60",justify="center",activebackground="#0d0d0d",compound="left",font=("Arial Black",12,"bold"),activeforeground="#27AE60",cursor="hand2")
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
        
        self.button_bg = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Rectangle 1 (3).png")
        btn_bg_label = Label(self.root,image=self.button_bg,bg="white")
        btn_bg_label.place(x=650,y=170)
        
        Export_button = Button(self.root,text="Export",bd=0,font=("Arial Black",18,"bold"),bg="#0D0D0D",fg="#27AE60",activebackground="#0D0D0D",activeforeground="#27AE60",cursor="hand2",command=self.export)
        Export_button.place(x=715,y=175)
        
        # ===================================================================================================================================
        
        database_frame = Frame(self.root,bg="white")
        database_frame.place(x=25,y=250,width=1490,height=570)
        
        scrollbar_y = Scrollbar(database_frame,orient="vertical")
        # --------------------- treeview ---------------------
        
        self.hydrogen_database= ttk.Treeview(database_frame,columns=("max_temp","min_temp","precipitation","wind","weather","solar_panel","hydrogen"), xscrollcommand= scrollbar_y.set) 
        self.hydrogen_database.place(x=0 , y=0,width=1490,height=570)
        scrollbar_y.pack(fill=Y,side=LEFT)
        scrollbar_y.config(command=self.hydrogen_database.yview)

        self.hydrogen_database['show'] = 'headings'
        self.hydrogen_database.heading('max_temp', text ='max_temp')
        self.hydrogen_database.heading('min_temp',text='min_temp')
        self.hydrogen_database.heading('precipitation',text='precipitation')
        self.hydrogen_database.heading('wind',text='wind')
        self.hydrogen_database.heading('weather',text='weather')
        self.hydrogen_database.heading('solar_panel',text='solar_panel')
        self.hydrogen_database.heading('hydrogen',text='hydrogen')
    
        self.hydrogen_database.column('max_temp',width=10)
        self.hydrogen_database.column('min_temp',width=10)
        self.hydrogen_database.column('precipitation',width=10)
        self.hydrogen_database.column('wind',width=10)
        self.hydrogen_database.column('weather',width=10)
        self.hydrogen_database.column('solar_panel',width=10)
        self.hydrogen_database.column('hydrogen',width=10)
        self.Time = "11:59:59 PM"
        self.Show_data()
        self.time()
        self.history()
        
        
    
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
        
    def Show_data(self):
        con = pymysql.connect( host="localhost", user="root", password="123456", database="Green_hydrogen")
        cur = con.cursor()  
        cur.execute("Select * from Production")
        rows = cur.fetchall()
        if len(rows)!= 0 : 
            self.hydrogen_database.delete(*self.hydrogen_database.get_children())
            for row in rows:
                self.hydrogen_database.insert("",END,values=row)
        con.commit()
        con.close()
    
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

            
    
    def export(self):
        conn = pymysql.connect( host="localhost", user="root", password="123456", database="Green_hydrogen")
        cursor = conn.cursor()
        query = "SELECT * FROM Production"
        cursor.execute(query)
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(data, columns=columns)
        df.to_csv("C:\\Users\\Computec\\Desktop\\Hydrogen_production.csv", index=False)
        conn.close()
        messagebox.showinfo("Export","Successfully converted to Excel file")
    
    def home(self):
        self.root.destroy()
        self.main_window.root.deiconify()
        sys.exit()
    
    def Refresh(self):
        self.root.withdraw()
        self.second_window = Database(self.main_window)
    
    def Monitor(self):
        from Second_interface import Weather
        self.root.withdraw()  
        self.third_window = Weather(self.main_window)
        sys.exit()
        
        
    def Exit_func(self):
            self.ques =  messagebox.askyesno("EXIT","Do You Really Want to Exit?")
            if self.ques == 1:
                self.root.destroy()
                sys.exit()
            else: 
                return