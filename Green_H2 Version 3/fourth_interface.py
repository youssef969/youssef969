from customtkinter import * 
import PIL.Image
from tkinter import messagebox
from time import strftime
from tkinter import messagebox



class Setting():
    def __init__(self,main_window):
        self.main_window = main_window
        self.root = CTkToplevel()
        self.root.state("zoomed")
        self.root.resizable(True,True)
        self.root.config(bg="#0d0d0d")
        self.root.title("Green Hydrogen")
        self.root.minsize(1550,800)
        self.root.iconbitmap(r"C:\\Users\\Computec\\Downloads\\Icons\\3-removebg-preview_1.ico")
        
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
        self.Home_button = CTkButton(self.root,text="  Home",image=self.sub_home,bg_color="#0d0d0d",hover_color="#2b2b2b",fg_color="#0d0d0d",text_color="white",compound="left",font=("Arial Black",15,"bold"),width=110,height=50,corner_radius=90,command=self.home)
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
        
        
        self.Setting = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\green_setting.png")
        self.Setting2 = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\green_setting.png")
        self.sub_Setting = CTkImage(light_image=self.Setting,size=(25,25),dark_image=self.Setting2)
        self.Setting_button = CTkButton(self.root,text="  Settings",image=self.sub_Setting,bg_color="#0d0d0d",hover_color="#2b2b2b",fg_color="#0d0d0d",text_color="#27ae60",compound="left",font=("Arial Black",15,"bold"),width=110,height=50,corner_radius=90)
        self.Setting_button.place(x=970,y=90)
        
        self.Exit = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\logout_white.png")
        self.Exit2 = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\logout_black.png")
        self.sub_Exit = CTkImage(light_image=self.Exit,size=(25,25),dark_image=self.Exit2)
        self.Exit_button = CTkButton(self.root,text="  Exit",image=self.sub_Exit,bg_color="#0d0d0d",hover_color="#2b2b2b",fg_color="#0d0d0d",text_color="white",compound="left",font=("Arial Black",15,"bold"),width=110,height=50,corner_radius=90,command=self.Exit_func)
        self.Exit_button.place(x=1140,y=90)
        
        self.date_lbl = CTkLabel(self.root,font =('Arial Black',20,'bold'),text_color='white',fg_color="#0D0D0D",bg_color="#0D0D0D")
        self.hist_lbl = CTkLabel(self.root,font =('Arial Black',20,'bold'),text_color='white',fg_color="#0D0D0D",bg_color="#0D0D0D")
        
        # ====================================================== Settings Buttons ==================================
        mode_label = CTkLabel(self.root,text="General Settings",text_color="white",fg_color="#4a4a4a",corner_radius=30,font=("Areil Black",30,"bold"),bg_color=("#dbdbdb","#2b2b2b"))
        mode_label.place(relx=0.5,anchor=CENTER,y=200)
        progreebar = CTkProgressBar(self.root,width=300,progress_color="#27ae60")
        
        progreebar.configure(mode="indeterminate")
        progreebar.start()
        progreebar.place(relx=0.5,anchor=CENTER,y=250)
        
        progreebar2 = CTkProgressBar(self.root,width=300,progress_color="#27ae60")
        progreebar2.configure(mode="indeterminate")
        progreebar2.start()
        
        progreebar2.place(relx=0.5,anchor=CENTER,y=780)
        
        mode_label = CTkLabel(self.root,text="Mode :",text_color="white",fg_color="#4a4a4a",corner_radius=30,font=("Areil Black",30,"bold"),bg_color=("#dbdbdb","#2b2b2b"))
        mode_label.place(x=600,y=700)
        
        self.seg_button = CTkSegmentedButton(self.root,values=("Dark","Light"),command=self.seg_btn,selected_color="#27ae60",width=180,height=40,font=("Ariel Black",25,"bold"),selected_hover_color="#106a43",)
        file = open("D:\\My Download\\Files\\Projects\\Green Hydrogen Project\\Green_H2 Version 3\\mode.txt",'r')
        self.seg_button.set(file.readlines()[0].strip())
        file.close()
        self.seg_button.place(x=790,y=696)
        
        self.line1 = CTkFrame(self.root,width=1300,height=5,fg_color=("black","White"))
        self.line1.place(relx=0.5,anchor=CENTER,y=630) 
        

        E_mail_label = CTkLabel(self.root,text="E-mail Settings",text_color="white",fg_color="#4a4a4a",corner_radius=30,font=("Areil Black",30,"bold"),bg_color=("#dbdbdb","#2b2b2b"))
        E_mail_label.place(x=1090,y=300)
        
        phone_label = CTkLabel(self.root,text="Phone Number Settings",text_color="white",fg_color="#4a4a4a",corner_radius=30,font=("Areil Black",30,"bold"),bg_color=("#dbdbdb","#2b2b2b"))
        phone_label.place(x=170,y=300)
        
        self.email = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\mail.png")
        self.sub_email = CTkImage(light_image=self.email,size=(20,20),dark_image=self.email)
        self.add_email_button = CTkButton(self.root,text=" Add E-mail Address",command=self.Add_email,fg_color="#27ae60",hover_color="#106a43",font=("Areil Black",15,"bold"),image=self.sub_email,compound="left",width=198,height=33)
        self.add_email_button.place(x=1300,y=450)
        
        self.phone = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\phone cell.png")
        self.sub_phone = CTkImage(light_image=self.phone,size=(25,25),dark_image=self.phone)
        self.add_Number_button = CTkButton(self.root,text=" Add Phone Number",fg_color="#27ae60",hover_color="#106a43",command=self.Add_numbers,font=("Areil Black",15,"bold"),image=self.sub_phone,compound="left",width=140)
        self.add_Number_button.place(x=425,y=450)
        
        self.delete_phone = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\delete-phone.png")
        self.sub_delete_phone = CTkImage(light_image=self.delete_phone,size=(25,25),dark_image=self.delete_phone)
        self.delete_number_button = CTkButton(self.root,text=" Delete Phone Number",fg_color="#ff0000",hover_color="#c70000",command=self.delete_number,font=("Areil Black",15,"bold"),image=self.sub_delete_phone,compound="left",width=130)
        self.delete_number_button.place(x=425,y=500)
        
        self.delete_email_photo = PIL.Image.open(r"C:\\Users\\Computec\\Downloads\\PNG Icons\\junk.png")
        self.sub_delete_email_photo = CTkImage(light_image=self.delete_email_photo,size=(22,22),dark_image=self.delete_email_photo)
        self.delete_e_mail = CTkButton(self.root,text=" Delete E-mail",fg_color="#ff0000",hover_color="#c70000",command=self.delete_email,font=("Areil Black",15,"bold"),image=self.sub_delete_email_photo,compound="left",width=198,height=33)
        self.delete_e_mail.place(x=1300,y=500)
        # ================================================= frame ===============================================
        
        self.history()
        self.time()
        self.change_mode()
        self.Show_numbers()
        self.Show_emails()
        self.diasabled_button()
        
    def Show_emails(self):
        font = CTkFont("Pacifico",size=22,weight="bold",slant="italic")
        file = open("D:\\My Download\\Files\\Projects\\Green Hydrogen Project\\Green_H2 Version 3\\numbersandemails.txt", "r+") 
        row = file.readlines()
        start = row.index("\n",2)
        numbers = row[start+1:]
        self.numbers_frame = CTkScrollableFrame(self.root,fg_color="#27ae60",width=300)
        self.numbers_frame.place(x=900,y=350)
        self.numbers_frame.grid_rowconfigure(0,weight=1)
        self.numbers_frame.grid_columnconfigure(0, weight=1)
        
        # =============================================== E-mail frame label ==========================================
        phonenumber_label_frame = CTkFrame(self.numbers_frame,fg_color="#106a43")
        phonenumber_label_frame.grid(row=0,column=0,sticky="nswe",padx=40)
        label = CTkLabel(phonenumber_label_frame,text="E-mails",font=font ,text_color="White")
        label.grid(row=0,column=0,sticky="nswe",padx=70)    
        line = CTkFrame(phonenumber_label_frame,fg_color="white",height=4,width=100)
        line.grid(row=1,column=0)
        
        # ============================================== E-mails ================================================
        for i in range(len(numbers)):
            number_frame = CTkFrame(self.numbers_frame,fg_color="#106a43")
            number_frame.grid(row=i+1,column=0,sticky="nswe",pady=15)
            number_frame.grid_columnconfigure(0,weight=1)
            number_label = CTkLabel(number_frame,text=f"{numbers[i].strip()}",font=("Areil Black",18,"bold"),text_color="White")
            number_label.grid(column=0,row=i,sticky="nswe",pady=15)
        file.close()
    
    def Show_numbers(self):
        font = CTkFont("Pacifico",size=22,weight="bold",slant="italic")
        file = open("D:\\My Download\\Files\\Projects\\Green Hydrogen Project\\Green_H2 Version 3\\numbersandemails.txt", "r+") 
        row = file.readlines()
        start = row.index("\n")
        end = row.index("**********************\n")
        numbers = row[start+1:end]
        self.numbers_frame = CTkScrollableFrame(self.root,fg_color="#27ae60",width=300)
        self.numbers_frame.place(x=25,y=350)
        self.numbers_frame.grid_rowconfigure(0,weight=1)
        self.numbers_frame.grid_columnconfigure(0, weight=1)
        
        # =============================================== phone number frame label ==========================================
        phonenumber_label_frame = CTkFrame(self.numbers_frame,fg_color="#106a43")
        phonenumber_label_frame.grid(row=0,column=0,sticky="nswe",padx=40)
        label = CTkLabel(phonenumber_label_frame,text="Phone numbers",font=font,text_color="White")
        label.grid(row=0,column=0,sticky="nswe",padx=40)    
        line = CTkFrame(phonenumber_label_frame,fg_color="white",height=4,width=150)
        line.grid(row=1,column=0)
        
        # ============================================== numbers ================================================
        for i in range(len(numbers)):
            number_frame = CTkFrame(self.numbers_frame,fg_color="#106a43")
            number_frame.grid(row=i+1,column=0,sticky="nswe",pady=15)
            number_frame.grid_columnconfigure(0,weight=1)
            number_label = CTkLabel(number_frame,text=f"+2{numbers[i].strip()}",font=("Areil Black",18,"bold"),text_color="White")
            number_label.grid(column=0,row=i,sticky="nswe",pady=15)
        file.close()
        
    def diasabled_button(self):
        file = open("D:\\My Download\\Files\\Projects\\Green Hydrogen Project\\Green_H2 Version 3\\numbersandemails.txt", "r+") 
        row = file.readlines()
        start = row.index("**********************\n")
        e_mails = row[start+2:]
        
        if e_mails == [] or e_mails == NONE:
            self.delete_e_mail.configure(state="disabled")
        
        number_start = row.index("----------------------\n")
        number_end = row.index("**********************\n")
        numbers = row[number_start+2:number_end]
        if numbers == [] or numbers == NONE:
            self.delete_number_button.configure(state="disabled")
            
            
        file.close()
        
    def delete_email(self):
        text = CTkInputDialog(title="Delete Phone Number",text="Please enter the order of the number you want to delete permanently!",font=("Ariel Black",15,"bold"),button_fg_color="#27ae60",button_hover_color="#106a43")
        index = int(text.get_input()) - 1
        file = open("D:\\My Download\\Files\\Projects\\Green Hydrogen Project\\Green_H2 Version 3\\numbersandemails.txt", "r+") 
        row = file.readlines()
        start = row.index("\n",2)
        numbers = row[start+1:]
        
        deleteed_number= numbers[index]
        numbers.pop(index)
        i=row.index(deleteed_number)
        row.pop(i)
        for i in range(len(row)):
            if row[i].strip() == "**********************":
                file = open("D:\\My Download\\Files\\Projects\\Green Hydrogen Project\\Green_H2 Version 3\\numbersandemails.txt", "w") 
                for i in range(len(row)):
                    file.write(row[i])
        messagebox.showinfo("Success",f"This E-mail Address: {deleteed_number} has been Successfully Deleted")
        
        file.close()
        self.Show_emails()
        self.diasabled_button()
        
       
    def delete_number(self):
        text = CTkInputDialog(title="Delete Phone Number",text="Please enter the order of the number you want to delete permanently!",font=("Ariel Black",15,"bold"),button_fg_color="#27ae60",button_hover_color="#106a43")
        index = int(text.get_input()) - 1
        file = open("D:\\My Download\\Files\\Projects\\Green Hydrogen Project\\Green_H2 Version 3\\numbersandemails.txt", "r+") 
        row = file.readlines()
        start = row.index("\n",1)
        end = row.index("**********************\n")
        numbers = row[start+1:end]
        deleteed_number= numbers[index]
        numbers.pop(index)
        i=row.index(deleteed_number)
        row.pop(i)
        for i in range(len(row)):
            if row[i].strip() == "**********************":
                file = open("D:\\My Download\\Files\\Projects\\Green Hydrogen Project\\Green_H2 Version 3\\numbersandemails.txt", "w") 
                for i in range(len(row)):
                    file.write(row[i])
        messagebox.showinfo("Success",f"This number: {deleteed_number} has been Successfully Deleted")
        file.close()
        self.Show_numbers()
        self.diasabled_button()
                    
      
        
    def Add_numbers (self):
        text = CTkInputDialog(title="Add Phone Number",text="Please write your Phone Number here and make Sure it is correct!",font=("Ariel Black",15,"bold"),button_fg_color="#27ae60",button_hover_color="#106a43")
        added_line = str(text.get_input())
        file = open("D:\\My Download\\Files\\Projects\\Green Hydrogen Project\\Green_H2 Version 3\\numbersandemails.txt", "r+") 
        row = file.readlines()
        
        if added_line == None or added_line == "":
            messagebox.showerror("Warning","Please Add the Phone Number, You did't Add it !")
        else:
            for i in range(len(row)):
                if row[i].strip() == "----------------------":
                    row.insert(i+1,f"\n{added_line}")
                    file = open("D:\\My Download\\Files\\Projects\\Green Hydrogen Project\\Green_H2 Version 3\\numbersandemails.txt", "w") 
                    for i in range(len(row)):
                        file.write(row[i])    
        messagebox.showinfo("Success",f"The Phone Number: {added_line} has been added successfully") 
        self.delete_number_button.configure(state="enabled")
        file.close()
        self.Show_numbers()
        
     
        
    def Add_email(self):
            text = CTkInputDialog(title="Add E-mail",text="Please write your E-mail here and make Sure it is correct!",font=("Ariel Black",15,"bold"),button_fg_color="#27ae60",button_hover_color="#106a43")
            added_line = str(text.get_input())
            file = open("D:\\My Download\\Files\\Projects\\Green Hydrogen Project\\Green_H2 Version 3\\numbersandemails.txt", "r+") 
            row = file.readlines()
            
            if added_line == None or added_line == "":
                messagebox.showerror("Warning","Please Add the E-mail Address, You did't Add it !")
            else:
                for i in range(len(row)):
                    if row[i].strip() == "**********************":
                        row.insert(i+1,f"\n{added_line}")
                        
                        file = open("D:\\My Download\\Files\\Projects\\Green Hydrogen Project\\Green_H2 Version 3\\numbersandemails.txt", "w") 
                        for i in range(len(row)):
                            file.write(row[i])   
                messagebox.showinfo("Success",f"The E-mail: {added_line} been added successfully")
                self.delete_e_mail.configure(state="enabled")   
                file.close()
                self.Show_emails()
        
    def change_mode(self):
        file = open("D:\\My Download\\Files\\Projects\\Green Hydrogen Project\\Green_H2 Version 3\\mode.txt",'r')
        self.seg_btn(file.readlines()[0].strip())
        file.close()
        
    def seg_btn(self,value):
       file = open("D:\\My Download\\Files\\Projects\\Green Hydrogen Project\\Green_H2 Version 3\\mode.txt",'w')
       file.write(value)
       if value == "Dark":                                    #self.sw.get()
            set_appearance_mode("dark") 
            self.root.config(bg="#dbdbdb")
            self.Frame.configure(bg_color="#dbdbdb")
            self.Frame2.configure(fg_color="White",bg_color="#dbdbdb")
            self.GreenH.configure(text_color="black",fg_color="#ffffff")
            self.image_label.configure(fg_color="#ffffff")
            self.Home_button.configure(fg_color="#dbdbdb",text_color="Black",bg_color="#dbdbdb",hover_color="white")
            self.Weather_button.configure(fg_color="#dbdbdb",text_color="Black",bg_color="#dbdbdb",hover_color="white")
            self.database_button.configure(fg_color="#dbdbdb",text_color="Black",bg_color="#dbdbdb",hover_color="white")
            self.refresh_button.configure(fg_color="#dbdbdb",text_color="Black",bg_color="#dbdbdb",hover_color="white")
            self.Setting_button.configure(fg_color="#dbdbdb",text_color="#27ae60",bg_color="#dbdbdb",hover_color="white")
            self.Exit_button.configure(fg_color="#dbdbdb",text_color="Black",bg_color="#dbdbdb",hover_color="white")
            self.date_lbl.configure(text_color='Black',fg_color="#dbdbdb",bg_color="#dbdbdb")
            self.hist_lbl.configure(text_color='Black',fg_color="#dbdbdb",bg_color="#dbdbdb")
       else:
            set_appearance_mode("light") 
            self.root.config(bg="#0d0d0d")
            self.Frame.configure(bg_color="#0d0d0d")
            self.Frame2.configure(fg_color="#1d1d1d",bg_color="#0d0d0d")
            self.GreenH.configure(text_color="white",fg_color="#1d1d1d")
            self.image_label.configure(fg_color="#1d1d1d")
            self.Home_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.Weather_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.database_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.refresh_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.Setting_button.configure(fg_color="#0d0d0d",text_color="#27ae60",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.Exit_button.configure(fg_color="#0d0d0d",text_color="white",bg_color="#0d0d0d",hover_color="#2b2b2b")
            self.date_lbl.configure(text_color='white',fg_color="#0D0D0D",bg_color="#0D0D0D")
            self.hist_lbl.configure(text_color='white',fg_color="#0D0D0D",bg_color="#0D0D0D")
       file.close()
    
    def home(self):
        self.root.destroy()
        self.main_window.root.deiconify()
        
    
    def Database(self):
        from Third_interface import Database
        self.root.destroy()
        self.third_window = Database(self.main_window)
        
    def Monitor(self):
        from Second_interface import Weather
        self.root.withdraw()  
        self.third_window = Weather(self.main_window)
        
        
    def Refresh(self):
        self.root.withdraw()
        self.second_window = Setting(self)
        
        
    def Exit_func(self):
            self.ques =  messagebox.askyesno("EXIT","Do You Yeally Want to Exit?")
            if self.ques == 1:
                self.root.destroy()
                sys.exit()
            else: 
                return
            
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
        
        
# root = CTk()
# ob = Setting(root)
# root.mainloop()