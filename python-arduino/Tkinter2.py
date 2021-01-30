import tkinter as tk
ventana = tk.Tk()
ventana.title('Primera ventana')
ventana.geometry('800x600')
ventana.configure(background='dark turquoise')
etiqueta1 = tk.Label(ventana,text="CCTMexico",bg="red",fg="white")
etiqueta1.pack()

etiqueta2 = tk.Label(ventana,text="les manda",bg="pink",fg="white")
etiqueta2.pack()

etiqueta3 = tk.Label(ventana,text="Muchos saludos",bg="gold",fg="black")
etiqueta3.pack()

ventana.mainloop()