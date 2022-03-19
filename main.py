from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root = Tk()
root.geometry("800x800")
clockImage = ImageTk.PhotoImage(Image.open(r"P:\Python projects\Clock Timings Usa and india\clock.jpg"))

#--------------------------------------------------------

# Indian Timing labels etc
india_label = Label(root, text ="India")
india_label.place(relx = 0.2, rely = 0.05, anchor=CENTER)

india_clock = Label(root)
india_clock["image"] = clockImage
india_clock.place(relx = 0.2, rely = 0.35, anchor=CENTER)

india_time = Label(root)
india_time.place(relx = 0.2, rely = 0.65, anchor=CENTER)

# Us Timing Labels Etc

us_label = Label(root, text = "US")
us_label.place(relx = 0.6, rely = 0.05, anchor=CENTER)

us_clock = Label(root)
us_clock["image"] = clockImage
us_clock.place(relx = 0.6, rely = 0.35, anchor=CENTER)

us_time = Label(root)
us_time.place(relx = 0.6, rely = 0.65, anchor=CENTER)

#------------------------------------------------------

class India():
    def times(self):
        home = pytz.timezone('Asia/Delhi')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        india_time["text"] = "Time:" + current_time
        india_time.after(200, self.times)
        
class US():
    def times(self):
        home = pytz.timezone('US/Central')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        us_time["text"] = "Time:" + current_time
        us_time.after(200, self.times)

obj_india = India()
obj_us = US()
btn_india = Button(root, text = "Find current indian time", command = obj_india.times)
btn_india.place(relx = 0.2, rely = 0.8, anchor=CENTER)
btn_us  = Button(root, text = "Find the current US Timings", command=obj_us.times)
btn_us.place(relx = 0.6, rely = 0.8, anchor=CENTER)

root.mainloop
