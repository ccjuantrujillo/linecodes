import serial
import simplejson
import time
from drawnow import *

#Creamos una lista
datos = []
#Inicializamos python para trabajar con el puerto serial
arduinoData = serial.Serial('COM3',9600)
#Habilitamos la grafica en tiempo real
plt.ion()

#Creamos una funcion que grafique los datos
def makeFig():
    plt.ylim(15,30)
    plt.title('Medicion de la Temperatura')
    plt.grid(True)
    plt.ylabel('Temperatura')
    plt.plot(datos,'ro-',label='Temperatura')
    plt.legend(loc='upper left')

while True:
    while(arduinoData.inWaiting()==0):
        pass
    #Leemos los datos enviados por el arduino al puerto serial
    arduinoString = arduinoData.readline()
    #Convertimos el objeto json a un arreglo
    jsonObject = simplejson.loads(arduinoString)
    #Extraemos la temperatura
    temp = float(jsonObject["t"])
    #Retardo de 0.01 segundos
    time.sleep(0.01)
    #Imprimimos la temperatura en consola
    print(temp)
    #Agregamos la temperatura a la lista
    datos.append(temp)
    #Llamamos a la función makeFig para graficar la lista datos
    drawnow(makeFig)
    #Creamos un retardo de 0.0001 segundos
    plt.pause(.0001)