import PIL.Image
from customtkinter import * 
from tkinter import * 
import PIL
from tkinter import messagebox
from time import strftime
import speech_recognition as sr
from data import Data
import webbrowser
import re
import serial
import sys
import warnings
from threading import Thread
warnings.filterwarnings("ignore")

class Into():
    def __init__(self,root):
        self.root = root 
        self.root.state("zoomed")
        self.root.resizable(True,True)
        self.root.config(bg="#0d0d0d")
        self.root.title("Green Hydrogen")
        self.root.minsize(1550,800)
        self.root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\3-removebg-preview_1.ico")
        
        # ================================================== Variables ==========================================
        self.learn = StringVar()
        self.x = IntVar()
        # ============================================== Frames ==================================================
        self.Frame = CTkFrame(self.root,width=1550,height=1000,corner_radius=180,bg_color=("#0d0d0d","#dbdbdb"))
        self.Frame.place(x=-7,y=150)
        
        self.Frame2 = CTkFrame(self.root,width=300,height=70,corner_radius=90,bg_color=("#0d0d0d","#dbdbdb"),fg_color=("#1d1d1d","white"))
        self.Frame2.place(x=600,y=0)
        
        
        # ============================================== Frame 1 =================================================== 
        self.image = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\3-removebg-preview.png")
        self.sub = CTkImage(light_image=self.image,dark_image=self.image,size=(60,60))
        self.image_label = CTkLabel(self.Frame2,image=self.sub,fg_color=("#1d1d1d","#ffffff"),text="")
        self.image_label.place(x=25,y=5)
        
        self.GreenH = CTkLabel(self.Frame2,text="Green Hydorgen",text_color=("white","black"),font=("Pacifico",22,"bold"),fg_color=("#1d1d1d","white"))
        self.GreenH.place(x=105,y=10)
        
        self.Home = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\Home 2.png")
        self.sub_home = CTkImage(light_image=self.Home,size=(25,25),dark_image=self.Home)
        self.Home_button = CTkButton(self.root,text="  Home",image=self.sub_home,bg_color="#0d0d0d",hover_color="#2b2b2b",fg_color="#0d0d0d",text_color="#27AE60",compound="left",font=("Arial Black",15,"bold"),width=110,height=50,corner_radius=90)
        self.Home_button.place(x=300,y=90)
        
        self.weather = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\dashboard_white.png")
        self.weather2 = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\dashboard_black.png")
        self.sub_weather = CTkImage(light_image=self.weather,size=(35,35),dark_image=self.weather2)
        self.Weather_button = CTkButton(self.root,text="  Monitor",image=self.sub_weather,bg_color="#0d0d0d",hover_color="#2b2b2b",fg_color="#0d0d0d",text_color="white",compound="left",font=("Arial Black",15,"bold"),width=110,height=50,corner_radius=90,command=self.Monitor)
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
        self.Setting_button = CTkButton(self.root,text="  Settings",image=self.sub_Setting,bg_color="#0d0d0d",hover_color="#2b2b2b",fg_color="#0d0d0d",text_color="white",compound="left",font=("Arial Black",15,"bold"),width=110,height=50,corner_radius=90,command=self.Settings)
        self.Setting_button.place(x=970,y=90)
        
        self.Exit = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\logout_white.png")
        self.Exit2 = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\logout_black.png")

        self.sub_Exit = CTkImage(light_image=self.Exit,size=(25,25),dark_image=self.Exit2)
        self.Exit_button = CTkButton(self.root,text="  Exit",image=self.sub_Exit,bg_color="#0d0d0d",hover_color="#2b2b2b",fg_color="#0d0d0d",text_color="white",compound="left",font=("Arial Black",15,"bold"),width=110,height=50,corner_radius=90,command=self.Exit_func)
        self.Exit_button.place(x=1140,y=90)
        
        self.date_lbl = CTkLabel(self.root,font =('Arial Black',20,'bold'),text_color='white',fg_color="#0D0D0D",bg_color="#0D0D0D")
        self.hist_lbl = CTkLabel(self.root,font =('Arial Black',20,'bold'),text_color='white',fg_color="#0D0D0D",bg_color="#0D0D0D")
        
        # ==================================================== Frame 2 =======================================================
        
        self.search_entry = CTkEntry(self.root,placeholder_text="Search",placeholder_text_color="white",font=("Arial",25,"bold"),bg_color="#dbdbdb",fg_color="#0d0d0d",text_color="White",width=725,height=55,corner_radius=90,justify="center")
        self.search_entry.place(x=416,y=205)
        
        img = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\search_white.png")
        img2 = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\search_black.png")
        self.search_im = CTkImage(light_image=img,size=(30,30),dark_image=img2)
        self.search_btn = CTkButton(self.root,image=self.search_im,fg_color="#0d0d0d",bg_color="#0d0d0d",command=self.search_2,text="",width=10,corner_radius=180,hover_color="#2b2b2b")
        self.search_btn.place(x=426,y=213)
        
        img = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\microphone_white.png")
        img2 = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\microphone_black.png")
        self.voice_im = CTkImage(light_image=img,size=(30,30),dark_image=img2)
        self.voice = CTkButton(self.root,image=self.voice_im,fg_color="#0d0d0d",bg_color="#0d0d0d",command=self.NLP_2,text="",width=10,corner_radius=180,hover_color="#2b2b2b")
        self.voice.place(x=1066,y=213)
        
        # ============================================================ Text ==========================================================
        
        text_H2_1 = "This is a system for managing green hydrogen production"
        self.Text_label_1 = CTkLabel(self.root,text=text_H2_1,text_color="Black",bg_color="#dbdbdb",font=("Arial Black",32,"bold"))
        self.Text_label_1.place(relx=0.5,anchor=CENTER,y=450)
        
        text_H2_2 = "helps in the process of reading and storing data, monitoring and ensuring the safety \nof the green hydrogen production process"
        self.Text_label_2 = CTkLabel(self.root,text=text_H2_2,text_color="Black",bg_color="#dbdbdb",font=("Arial Black",20,"bold"))
        self.Text_label_2.place(relx=0.5,anchor=CENTER,y=520)
        
        text_H2_3 = "Green hydrogen is one of the most important energies that will be used in the future \nso for more information click here"
        self.Text_label_3 = CTkLabel(self.root,text=text_H2_3,text_color="Black",bg_color="#dbdbdb",font=("Arial Black",15,"bold"))
        self.Text_label_3.place(relx=0.5,anchor=CENTER,y=650)
        
        self.H2_link = CTkButton(self.root,text="Learn more",font=("Arial Black",18,"bold"),text_color="#27AE60",bg_color="#dbdbdb",fg_color="#0D0D0D",command=self.Google,corner_radius=90,width=180,height=70,hover_color="#2b2b2b")
        self.H2_link.place(relx=0.5,anchor=CENTER,y=725)
        
        self.change_mode()
        self.history()
        self.time()
          
    def change_mode(self):
        file = open("D:\\My Download\\Files\\Projects\\Green Hydrogen Project\\Green_H2 Version 3\\mode.txt",'r')
        self.mode(mode = file.read())
        file.close()
              
    
    def mode(self,mode):
        if mode == "Dark" :                               
            set_appearance_mode("dark") 
            root.config(bg="#dbdbdb")
            self.Home_button.configure(fg_color="#dbdbdb",text_color="#27ae60",bg_color="#dbdbdb",hover_color="white")
            self.Weather_button.configure(fg_color="#dbdbdb",text_color="Black",bg_color="#dbdbdb",hover_color="white")
            self.database_button.configure(fg_color="#dbdbdb",text_color="Black",bg_color="#dbdbdb",hover_color="white")
            self.refresh_button.configure(fg_color="#dbdbdb",text_color="Black",bg_color="#dbdbdb",hover_color="white")
            self.Setting_button.configure(fg_color="#dbdbdb",text_color="Black",bg_color="#dbdbdb",hover_color="white")
            self.Exit_button.configure(fg_color="#dbdbdb",text_color="Black",bg_color="#dbdbdb",hover_color="white")
            self.date_lbl.configure(text_color='Black',fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.hist_lbl.configure(text_color='Black',fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.H2_link.configure(bg_color="#2b2b2b",hover_color="white",fg_color="#dbdbdb")
            self.Text_label_1.configure(fg_color="#2b2b2b",text_color="#dbdbdb")
            self.Text_label_2.configure(fg_color="#2b2b2b",text_color="#dbdbdb")
            self.Text_label_3.configure(fg_color="#2b2b2b",text_color="#dbdbdb")
            self.search_entry.configure(bg_color="#2b2b2b",fg_color="#ffffff",text_color="Black",placeholder_text_color="black")
            self.voice.configure(fg_color="#ffffff",bg_color="#ffffff",hover_color="#dbdbdb")
            self.search_btn.configure(fg_color="#ffffff",bg_color="#ffffff",hover_color="#dbdbdb")
        else:
            set_appearance_mode("light") 
            root.config(bg="#0d0d0d")
            self.Home_button.configure(fg_color="#0d0d0d",text_color="#27ae60",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.Weather_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.database_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.refresh_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.Setting_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.Exit_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.date_lbl.configure(text_color='white',fg_color="#0D0D0D",bg_color="#0D0D0D")
            self.hist_lbl.configure(text_color='white',fg_color="#0D0D0D",bg_color="#0D0D0D")
            self.Text_label_1.configure(fg_color="#dbdbdb",text_color="Black")
            self.Text_label_2.configure(fg_color="#dbdbdb",text_color="Black")
            self.Text_label_3.configure(fg_color="#dbdbdb",text_color="Black")
            self.H2_link.configure(bg_color="#dbdbdb",fg_color="#0d0d0d",hover_color="#2b2b2b")
            self.search_entry.configure(bg_color="#dbdbdb",fg_color="#0d0d0d",text_color="White",placeholder_text_color="White")
            self.voice.configure(fg_color="#0d0d0d",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.search_btn.configure(fg_color="#0d0d0d",bg_color="#0d0d0d",hover_color="#2b2b2b") 
            


               
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
        
    def Google(self):
        webbrowser.open_new("https://www.iberdrola.com/sustainability/green-hydrogen")
        
        
    def NLP(self):
        # try:
            
            port = self.is_port_open()
            ser = serial.Serial(f"{port}",9600)
            line = ser.readline().decode("utf-8")
            rec = sr.Recognizer()                       # للتعرف على الصوت 
            with sr.Microphone() as src:                # المكان الي هتستقبل منه الصوت علشان تتعرف عليه
                self.search_entry.delete(0,END)
                self.search_entry.insert(0,"How can I help You?")
            
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
                    self.search_entry.delete(0,END)
                    self.search_entry.insert(0,self.text)
                    
                 
                 
                    for x in range(len(result)):
                        
                            if temp[0] == result[x] :
                                
                                textbox=CTkTextbox(self.root, font=("Arial",30,"bold"),fg_color=("#dbdbdb","#2b2b2b"),width=1000,height=150,bg_color=("#dbdbdb","#2b2b2b"),border_width=0)
                                textbox.place(x=270,y=270)
                                learn= f"          Accroding to the current status temperature now is {self.temperature_1}°C"
                                textbox.insert(END,learn)
                                return 
                                
                                
                            elif humidity[0] == result[x]:
                                
                                textbox=CTkTextbox(self.root, font=("Arial",30,"bold"),fg_color=("#dbdbdb","#2b2b2b"),width=1000,height=150,bg_color=("#dbdbdb","#2b2b2b"),border_width=0)
                                textbox.place(x=270,y=270)
                                learn= f"          Accroding to the current status Humuidity now is {self.humuidity_1}%"
                                textbox.insert(END,learn)
                                return 
                            
                            elif wind[0] == result[x]:
                                textbox=CTkTextbox(self.root, font=("Arial",30,"bold"),fg_color=("#dbdbdb","#2b2b2b"),width=1000,height=150,bg_color=("#dbdbdb","#2b2b2b"),border_width=0)
                                textbox.place(x=270,y=270)
                                learn= f"    Accroding to the current status Wind Speed now is {Data().current_speed}K/M"
                                textbox.insert(END,learn) 
                                return
                             
                            elif H_temp[0] == result[x]:
                                
                                textbox=CTkTextbox(self.root, font=("Arial",29,"bold"),fg_color=("#dbdbdb","#2b2b2b"),width=1000,height=150,bg_color=("#dbdbdb","#2b2b2b"),border_width=0)
                                textbox.place(x=270,y=270)
                                learn= f"     Accroding to the current status Hydrogen Temperature now is {self.temperature_H}°C"
                                textbox.insert(END,learn)
                                return 
                            
                            elif H_humuidity[0] == result[x]:
                                self.H_humuidity = line[15:20]
                                textbox=CTkTextbox(self.root, font=("Arial",30,"bold"),fg_color=("#dbdbdb","#2b2b2b"),width=1000,height=150,bg_color=("#dbdbdb","#2b2b2b"),border_width=0)
                                textbox.place(x=270,y=270)
                                learn= f"Accroding to the current status Hydrogen Humuidity now is {self.humuidity_H}%"
                                textbox.insert(END,learn)
                                return 
                            
                            elif Soler_panel[0] == result[x]:
                                sunrise = Data().sunrise_1
                                sunset = Data().sunset_1
                                temperature = Data().current
                                electricity = Data.Solar_Panel_Elec(self=self,sunrise=sunrise,sunset=sunset,temperature=temperature)
                                textbox=CTkTextbox(self.root, font=("Arial",30,"bold"),fg_color=("#dbdbdb","#2b2b2b"),width=1000,height=150,bg_color=("#dbdbdb","#2b2b2b"),border_width=0)
                                textbox.place(x=270,y=270)
                                learn= f"Accroding to the current temperature, Electricity production will be                                           {electricity} kilowatts"
                                textbox.insert(END,learn)
                                return 
                                
                            elif close[0] == result[x]:
                                self.search_entry.delete(0,END)
                                textbox=CTkTextbox(self.root, font=("Arial",30,"bold"),fg_color=("#dbdbdb","#2b2b2b"),width=1000,height=150,bg_color=("#dbdbdb","#2b2b2b"),border_width=0)
                                textbox.place(x=270,y=270)
                                textbox.delete("0.0",END)   
                                return
                               
        # except:
        #         self.search_entry.delete(0,END)
        #         textbox=CTkTextbox(self.root, font=("Arial",30,"bold"),fg_color=("#dbdbdb","#2b2b2b"),width=1000,height=150,bg_color=("#dbdbdb","#2b2b2b"),border_width=0)
        #         textbox.place(x=270,y=270)
        #         learn= ""
        #         textbox.insert(END,learn)
        #         messagebox.showerror("WARNING","Something Wrong in Voice\n please Try Again")
    
    def NLP_2(self):
        self.t1 = Thread(target=self.NLP)
        self.t1.start()
        
    def search_2(self):
        self.t1 = Thread(target=self.search)
        self.t1.start()
        
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
        self.text = self.search_entry.get()
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
        if self.search_entry.get() == "":
            messagebox.showwarning("Warning","Please Enter your search")
       
            
        for x in range(len(result)):
                
                
                if result[x] == temp[0]  :
                    
                    textbox=CTkTextbox(self.root, font=("Arial",30,"bold"),fg_color=("#dbdbdb","#2b2b2b"),width=1000,height=150,bg_color=("#dbdbdb","#2b2b2b"),border_width=0)
                    textbox.place(x=270,y=270)
                    learn= f"          Accroding to the current status temperature now is {self.temperature_1}°C"
                    textbox.insert(END,learn)
                                     
                elif humidity[0] == result[x]:
                    
                    textbox=CTkTextbox(self.root, font=("Arial",30,"bold"),fg_color=("#dbdbdb","#2b2b2b"),width=1000,height=150,bg_color=("#dbdbdb","#2b2b2b"),border_width=0)
                    textbox.place(x=270,y=270)
                    learn= f"          Accroding to the current status Humuidity now is {self.humuidity_1}%"
                    textbox.insert(END,learn)
                               
                elif wind[0] == result[x]:
                    textbox=CTkTextbox(self.root, font=("Arial",30,"bold"),fg_color=("#dbdbdb","#2b2b2b"),width=1000,height=150,bg_color=("#dbdbdb","#2b2b2b"),border_width=0)
                    textbox.place(x=270,y=270)
                    learn= f"    Accroding to the current status Wind Speed now is   {Data().current_speed}K/M"
                    textbox.insert(END,learn) 
                    
                elif H_temp[0] == result[x]:
                    self.H_temp = line[41:46]
                    textbox=CTkTextbox(self.root, font=("Arial",29,"bold"),fg_color=("#dbdbdb","#2b2b2b"),width=1000,height=150,bg_color=("#dbdbdb","#2b2b2b"),border_width=0)
                    textbox.place(x=270,y=270)
                    learn= f"     Accroding to the current status Hydrogen Temperature now is {self.temperature_H}°C"
                    textbox.insert(END,learn)
                    return 
                            
                elif H_humuidity[0] == result[x]:
                    self.H_humuidity = line[15:20]
                    textbox=CTkTextbox(self.root, font=("Arial",30,"bold"),fg_color=("#dbdbdb","#2b2b2b"),width=1000,height=150,bg_color=("#dbdbdb","#2b2b2b"),border_width=0)
                    textbox.place(x=270,y=270)
                    learn= f"Accroding to the current status Hydrogen Humuidity now is {self.humuidity_H}%"
                    textbox.insert(END,learn)
                    return 
                
                elif Soler_panel[0] == result[x]:
                    sunrise = Data().sunrise_1
                    sunset = Data().sunset_1
                    temperature = Data().current
                    electricity = Data.Solar_Panel_Elec(self=self,sunrise=sunrise,sunset=sunset,temperature=temperature)
                    textbox=CTkTextbox(self.root, font=("Arial",30,"bold"),fg_color=("#dbdbdb","#2b2b2b"),width=1000,height=150,bg_color=("#dbdbdb","#2b2b2b"),border_width=0)
                    textbox.place(x=270,y=270)
                    learn= f"Accroding to the current temperature, Electricity production will be                                           {electricity} kilowatts"
                    textbox.insert(END,learn)
                    return
                   
                elif close[0] == result[x]:
                    self.search_entry.delete(0,END)
                    textbox=CTkTextbox(self.root, font=("Arial",30,"bold"),fg_color=("#dbdbdb","#2b2b2b"),width=1000,height=150,bg_color=("#dbdbdb","#2b2b2b"),border_width=0)
                    textbox.place(x=270,y=270)
                    textbox.delete("0.0",END)   
                    return 
                
                
    def Monitor (self):
        from Second_interface import Weather
        self.root.withdraw()
        self.eather = Weather(self)
        
    def Database (self):
        from Third_interface import Database
        self.root.withdraw()
        self.eather = Database(self)
    
    def Settings(self):
        from fourth_interface import Setting
        self.root.withdraw()
        self.eather = Setting(self)
    
    def Refresh(self):
        self.search_entry.delete(0,END)
        textbox=CTkTextbox(self.root, font=("Arial",30,"bold"),fg_color=("#dbdbdb","#2b2b2b"),width=1000,height=150,bg_color=("#dbdbdb","#2b2b2b"),border_width=0)
        textbox.place(x=270,y=270)
        learn= ""
        textbox.insert(END,learn)
    
    
        
    def Exit_func(self):
            self.ques =  messagebox.askyesno("EXIT","Do You Really Want to Exit?")
            if self.ques == 1:
                root.destroy()
                sys.exit()
            else: 
                return

    
# if __name__ == "__main__":
root = CTk()
ob = Into(root)
root.mainloop()           