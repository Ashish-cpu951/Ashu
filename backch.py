from tkinter import*
a=Tk()
def red():
    a.config(bg="red")
    
def green():
    a.config(bg="green")

def blue():
    a.config(bg="blue")

def yellow():
    a.config(bg="yellow")
def pink():
    a.config(bg="pink")

a.geometry("1000x600")
a.title("color change gui")

b1=Button(a,text="red",command=red,bg="white",fg="red")
b1.grid(row=10,column=6)

b2=Button(a,text="green",command=green,bg="white",fg="green")
b2.grid(row=10,column=12)

b3=Button(a,text="blue",command=blue,bg="white",fg="blue")
b3.grid(row=10,column=18)

b4=Button(a,text="yellow",command=yellow,bg="white",fg="yellow")
b4.grid(row=10,column=24)

b4=Button(a,text="pink",command=pink,bg="white",fg="pink")
b4.grid(row=10,column=28)

a.mainloop()
