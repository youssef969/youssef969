from tkinter import * 
from PIL import Image ,ImageTk
import threading 



gif_frames =[]
frame_delay = 0
frame_count = -1

def read_gif():
    global frame_delay
    gif_file = Image.open("C:\\Users\\Computec\\Downloads\\PNG Icons\\wired-flat-1140-error.gif") 
    for r in range(0,gif_file.n_frames):
        gif_file.seek(r)
        gif_frames.append(gif_file.copy())
    frame_delay = gif_file.info["duration"]
    play_gif()
       
def play_gif():
    global frame_count , current_frame
    if frame_count >= len(gif_frames)- 1:
        frame_count = -1
    else:
        frame_count +=1
        current_frame = ImageTk.PhotoImage(gif_frames[frame_count])
        gif_label.config(image=current_frame)
        root.after(frame_delay,play_gif)
        

# def load():
#     read_gif()
#     play_gif()
#     root.destroy()
#     from First_interface import Into      


root = Tk()
root.geometry("640x432+500+150")
root.overrideredirect(True)
#root.after(3000,load)



gif_label = Label(root)
gif_label.pack(fill=BOTH)
threading.Thread(target=read_gif).start()

root.mainloop()