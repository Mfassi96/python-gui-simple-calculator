from tkinter import *
from tkinter import ttk

def operar():
    num1=int(e1_value.get())
    num2=int(e2_value.get())
    operacion=combo.get()

    if operacion=="SUMA":
        suma=num1+num2
        result.insert(END,suma)
    elif operacion=="RESTA":
                resta=num1-num2
                result.insert(END,resta)
    elif operacion=="MULTIPLICACION":
        mult=num1*num2
        result.insert(END,mult)
    elif operacion=="DIVICION":
        div=num1/num2
        result.insert(END,div)
        

    



window = Tk()
window.title("Calculadora basica Python Tkinter")
style = ttk.Style()
style.theme_use('clam')

# creando combobox
option_txt=ttk.Label(window,text="Seleccione una opcion")
option_txt.grid(row=1,column=20)
opciones = ["SUMA", "RESTA", "MULTIPLICACION", "DIVICION"]
combo = ttk.Combobox(window, values=opciones)
combo.grid(row=2, column=20)

# Usamos Label en lugar de Text para el título
titulo = ttk.Label(window, text="Simple calculadora Python Tkinter")
titulo.grid(row=0, column=20)


num_1_txt = ttk.Label(window, text="Ingrese el primer numero")
num_1_txt.grid(row=1, column=0)

e1_value=StringVar()
e1 = ttk.Entry(window,textvariable=e1_value)
e1.grid(row=2, column=0)

num_2_txt = ttk.Label(window, text="Ingrese el Segundo numero")
num_2_txt.grid(row=1, column=50)

e2_value=StringVar()
e2 = ttk.Entry(window,textvariable=e2_value)
e2.grid(row=2, column=50)

sum_btn=ttk.Button(window,text="OPERAR",command=operar)
sum_btn.grid(row=4, column=20)
result=Text(window,height=1,width=50)
result.grid(row=7,column=20)




window.mainloop()