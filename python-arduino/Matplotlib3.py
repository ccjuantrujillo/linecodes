import serial
import simplejson
import matplotlib.pyplot as plt
from drawnow import *

values = []

plt.ion()
cnt = 0

serialArduino = serial.Serial('COM3',9600)

def plotValues():
    plt.title('Serial values from Arduino')
    plt.grid(True)
    plt.ylim(0,1050)
    plt.ylabel('Values')
    plt.plot(values,'rx-',label='values')
    plt.legend(loc='upper right')

for i in range(0,26):
    values.append(0)

while True:
    while serialArduino.inWaiting()==0:
        pass
    valueRead = serialArduino.readline()

    try:
        jsonObject = simplejson.loads(valueRead)
        valueInInt = int(jsonObject["y"])
        print(valueInInt)
        if valueInInt <= 1024:
            if valueInInt>=0:
                values.append(valueInInt)
                values.pop(0)
                drawnow(plotValues)
            else:
                print('Valor invalido, numero negativo')
        else:
            print('Valor invalido, muy largo')
    except ValueError:
        print('Invalido, no puede convertise')

