import tkinter as tk
import serial
import simplejson
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from drawnow import *
import matplotlib.pyplot as plt


datos = []
arduinoData = serial.Serial('COM3',9600,timeout=5)
plt.ion()
cnt = 0

def suma():
    suma = int(entrada1.get())
    arduinoData.write(suma)
    time.sleep(1)
    print(suma)
    return var.set(suma)

def makeFig():
    plt.ylim(0,50)
    plt.title('Medicion de la Temperatura')
    plt.grid(True)
    plt.ylabel('Temperatura')
    plt.plot(datos,'ro-',label='Temperatura')
    plt.legend(loc='upper left')
    fig.canvas.draw()

ventana = tk.Tk()
ventana.wm_title("Lectura de Temperaturas")
var = tk.StringVar()

fig = plt.figure()
canvas = FigureCanvasTkAgg(fig,master=ventana)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

el = tk.Label(ventana,text="Numero1: ",bg="pink",fg="white")
el.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)

entrada1 = tk.Entry(ventana)
entrada1.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

botonSuma = tk.Button(ventana,text="Suma",fg="blue",command=suma)
botonSuma.pack(side=tk.TOP)

while True:
    while(arduinoData.inWaiting()==0):
        pass
    arduinoString = arduinoData.readline()
    jsonObject = simplejson.loads(arduinoString)
    temp = float(jsonObject["t"])
    y = float(jsonObject["y"])
    time.sleep(0.01)
    print(temp,",",y)
    datos.append(temp)
    drawnow(makeFig)
    plt.pause(.0001)
ventana.mainloop()