from tkinter import *

def km_to_miles():
    print(e1_value.get()) 
    miles=float(e1_value.get())*1.6
    t1.insert(END,miles)

window=Tk()

#Input
e1_value=StringVar() #objeto que almacena la entrada dek usuario
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=0)

#btn
b1=Button(window,text="Add",command=km_to_miles)
b1.grid(row=0,column=2)

#text area
t1=Text(window,height=5,width=20)
t1.grid(row=1,column=0,)


window.mainloop() #esta instruccion siempre tiene que estar al final del codigo
