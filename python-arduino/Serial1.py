import serial
import simplejson

ser = serial.Serial('COM3',9600)

while True:
    jsonResult = ser.readline().rstrip()
    try:
        jsonObject = simplejson.loads(jsonResult)
        print(jsonObject["y"])
    except Exception:
        pass



