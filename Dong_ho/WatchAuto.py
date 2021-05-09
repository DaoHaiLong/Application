from tkinter import *
from tkinter.ttk import *
from time import *

root =Tk()
root.title("Digital Watch")

label=Label(root,font=("digital-7",160),background='black',foreground='white')
label.pack(anchor='center')

def clock():
    string=strftime('%H:%M:%S:%p')
    label.config(text=string)
    label.after(1000,clock)

if __name__  =="__main__":
    clock()
    root.mainloop()
    
