import tkinter as tk

def suma():
    suma = int(entrada1.get())
    print(suma)
    return var.set(suma)

ventana = tk.Tk()
ventana.title("Sumadora")
ventana.geometry('800x600')
ventana.configure(background='dark turquoise')
var = tk.StringVar()

el = tk.Label(ventana,text="Numero1: ",bg="pink",fg="white")
el.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
entrada1 = tk.Entry(ventana)
entrada1.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

res = tk.Label(ventana,bg="plum",textvariable=var,padx=5,pady=5,width=50)
res.pack()

botonSuma = tk.Button(ventana,text="Suma",fg="blue",command=suma)
botonSuma.pack(side=tk.TOP)

ventana.mainloop()