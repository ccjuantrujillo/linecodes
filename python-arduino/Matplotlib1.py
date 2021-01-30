import matplotlib.pyplot as plt
import simplejson
import serial

lectura = []
fig,ax = plt.subplots()
ser = serial.Serial('COM3',9600)

contador = 0
eje_x = 100
while True:
    while(ser.inWaiting()==0):
        pass
    jsonResult = ser.readline().rstrip()
    jsonObject = simplejson.loads(jsonResult)
    datos = int(jsonObject["x"])
    print(datos)
    ax.clear()
    ax.set_xlim(0,eje_x)
    ax.set_ylim(0,1023)
    lectura.append(datos)
    ax.plot(lectura)
    plt.pause(.000001)
    contador = contador +1

    if(contador>eje_x):
        lectura.pop(0)
ser.close()