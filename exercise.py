from tkinter import *

def convert_grams():
    grams=float(e1_value.get())*1000
    txt_grams.insert(END,grams)

    pounds=float(e1_value.get())*2.20462
    txt_pounds.insert(END,pounds)

    ounces=float(e1_value.get())*35.274
    txt_ounces.insert(END,ounces)



window=Tk()

tx1=Text(window,height=1,width=20)
tx1.insert(END,"Kg: ")
tx1.grid(column=0,row=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(column=1,row=0)

b1=Button(window,text="Calcular",command=convert_grams)
b1.grid(column=3,row=0)

# Areas de texto

# grams
txt_grams=Text(window)
txt_grams=Text(window,height=1,width=20)
txt_grams.grid(row=1,column=0)


#pounds
txt_pounds=Text(window)
txt_pounds=Text(window,height=1,width=20)
txt_pounds.grid(row=1,column=1)



#ounces
txt_ounces=Text(window)
txt_ounces=Text(window,height=1,width=20)
txt_ounces.grid(row=1,column=2)



window.mainloop()