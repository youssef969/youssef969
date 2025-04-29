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
image = PhotoImage(file = "C:\\Users\\Computec\\Downloads\\PNG Icons\\1710162623466-removebg-preview.png")
sub = image.subsample(2,2)
image_label = Label(root,image=sub,bg="white")
image_label.pack()  

GreenH_label = Label(text="Green Hydrogeen",bg="white",font=("Pacifico",18,"bold"),fg="#369f31") 
GreenH_label.pack() 
root.mainloop()