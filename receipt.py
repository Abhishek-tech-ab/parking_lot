from tkinter import *
import os
import tempfile

def show():
    print("start")

def print_area(text):
    temp_file=tempfile.mktemp('.text')
    open(temp_file,'w').write(text)
    os.stat(temp_file,'print')

root=Tk()
root.title("PARKING MANAGEMENT SYSTEM ")
root.geometry('500x500')

lbl_print=Label(root,text="Paeking Payment Recipt:",font=("Elephant",20),fg="brown").place(x=100,y=20)
text_area=Text(root,bg="light yellow")
btn_print=Button(root,text="Print",font=("Ariel",18,"bold"),bg="light green",fg="brown",activebackground="yellow",command=lambda :print_area(text_area.get('1.0',END)))
btn_print.place(x=200,y=120)
root.mainloop()