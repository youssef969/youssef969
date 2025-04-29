from tkinter import * 
from tkinter import messagebox
from time import strftime
import speech_recognition as sr
from data import Data
from Weather import Wheather
from database import Database
import re
import serial

 

class Into():
    def __init__(self,root):
        self.root = root
        self.root.geometry("900x500+350+150")
        self.root.resizable(False,False)
        self.root.config(bg="white")
        self.root.title("Green Hydrogen")
        self.root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\1710162623466-removebg-preview.ico")
        
        # ================================================== Frames ============================================================
        self.fr1 = Frame(self.root,bg="#27AE60")
        self.fr1.place(x=50,y=0,width=850,height=80)
       
        fr2 = Frame(self.root,bg="#7DCEA0")
        fr2.place(x=0,y=0,width=50,height=500)
        
        fr3 = Frame(self.root,bg="#27AE60")
        fr3.place(x=50,y=125,width=850,height=5)
        
        # ================================================== Variables ========================================================
        self.text1 = StringVar()
        self.learn = StringVar()
        # =================================================== Frame 1 =====================================================
        self.image = PhotoImage(file ="C:\\Users\\Computec\\Downloads\\PNG Icons\\1710162623466-removebg-preview.png")
        self.sub = self.image.subsample(5,5)
        image_label = Label(self.fr1,image=self.sub,bg="#27AE60")
        image_label.place(x=760,y=0)
        
        GreenH = Label(self.fr1,text="Green Hydorgen",fg="white",font=("Pacifico",19,"bold"),bg="#27AE60")
        GreenH.place(x=540,y=7)
        
        # ==================================================== Root =======================================================
        self.Search_bar = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Copy of search.png")
        self.sub_search_bar = self.Search_bar.subsample(2,2)
        search_bar = Label(self.root,image=self.sub_search_bar,bg="white")
        search_bar.place(x=350,y=80)
        
        self.Search = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\magnifying-glass.png")
        self.Sub_Search = self.Search.subsample(5,5)
        search = Button(self.root,image=self.Sub_Search,bg="#434343",bd=0,activebackground="#434343",cursor="hand2",command=self.search)
        search.place(x=544,y=87)
        
        self.voice = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\microphone.png")
        self.sub_voice = self.voice.subsample(5,5)
        voice = Button(self.root,image=self.sub_voice,bg="#434343",bd=0,activebackground="#434343",cursor="hand2",command=self.NLP)
        voice.place(x=370,y=87)
        
        self.search_entry = Entry(self.root,bd=0,justify="center",font=("Arial",10,"bold"),bg="#434343",fg="White",cursor="hand2",textvariable=self.text1,insertbackground="White")
        self.search_entry.place(x=395,y=87,width=145,height=29)
        
        # ===================================================== Frame 2 ====================================================
        self.Home = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\home 2.png")
        self.sub_home = self.Home.subsample(5,5)
        self.Home_button = Button(fr2,image=self.sub_home,bd=0,bg="#7DCEA0",justify="center",activebackground="#7DCEA0")
        self.Home_button.place(x=10,y=20,width=30,height=60)
        
        self.weather = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\rainy-day.png")
        self.sub_weather = self.weather.subsample(5,5)
        Weather_button =  Button(fr2,image=self.sub_weather,bd=0,bg="#7DCEA0",justify="center",activebackground="#7DCEA0",command=self.Weather)
        Weather_button.place(x=10,y=80,width=30,height=60)
        
        self.monitor = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Monitor.png")
        self.sub_monitor = self.monitor.subsample(5,5)
        Monitor_button =  Button(fr2,image=self.sub_monitor,bd=0,bg="#7DCEA0",justify="center",activebackground="#7DCEA0",command=self.Monitor)
        Monitor_button.place(x=10,y=140,width=30,height=60)
        
        self.database = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\database (1).png")
        self.sub_database = self.database.subsample(5,5)
        database_button = Button(fr2,image=self.sub_database,bd=0,bg="#7DCEA0",justify="center",activebackground="#7DCEA0",command=self.Database_func)
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
        Exit_button = Button(fr2,image=self.sub_Exit,bd=0,bg="#7DCEA0",justify="center",activebackground="#7DCEA0",command=self.Exit_func)
        Exit_button.place(x=13,y=380,width=30,height=65)
        
       
        self.history()
        self.time()
        
         
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
            
    def NLP(self):
        #try:
            ser = serial.Serial('COM5',9600)
            line = ser.readline().decode("utf-8")
            rec = sr.Recognizer()                       # للتعرف على الصوت 
            with sr.Microphone() as src:                # المكان الي هتستقبل منه الصوت علشان تتعرف عليه
                self.text1.set("How can I help You?")
            
                while True:
                    root.update()
                    self.audio = rec.listen(src)                     # هتستقبل الصوت من المايك
                    self.text = rec.recognize_google(self.audio)          # هنستخدم معرف جوجل علشان يتعؤف على الصوت
                    
                    result = re.findall(r"[Hh]umi\w+ of [Hh]ydrogen|[Tt]emp\w+ of [Hh]ydrogen|[Tt]emp\w+|[Hh]umi\w+|[Ww]ind\[Ss]peed|[Cc]lose|Electri\w+|power|[Hh]ydrogen temp\w+|[Hh]ydrogen [Hh]umi\w+",self.text)
                    temp = re.findall(r"[Tt]emp\w+",self.text)
                    temp.append("")
                    humidity = re.findall(r"[Hh]umi\w+",self.text)
                    humidity.append("")
                    wind = re.findall(r"[Ww]ind\[Ss]peed",self.text)
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
                    print(result)
                    
                           
                    
                        
                        
                 
                    for x in range(len(result)):
                        
                            if temp[0] == result[x] :
                                self.temperature = line[36:38]
                                text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="white",insertbackground="white")
                                text.place(x=70,y=140,width=840,height=340)
                                learn= f"Accroding to the current status temperature now is {self.temperature}°C"
                                text.insert(END,learn)
                                return 
                                
                                
                            elif humidity[0] == result[x]:
                                self.humuidity = line[10:12]
                                text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="white",insertbackground="white")
                                text.place(x=70,y=140,width=840,height=340)
                                learn= f"Accroding to the current status Humuidity now is {self.humuidity}%"
                                text.insert(END,learn)
                                return 
                            
                            elif wind[0] == result[x]:
                                text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="white",insertbackground="white")
                                text.place(x=70,y=140,width=850,height=340)
                                learn= f"Accroding to the current status Wind Speed now is {Data().current_speed}K/M"
                                text.insert(END,learn) 
                                return
                             
                            elif H_temp[0] == result[x]:
                                self.H_temp = line[41:46]
                                text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="white",insertbackground="white")
                                text.place(x=70,y=140,width=840,height=340)
                                learn= f"Accroding to the current status Hydrogen\n Temperature now is {self.H_temp}%"
                                text.insert(END,learn)
                                return 
                            
                            elif H_humuidity[0] == result[x]:
                                self.H_humuidity = line[15:20]
                                text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="white",insertbackground="white")
                                text.place(x=70,y=140,width=840,height=340)
                                learn= f"Accroding to the current status Hydrogen\n Humuidity now is {self.H_humuidity}%"
                                text.insert(END,learn)
                                return 
                            
                            elif Soler_panel[0] == result[x]:
                                sunrise = Data().sunrise_1
                                sunset = Data().sunset_1
                                temperature = Data().current
                                electricity = Data.Solar_Panel_Elec(self=self,sunrise=sunrise,sunset=sunset,temperature=temperature)
                                text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="white",insertbackground="white")
                                text.place(x=70,y=140,width=850,height=340)
                                learn= f"Accroding to the current temperature, Electricity production will be {electricity} kilowatts"
                                text.insert(END,learn)
                                return 
                                
                            elif close[0] == result[x]:
                                self.text1.set("")
                                text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="white")
                                text.place(x=70,y=140,width=850,height=340) 
                                text.delete("0.0",END)   
                                return
                               
        # except:
        #     self.text1.set("")
        #     text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="white")
        #     text.place(x=70,y=140,width=850,height=340)
        #     learn= ""
        #     text.insert(END,learn)
        #     messagebox.showerror("WARNING","Something Wrong in Voice\n please Try Again")
                                
    def search(self):
        ser = serial.Serial('COM5',9600)
        line = ser.readline().decode("utf-8")
        self.text = self.text1.get()
        result = re.findall(r"[Hh]umi\w+ of [Hh]ydrogen|[Tt]emp\w+ of [Hh]ydrogen|[Tt]emp\w+|[Hh]umi\w+|[Ww]ind\[Ss]peed|[Cc]lose|Electri\w+|power|[Hh]ydrogen temp\w+|[Hh]ydrogen [Hh]umi\w+",self.text)
        temp = re.findall(r"[Tt]emp\w+",self.text)
        temp.append("")
        humidity = re.findall(r"[Hh]um\w+",self.text)
        humidity.append("")
        wind = re.findall(r"[Ww]ind\[Ss]peed",self.text)
        wind.append("")
        Soler_panel = re.findall(r"[El]ectri\w+|power",self.text)
        Soler_panel.append("")
        H_temp = re.findall(r"[Hh]ydrogen temp\w+|[Tt]emp\w+ of [Hh]ydrogen",self.text)
        H_temp.append("")
        H_humuidity = re.findall(r"[Hh]ydrogen [Hh]umi\w+|[Hh]umi\w+ of [Hh]ydrogen",self.text)
        H_humuidity.append("")
        close = re.findall(r"[Cc]lose",self.text)
        close.append("")
        if self.text1.get() == "":
            messagebox.showwarning("Warning","Please Enter your search")
       
            
        for x in range(len(result)):
                
                if result[x] == temp[0]  :
                    self.temperature = line[36:38]
                    text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="white",insertbackground="white")
                    text.place(x=70,y=140,width=840,height=340)
                    learn= f"Accroding to the current status temperature now is {self.temperature}°C"
                    text.insert(END,learn)
                                     
                elif humidity[0] == result[x]:
                    self.humuidity = line[10:12]
                    text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="white",insertbackground="white")
                    text.place(x=70,y=140,width=840,height=340)
                    learn= f"Accroding to the current status Humuidity now is {self.humuidity}%"
                    text.insert(END,learn)
                               
                elif wind[0] == result[x]:
                    text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="white",insertbackground="white")
                    text.place(x=70,y=140,width=850,height=340)
                    learn= f"Accroding to the current status Wind Speed now is {Data().current_speed}K/M"
                    text.insert(END,learn) 
                    
                elif H_temp[0] == result[x]:
                    self.H_temp = line[41:46]
                    text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="white",insertbackground="white")
                    text.place(x=70,y=140,width=840,height=340)
                    learn= f"Accroding to the current status Hydrogen\n Temperature now is {self.H_temp}%"
                    text.insert(END,learn)
                    return 
                            
                elif H_humuidity[0] == result[x]:
                    self.H_humuidity = line[15:20]
                    text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="white",insertbackground="white")
                    text.place(x=70,y=140,width=840,height=340)
                    learn= f"Accroding to the current status Hydrogen\n Humuidity now is {self.H_humuidity}%"
                    text.insert(END,learn)
                    return 
                
                elif Soler_panel[0] == result[x]:
                    sunrise = Data().sunrise_1
                    sunset = Data().sunset_1
                    temperature = Data().current
                    electricity = Data.Solar_Panel_Elec(self=self,sunrise=sunrise,sunset=sunset,temperature=temperature)
                    text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="white",insertbackground="white")
                    text.place(x=70,y=140,width=850,height=340)
                    learn= f"Accroding to the current temperature, Electricity production will be {electricity} kilowatts"
                    text.insert(END,learn)
                   
                elif close[0] == result[x]:
                    self.text1.set("")
                    text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="white",insertbackground="white")
                    text.place(x=70,y=140,width=850,height=340) 
                    text.delete("0.0",END)   
                    return 
    
                                 
    def Weather (self):
        self.root.withdraw()
        self.eather = Wheather(self)
        
        
    def Monitor(self):
        from monitor import Monitor
        self.root.withdraw()  
        self.third_window = Monitor(self)
        
        
    def Database_func(self):
        self.root.withdraw()
        self.second_window = Database(self)
        
        
    def Refresh(self):
        self.text1.set("")
        text = Text(self.root, font=("Arial",30,"bold"),bd=0,background="white",insertbackground="white")
        text.place(x=70,y=140,width=850,height=340)
        learn= ""
        text.insert(END,learn)

  
    def Exit_func(self):
        self.ques =  messagebox.askyesno("EXIT","Do you really want to Exit")
        if self.ques == 1:
            root.destroy()
        else: 
            return
      
root = Tk()
ob = Into(root)   
root.mainloop()