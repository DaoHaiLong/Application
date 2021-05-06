from tkinter import *
from PIL import Image,ImageTk
from googletrans import Translator

# tao Tk win
root=Tk()
root.title('Google Translate')
root.geometry("700x800")
root.iconbitmap('logo.ico')

imgs = Image.open('backs.png')
render=ImageTk.PhotoImage(imgs)
img=Label(root,image=render)
img.place(x=0,y=0)

name=Label(root,text="Translator",fg="#FFFFFF",bd=0,bg="#03152D")
name.config(font=("Transformers Movie",30))
name.pack(pady=10)

box=Text(root,width=50,height=10,font=("ROBOTO",16))
box.pack(pady=20)

but_frame=Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)
def translates():
    INPUT=box.get(1.0,END)
    print(INPUT)
    tr=Translator()
    a=tr.translate(INPUT,src="vi",dest="en")
    b=a.text
    box1.insert(END,b)           #  them cau lenh vao box1
    
clear_but=Button(but_frame, text="clear text", font=("Arial", 10, 'bold'), bg='#303030', fg="#FFFFFF", command=clear)
clear_but.place(x=160,y=350)

trans_but=Button(but_frame, text="Translate", font=("Arial", 10, 'bold'), bg='#303030', fg="#FFFFFF", command=translates)
trans_but.place(x=480,y=350)

box1=Text(root,width=50,height=10,font=("ROBOTO",16))
box1.pack(pady=50)
root.mainloop()