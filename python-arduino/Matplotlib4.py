import serial
import numpy
import simplejson
import random
import time
from drawnow import *

datos = []
#arduinoData = serial.Serial('COM3',9600)
plt.ion()
cnt = 0

def makeFig():
    plt.ylim(0,50)
    plt.title('Medicion de la Temperatura')
    plt.grid(True)
    plt.ylabel('Temperatura')
    plt.plot(datos,'ro-',label='Temperatura')
    plt.legend(loc='upper left')

while True:
    while(arduinoData.inWaiting()==0):
        pass
    #arduinoString = arduinoData.readline()
    #jsonObject = simplejson.loads(arduinoString)
    #temp = float(jsonObject["t"])
    temp = random.random
    time.sleep(0.01)
    print(temp)
    datos.append(temp)
    drawnow(makeFig)
    plt.pause(.0001)
    cnt=cnt+1

    if(cnt>50):
        datos.pop(0)



