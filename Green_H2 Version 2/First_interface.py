from tkinter import * 
from tkinter import messagebox
from time import strftime
import speech_recognition as sr
from data import Data
import webbrowser
import re
import serial
from Second_interface import Weather
import sys


class Into():
    def __init__(self,root):
        self.root = root
        self.root.state("zoomed")
        self.root.resizable(True,True)
        self.root.config(bg="#0d0d0d")
        self.root.title("Green Hydrogen")
        self.root.minsize(1550,800)
        self.root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\3-removebg-preview_1.ico")
        # ================================================== Variables ========================================================
        self.text1 = StringVar()
        self.learn = StringVar()
        
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
        
        self.Home = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Home 2.png")
        self.sub_home = self.Home.subsample(3,3)
        self.Home_button = Button(self.root,text="  Home",image=self.sub_home,bd=0,bg="#0d0d0d",fg="#27AE60",justify="center",activebackground="#0d0d0d",compound="left",font=("Arial Black",12,"bold"),activeforeground="#27AE60",cursor="hand2")
        self.Home_button.place(x=300,y=90,width=110,height=50)
        
        self.weather = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\monitoring.png")
        self.sub_weather = self.weather.subsample(3,3)
        self.Weather_button = Button(self.root,text="  Monitor",image=self.sub_weather,bd=0,bg="#0d0d0d",fg="white",justify="center",activebackground="#0d0d0d",compound="left",font=("Arial Black",12,"bold"),activeforeground="white",cursor="hand2",command=self.Monitor)
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
        
        
        # ==================================================== Frame 2 =======================================================
        self.search_box = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Rectangle 1 (2).png")
        search_box_label = Label(self.root,image=self.search_box,bg="white")
        search_box_label.place(x=350,y=200)
        
        self.search_entry = Entry(self.root,bd=0,justify="center",font=("Arial",25,"bold"),bg="#1D1D1D",fg="White",cursor="hand2",textvariable=self.text1,insertbackground="White")
        self.search_entry.place(x=416,y=205,width=725,height=55)
        
        self.Search = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\magnifying-glass.png")
        self.Sub_Search = self.Search.subsample(3,3)
        search = Button(self.root,image=self.Sub_Search,bg="#1D1D1D",bd=0,activebackground="#1D1D1D",cursor="hand2",command=self.search)
        search.place(x=370,y=210)
        
        self.voice = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\microphone.png")
        self.sub_voice = self.voice.subsample(3,3)
        voice = Button(self.root,image=self.sub_voice,bg="#1D1D1D",bd=0,activebackground="#1D1D1D",cursor="hand2",command=self.NLP)
        voice.place(x=1140,y=210)
        
        # ============================================================ Text ==========================================================
        
        text_H2_1 = "This is a system for managing green hydrogen production"
        Text_label_1 = Label(self.root,text=text_H2_1,fg="Black",bg="White",font=("Arial Black",32,"bold"))
        Text_label_1.place(x=90,y=450)
        
        text_H2_2 = "helps in the process of reading and storing data, monitoring and ensuring the safety \nof the green hydrogen production process"
        Text_label_2 = Label(self.root,text=text_H2_2,fg="Black",bg="White",font=("Arial Black",20,"bold"))
        Text_label_2.place(x=150,y=520)
        
        text_H2_3 = "Green hydrogen is one of the most important energies that will be used in the future \nso for more information click here"
        Text_label_3 = Label(self.root,text=text_H2_3,fg="Black",bg="White",font=("Arial Black",15,"bold"))
        Text_label_3.place(x=300,y=650)
        
        self.button_bg = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Rectangle 1 (3).png")
        btn_bg_label = Label(self.root,image=self.button_bg,bg="white")
        btn_bg_label.place(x=650,y=720)
        
        H2_link = Button(self.root,text="Learn more",bd=0,font=("Arial Black",18,"bold"),bg="#0D0D0D",fg="#27AE60",activebackground="#0D0D0D",activeforeground="#27AE60",cursor="hand2",command=self.Google)
        H2_link.place(x=685,y=725)
        
        self.history()
        self.time()
        
         
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
        
    def Google(self):
        webbrowser.open_new("https://www.iberdrola.com/sustainability/green-hydrogen")
        
        
    def NLP(self):
        try:
            port = self.is_port_open()
            ser = serial.Serial(f"{port}",9600)
            line = ser.readline().decode("utf-8")
            rec = sr.Recognizer()                       # للتعرف على الصوت 
            with sr.Microphone() as src:                # المكان الي هتستقبل منه الصوت علشان تتعرف عليه
                self.text1.set("How can I help You?")
            
                while True:
                    self.root.update()
                    self.audio = rec.listen(src)                     # هتستقبل الصوت من المايك
                    self.text = rec.recognize_google(self.audio)          # هنستخدم معرف جوجل علشان يتعؤف على الصوت
                    
                    sensor_values = re.findall(r"[0-9.]*\S",line)
                    self.temperature_1 = float(sensor_values[0])
                    self.temperature_H = float(sensor_values[1])
                    self.humuidity_1 = float(sensor_values[2])
                    self.humuidity_H = float(sensor_values[3])
                    self.hydrogen = int(sensor_values[4])
                    
                    result = re.findall(r"[Hh]umi\w+ of [Hh]ydrogen|[Tt]emp\w+ of [Hh]ydrogen|[Tt]emp\w+|[Hh]umi\w+|[Ww]ind\s[Ss]peed|[Cc]lose|Electri\w+|power|[Hh]ydrogen temp\w+|[Hh]ydrogen [Hh]umi\w+",self.text)
                    temp = re.findall(r"[Tt]emp\w+",self.text)
                    temp.append("")
                    humidity = re.findall(r"[Hh]umi\w+",self.text)
                    humidity.append("")
                    wind = re.findall(r"[Ww]ind\s[Ss]peed",self.text)
                    wind.append("")
                    Soler_panel = re.findall(r"Electri\w+|power",self.text)
                    Soler_panel.append("")
                    H_temp = re.findall(r"[Hh]ydrogen temp\w+|[Tt]emp\w+ of [Hh]ydrogen",self.text)
                    H_temp.append("")
                    H_humuidity = re.findall(r"[Hh]ydrogen [Hh]umi\w+|[Hh]umi\w+ of [Hh]ydrogen",self.text)
                    H_humuidity.append("")
                    close = re.findall(r"[Cc]lose",self.text)
                    close.append("")
                    self.text1.set(self.text)
                    
                 
                 
                    for x in range(len(result)):
                        
                            if temp[0] == result[x] :
                                
                                text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="White",insertbackground="white")
                                text.place(x=270,y=270,width=1000,height=150)
                                learn= f"Accroding to the current status temperature now is\n\t\t      {self.temperature_1}°C"
                                text.insert(END,learn)
                                return 
                                
                                
                            elif humidity[0] == result[x]:
                                
                                text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="White",insertbackground="white")
                                text.place(x=270,y=270,width=1000,height=150)
                                learn= f"Accroding to the current status Humuidity now is\n\t\t      {self.humuidity_1}%"
                                text.insert(END,learn)
                                return 
                            
                            elif wind[0] == result[x]:
                                text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="White",insertbackground="white")
                                text.place(x=270,y=270,width=1000,height=150)
                                learn= f"Accroding to the current status Wind Speed now is   {Data().current_speed}K/M"
                                text.insert(END,learn) 
                                return
                             
                            elif H_temp[0] == result[x]:
                                
                                text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="White",insertbackground="white")
                                text.place(x=270,y=270,width=1000,height=150)
                                learn= f"   Accroding to the current status Hydrogen\n  \tTemperature now is {self.temperature_H}°C"
                                text.insert(END,learn)
                                return 
                            
                            elif H_humuidity[0] == result[x]:
                                self.H_humuidity = line[15:20]
                                text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="White",insertbackground="white")
                                text.place(x=270,y=270,width=1000,height=150)
                                learn= f"Accroding to the current status Hydrogen\n Humuidity now is {self.humuidity_H}%"
                                text.insert(END,learn)
                                return 
                            
                            elif Soler_panel[0] == result[x]:
                                sunrise = Data().sunrise_1
                                sunset = Data().sunset_1
                                temperature = Data().current
                                electricity = Data.Solar_Panel_Elec(self=self,sunrise=sunrise,sunset=sunset,temperature=temperature)
                                text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="White",insertbackground="white")
                                text.place(x=270,y=270,width=1000,height=150)
                                learn= f"Accroding to the current temperature, Electricity       \tproduction will be {electricity} kilowatts"
                                text.insert(END,learn)
                                return 
                                
                            elif close[0] == result[x]:
                                self.text1.set("")
                                text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="White",insertbackground="white")
                                text.place(x=270,y=270,width=1000,height=150) 
                                text.delete("0.0",END)   
                                return
                               
        except:
                self.text1.set("")
                text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="white")
                text.place(x=70,y=140,width=850,height=340)
                learn= ""
                text.insert(END,learn)
                messagebox.showerror("WARNING","Something Wrong in Voice\n please Try Again")
        
        
    def is_port_open(self):
            try:
                ports = ["COM7","COM5"]
                for x in range(0,2):
                    if  serial.Serial(ports[x]).is_open == True:
                        return ports[x]             
            except serial.SerialException:
               return ports[x+1]   
            
    def search(self):
        port = self.is_port_open()
        ser = serial.Serial(f"{port}",9600)
        line = ser.readline().decode("utf-8")
        self.text = self.text1.get()
        sensor_values = re.findall(r"[0-9.]*\S",line)
        self.temperature_1 = float(sensor_values[0])
        self.temperature_H = float(sensor_values[1])
        self.humuidity_1 = float(sensor_values[2])
        self.humuidity_H = float(sensor_values[3])
        self.hydrogen = int(sensor_values[4])
        result = re.findall(r"[Hh]umi\w+ of [Hh]ydrogen|[Tt]emp\w+ of [Hh]ydrogen|[Tt]emp\w+|[Hh]umi\w+|[Ww]ind\s[Ss]peed|[Cc]lose|Electri\w+|power|[Hh]ydrogen temp\w+|[Hh]ydrogen [Hh]umi\w+",self.text)
        temp = re.findall(r"[Tt]emp\w+",self.text)
        temp.append("")
        humidity = re.findall(r"[Hh]umi\w+",self.text)
        humidity.append("")
        wind = re.findall(r"[Ww]ind\s[Ss]peed",self.text)
        wind.append("")
        Soler_panel = re.findall(r"[El]ectri\w+|power",self.text)
        Soler_panel.append("")
        H_temp = re.findall(r"[Hh]ydrogen temp\w+|[Tt]emp\w+ of [Hh]ydrogen",self.text)
        H_temp.append("")
        H_humuidity = re.findall(r"[Hh]ydrogen [Hh]umi\w+|[Hh]umi\w+ of [Hh]ydrogen",self.text)
        H_humuidity.append("")
        close = re.findall(r"[Cc]lose",self.text)
        close.append("")
        print(result)
        if self.text1.get() == "":
            messagebox.showwarning("Warning","Please Enter your search")
       
            
        for x in range(len(result)):
                
                
                if result[x] == temp[0]  :
                    
                    text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="White",insertbackground="white")
                    text.place(x=270,y=270,width=1000,height=150)
                    learn= f"Accroding to the current status temperature now is\n\t\t      {self.temperature_1}°C"
                    text.insert(END,learn)
                                     
                elif humidity[0] == result[x]:
                    
                    text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="White",insertbackground="white")
                    text.place(x=270,y=270,width=1000,height=150)
                    learn= f"Accroding to the current status Humuidity now is\n\t\t      {self.humuidity_1}%"
                    text.insert(END,learn)
                               
                elif wind[0] == result[x]:
                    text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="White",insertbackground="white")
                    text.place(x=270,y=270,width=1000,height=150)
                    learn= f"Accroding to the current status Wind Speed now is   {Data().current_speed}K/M"
                    text.insert(END,learn) 
                    
                elif H_temp[0] == result[x]:
                    self.H_temp = line[41:46]
                    text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="White",insertbackground="white")
                    text.place(x=270,y=270,width=1000,height=150)
                    learn= f"Accroding to the current status Hydrogen\n Temperature now is {self.temperature_H}°C"
                    text.insert(END,learn)
                    return 
                            
                elif H_humuidity[0] == result[x]:
                    self.H_humuidity = line[15:20]
                    text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="White",insertbackground="white")
                    text.place(x=270,y=270,width=1000,height=150)
                    learn= f"Accroding to the current status Hydrogen\n Humuidity now is {self.humuidity_H}%"
                    text.insert(END,learn)
                    return 
                
                elif Soler_panel[0] == result[x]:
                    sunrise = Data().sunrise_1
                    sunset = Data().sunset_1
                    temperature = Data().current
                    electricity = Data.Solar_Panel_Elec(self=self,sunrise=sunrise,sunset=sunset,temperature=temperature)
                    text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="White",insertbackground="white")
                    text.place(x=270,y=270,width=1000,height=150)
                    learn= f"Accroding to the current temperature, Electricity       \tproduction will be {electricity} kilowatts"
                    text.insert(END,learn)
                    return
                   
                elif close[0] == result[x]:
                    self.text1.set("")
                    text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="White",insertbackground="white")
                    text.place(x=270,y=270,width=1000,height=150)
                    text.delete("0.0",END)   
                    return 
                
                
    def Monitor (self):
        self.root.withdraw()
        self.eather = Weather(self)
        
    def Database (self):
        from Third_interface import Database
        self.root.withdraw()
        self.eather = Database(self.exit_function)
        
    
    def Refresh(self):
        self.text1.set("")
        text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="White",insertbackground="white")
        text.place(x=270,y=270,width=1000,height=150)
        learn= ""
        text.insert(END,learn)
        
    def exit_function(self):
        self.root.destroy()
        self.destroy()
    def Exit_func(self):
            self.ques =  messagebox.askyesno("EXIT","Do You Really Want to Exit?")
            if self.ques == 1:
                root.destroy()
                sys.exit()
            else: 
                return


root = Tk()
ob = Into(root)
root.mainloop()