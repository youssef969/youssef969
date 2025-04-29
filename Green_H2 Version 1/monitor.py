from tkinter import * 
from tkinter import messagebox 
from time import strftime
import serial
import continuous_threading
import time 

class Monitor:
    def __init__(self,main_window):
        self.main_window = main_window

        self.root = Toplevel()
        self.root.geometry("950x550+350+150")  
        self.root.resizable(False,False)
        self.root.config(bg="white")
        self.root.title("Data Monitoring")
        self.root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\1710162623466-removebg-preview.ico")
       
        
        # ================================================= first_interface ========================================
        self.fr1 = Frame(self.root,bg="#27AE60")
        self.fr1.place(x=50,y=0,width=900,height=80)
       
        fr2 = Frame(self.root,bg="#7DCEA0")
        fr2.place(x=0,y=0,width=50,height=550)
        
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
        
        self.weather = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\rainy-day.png")
        self.sub_weather = self.weather.subsample(5,5)
        weather_button_1 =  Button(fr2,image=self.sub_weather,bd=0,bg="#7DCEA0",justify="center",activebackground="#7DCEA0",command=self.Weather)
        weather_button_1.place(x=10,y=80,width=30,height=60)
        
        self.monitor = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Monitor (1).png")
        self.sub_monitor = self.monitor.subsample(5,5)
        Monitor_button =  Button(fr2,image=self.sub_monitor,bd=0,bg="#7DCEA0",justify="center",activebackground="#7DCEA0")
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
        # ===================================================================================================================================
        
        Temperature_label = Label(self.root,text=f"Hydrogen Temperature:",font=('Stincil',25,'bold'),foreground="#259269",bg="white")
        Temperature_label.place(x=80,y=100)
        
        Humidity_label = Label(self.root,text="Hydrogen Humidity:",font=('Stincil',25,'bold'),foreground="#259269",bg="white")
        Humidity_label.place(x=90,y=250)
        
        Volume_label = Label(self.root,text="Hydrogen Concentrate:",font=('Stincil',25,'bold'),foreground="#259269",bg="white")
        Volume_label.place(x=80,y=400)
        
        self.time()
        self.history()
        
        self.t1 = continuous_threading.PeriodicThread(1,self.Temperature)
        self.t1.start()
        
        
            
    def time(self):
        self.date = strftime('%I:%M:%S %p')
        self.date_lbl = Label(self.fr1,font =('calibri',20,'bold'),foreground='white',bg="#27AE60")
        self.date_lbl.place(x=20,y=2)
        self.date_lbl.config(text= self.date)
        self.date_lbl.after(1000,self.time)
            
    def history(self):
        self.hist =  strftime("%d/%m/%Y")
        self.hist_lbl = Label(self.fr1,font=('calibri',20,'bold'),foreground="white",bg="#27AE60")
        self.hist_lbl.place(x=20,y=40)
        self.hist_lbl.config(text=self.hist)
        self.hist_lbl.after(1000,self.history)
        
    def Temperature(self):    
        self.ser = serial.Serial('COM5',9600)
        self.line = self.ser.readline().decode("utf-8")
        self.temperature_2 = self.line[41:46]
        self.Temperature_label = Label(self.root,font=('Stincil',25,'bold'),foreground="#259269",bg="white")
        self.Temperature_label.place(x=80,y=100)
        self.Temperature_label.config(text=f"Hydrogen Temperature:  {self.temperature_2}°C")
        self.humuidity_2 = self.line[15:20]
        self.Humidity_label = Label(self.root,font=('Stincil',25,'bold'),foreground="#259269",bg="white")
        self.Humidity_label.place(x=90,y=250)
        self.Humidity_label.config(text=f"Hydrogen Humidity:  {self.humuidity_2}%")
            
    def home(self):
        self.root.destroy()
        self.main_window.root.deiconify()
                
    def Weather (self):
        
        from Weather import Wheather
        self.root.withdraw()  
        self.third_window = Wheather(self.main_window)
        
    def Database(self):
        from database import Database
        self.root.withdraw()  
        self.third_window = Database(self.main_window) 
        
    def Refresh(self):
        from monitor import Monitor
        self.root.withdraw()  
        self.third_window = Monitor(self)
        
    def Exit_func(self):
        self.ques =  messagebox.askyesno("EXIT","Do you really want to Exit")
        if self.ques == 1:
            self.root.destroy()
        else: 
            return   
          
# root = Tk()       
# ob = Monitor(root,color="white")
# root.mainloop()