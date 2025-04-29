from tkinter import *
import sys

def load():
    root.destroy()
    from First_interface import Into
    sys.exit()

root = Tk()
root.geometry("400x250+650+250")
root.overrideredirect(True)
root.config(bg="white")
root.resizable("false","false")
root.after(3000,load)

# =================================================== Frames ================================================== 
fr1 = Frame(root,bg="#27AE60",width=250,height=6)
fr1.pack(fill=X)

fr1 = Frame(root,bg="#27AE60",width=250,height=6)
fr1.pack(fill=X,side="bottom")

fr1 = Frame(root,bg="#27AE60",width=6,height=400)
fr1.pack(fill=Y,side="left")

fr1 = Frame(root,bg="#27AE60",width=6,height=400)
fr1.pack(fill=Y,side="right")

# ================================================== Images ==================================================== 

GreenH_bg = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Rectangle 1 (4).png")
GreenH_label = Label(root,image=GreenH_bg,bg="white")
GreenH_label.place(x=12,y=50)

image = PhotoImage(file = "C:\\Users\\Computec\\Downloads\\PNG Icons\\1710162623466-removebg-preview.png")
sub = image.subsample(4,4)
image_label = Label(root,image=sub,bg="#1d1d1d")
image_label.place(x=32,y=75)  

GreenH_label = Label(text="Green Hydrogen",bg="#1d1d1d",font=("Pacifico",23,"bold"),fg="white") 
GreenH_label.place(x=135,y=85) 


root.mainloop()