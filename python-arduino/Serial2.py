import serial
import simplejson
import matplotlib.pyplot as plt
from drawnow import *

ser = serial.Serial('COM3',9600)
datos = []
plt.ion()
contador = 0

def makeFig():
    plt.ylim(0,1050)
    plt.title('Medicion de un potenciometro')
    plt.grid(True)
    plt.ylabel('Temperatura')
    plt.plot(datos,'ro-',label='Temperatura')
    plt.legend(loc='upper center')

while True:
    jsonResult = ser.readline().rstrip()
    try:
        jsonObject = simplejson.loads(jsonResult)
        valor = jsonObject["y"]
        datos.append(valor)
        contador = contador +1
        print(valor)
        drawnow(makeFig)
        plt.pause(.0001)
    except Exception:
        pass
