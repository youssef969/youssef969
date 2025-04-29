from tkinter import * 
from tkinter import messagebox
from tkinter import ttk 
from time import strftime
from Weather import Wheather
import pymysql

class Database(Tk):
    def __init__(self,main_window):
        self.main_window = main_window
        self.root = Toplevel()
        self.root.geometry("950x650+350+50")  
        self.root.resizable(False,False)
        self.root.config(bg="white")
        self.root.title("Database")
        self.root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\1710162623466-removebg-preview.ico")
        
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
        
        
        self.weather = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\rainy-day.png")
        self.sub_weather = self.weather.subsample(5,5)
        weather_button_1 =  Button(fr2,image=self.sub_weather,bd=0,bg="#7DCEA0",justify="center",activebackground="#7DCEA0",command=self.Weather)
        weather_button_1.place(x=10,y=80,width=30,height=60)
        
        self.monitor = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Monitor.png")
        self.sub_monitor = self.monitor.subsample(5,5)
        Monitor_button =  Button(fr2,image=self.sub_monitor,bd=0,bg="#7DCEA0",justify="center",activebackground="#7DCEA0",command=self.Monitor)
        Monitor_button.place(x=10,y=140,width=30,height=60)
        
        self.database = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\database.png")
        self.sub_database = self.database.subsample(5,5)
        database_button = Button(fr2,image=self.sub_database,bd=0,bg="#7DCEA0",justify="center",activebackground="#7DCEA0")
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
        
        database_frame = Frame(self.root,bg="white")
        database_frame.place(x=50,y=80,width=900,height=570)
        
        scrollbar_y = Scrollbar(database_frame,orient="vertical")
        # --------------------- treeview ---------------------
        
        self.hydrogen_database= ttk.Treeview(database_frame,columns=("max_temp","min_temp","precipitation","wind","weather","solar_panel","hydrogen"), xscrollcommand= scrollbar_y.set) 
        self.hydrogen_database.place(x=0 , y=0,width=900,height=570)
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
        self.Show_data()
        self.time()
        self.history()
        
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
        
    def Show_data(self):
        con = pymysql.connect( host="localhost", user="root", password="123456", database="Green_hydrogen")
        cur = con.cursor()  
        cur.execute("Select * from Production")
        rows = cur.fetchall()
        if len(rows)!= 0 : 
            self.hydrogen_database.delete(*self.hydrogen_database.get_children())
            for row in rows:
                self.hydrogen_database.insert("",END,values=row)
        #messagebox.showinfo("SUCCESS","THE DATA IS SHOWN NOW")
        con.commit()
        con.close()
        
        
    def Add_data (self):
            con = pymysql.connect( host="localhost", user="root", password="123456", database="gym")
            cur = con.cursor()   
            cur.execute("insert into Production values (%s,%s,%s,%s)",(self.week_var.get(),self.Exercise_var.get(),self.weight_var.get(),self.iteration_var.get()))
            self.hydrogen_database.after(2000,self.Add_data)
            con.commit()
            con.close()
            
        
    def home(self):
        self.root.destroy()
        self.main_window.root.deiconify()
        
             
    def Weather(self):
        self.root.withdraw()  
        self.third_window = Wheather(self.main_window)
        
            
    def Monitor(self):
        from monitor import Monitor
        self.root.withdraw()  
        self.third_window = Monitor(self.main_window)
        
        
    def Refresh(self):
        self.root.withdraw()
        self.second_window = Database(self)
        
     
    def Exit_func(self):
        self.ques =  messagebox.askyesno("EXIT","Do you really want to Exit")
        if self.ques == 1:
            self.root.destroy()
        else: 
            return   