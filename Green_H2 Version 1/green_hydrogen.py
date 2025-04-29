from tkinter import * 
from tkinter import messagebox 
import requests
from time import strftime
import datetime



root = Tk()
root.geometry("900x500+350+150")  # hight = 864   width = 1536
root.resizable(True,True)
root.config(bg="#57aeff")
root.title("Weather")
root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\weather-app.ico")

# ============================================== Variables ==================================================

City_name = StringVar()
# =============================================== Functions ==================================================
def time_now():
    date = strftime('%I:%M:%S %p')
    date_lbl.config(text = date)
    date_lbl.after(1000,time_now)
    
def history():
   hist =  strftime("%d/%m/%Y")
   hist_lbl.config(text=hist)
   hist_lbl.after(1000,history)

def Search():
    city = City_name.get()
    city_cap = city.capitalize()
    City_lbl = Label(f3,text=f"{city_cap}",font=('Arialblack',40,'bold'),fg="white",bg="#57aeff")
    City_lbl.place(x=0,y=0)
    City_name.set("")  
            
def clear():
    City_name.set("")
    
# ============================================ Frame ======================================================

f1 = Frame(root,bg="#29323b")
f1.place(x=20,y=100,width=220,height=150)

f2 = Frame(root,bg="#1f3243",width=900,height=200,highlightbackground="black")
f2.place(x=0,y=300)

f3 = Frame(root,bg="#57aeff",width=400,height=200)
f3.place(x=500,y=100)

# firstframe = Frame(f2,bg="white",width=200,height=130)
# firstframe.place(x=43,y=40)




#=============================================================== photo Image =====================================================
# ========================================= Search Bar ==============================================
# search_bar = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Copy of search.png")
# sub_search = search_bar.subsample(2,2)
# Search_label = Label(root,image=sub_search,background="#57aeff",)
# Search_label.place(x=350,y=10) #60
# Entry_city = Entry(root,bd=0,justify="center",font=("Arial",14,"bold"),bg="#1f3243",fg="White",cursor="hand2",textvariable=City_name)
# Entry_city.place(x=380,y=20,height=25,width=160) #90

# # ======================================= Search Icon =================================================
# Search_icon = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\search.png")
# sub_search_icon = Search_icon.subsample(3,3)
# Search_button = Button(root,image=sub_search_icon,bg="#1f3243",fg="white",bd=0,activebackground="#1f3243",cursor="hand2",command=Search)
# Search_button.place(x=545,y=20)   #255

# box = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\rectangle.png")
# sub_box = box.subsample(1,1)
# box_label = Label(f2,image=sub_box,bg="#1f3243")
# box_label.place(x=15,y=10)

# cloud = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\cloudy.png")
# sub_cloud = cloud.subsample(3,3)
# cloud_label = Label(root,image=sub_cloud,bg="#57aeff")
# cloud_label.place(x=300,y=80)

# box1 = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\rounded-rectangle.png")
# box1_label = Label(f2,image=box1,bg="#1f3243")
# box1_label.place(x=280,y=30)

# box2 = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\rounded-rectangle.png")
# box2_label = Label(f2,image=box2,bg="#1f3243")
# box2_label.place(x=380,y=30)

# box3 = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\rounded-rectangle.png")
# box3_label = Label(f2,image=box3,bg="#1f3243")
# box3_label.place(x=480,y=30)

# box4 = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\rounded-rectangle.png")
# box4_label = Label(f2,image=box4,bg="#1f3243")
# box4_label.place(x=580,y=30)

# box5 = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\rounded-rectangle.png")
# box5_label = Label(f2,image=box5,bg="#1f3243")
# box5_label.place(x=680,y=30)

# box6 = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\rounded-rectangle.png")
# box6_label = Label(f2,image=box6,bg="#1f3243")
# box6_label.place(x=780,y=30)


# ================================================= Labels =======================================================  
hist_lbl = Label(root,font=('calibri',20,'bold'),foreground="white",bg="#57aeff")
hist_lbl.place(x=750,y=5)
date_lbl = Label(root,font = ('calibri',20,'bold'),foreground = 'white',bg="#57aeff")
date_lbl.place(x=20,y=5)

max_temp = 37
Max_temp_lbl = Label(f1,text=f"Max Temp.             {max_temp} ℃",font=('Arialblack',10,'bold'),fg="white",bg="#29323b")
Max_temp_lbl.place(x=20,y=5)

Min_temp = 15
Min_temp_lbl = Label(f1,text=f"Min Temp.              {Min_temp} ℃",font=('Arialblack',10,'bold'),fg="white",bg="#29323b")
Min_temp_lbl.place(x=20,y=35)


humuidity = 43
humuidity_lbl = Label(f1,text=f"Humuidity               {humuidity} %",font=('Arialblack',10,'bold'),fg="white",bg="#29323b")
humuidity_lbl.place(x=20,y=65)

wind = 14
windspeed_lbl = Label(f1,text=f"Wind Speed         {wind} K\M",font=('Arialblack',10,'bold'),fg="white",bg="#29323b")
windspeed_lbl.place(x=20,y=95)

Desc = "Sunny"
Desc_lbl = Label(f1,text=f"Description           {Desc}",font=('Arialblack',10,'bold'),fg="white",bg="#29323b")
Desc_lbl.place(x=20,y=125)

# =========================================================================================================

first_day = datetime.datetime.now()
first_day_lbl = Label(f2,text=first_day.strftime("%A"))
first_day_lbl.place(x=0,y=0)

second_day = first_day + datetime.timedelta(1)
first_day_lbl = Label(f2,text=second_day.strftime("%A"))
first_day_lbl.place(x=20,y=30)

third_day = second_day + datetime.timedelta(1)
third_day_lbl = Label(f2,text=third_day.strftime("%A"))
third_day_lbl.place(x=20,y=50)

fourth_day = third_day + datetime.timedelta(1)
fourth_day_lbl = Label(f2,text=fourth_day.strftime("%A"))
fourth_day_lbl.place(x=20,y=60)

fifth_day = fourth_day + datetime.timedelta(1)
fifth_day_lbl = Label(f2,text=fifth_day.strftime("%A"))
fifth_day_lbl.place(x=20,y=70)

sixth_day = fifth_day + datetime.timedelta(1)
sixth_day_lbl = Label(f2,text=sixth_day.strftime("%A"))
sixth_day_lbl.place(x=20,y=90)

last_day = sixth_day + datetime.timedelta(1)
last_day_lbl = Label(f2,text=last_day.strftime("%A"))
last_day_lbl.place(x=20,y=110)




time_now()
history()
root.mainloop()