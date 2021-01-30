import numpy as np
import tkinter
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

Ventana = tkinter.Tk()
Ventana.title("Sumadora")
Ventana.geometry('800x600')
Ventana.configure(background='dark turquoise')

def GRAFICO():
    x=np.arange(100)
    y=x**2
    plt.plot(x,y)
    fig.canvas.draw()

fig = plt.figure()
FIGURE = FigureCanvasTkAgg(fig,master=Ventana)
FIGURE.get_tk_widget().grid(row=0,column=0)

tkinter.Button(Ventana,text="Graficar",command=GRAFICO).grid(row=1,column=0)

Ventana.mainloop()
