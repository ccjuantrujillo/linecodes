from pyfirmata import Arduino,util
import paho.mqtt.client as mqtt
import time
import sys

#Definimos las variables
placa = Arduino("COM6")
rele1=13;
rele2=12;
rele3=11;
rele4=10;
topic="undefined"
valor=1

#Definimos las funciones
def on_connect(client,userdata,flags,rc):
    print("Conectado - codigo de resultado:" +str(rc))

def on_message(client,userdata,msg):
    #print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    global topic
    global valor
    topic = msg.topic
    valor=int(msg.payload)

def on_publish(client,obj,mid):
    print("mid: " + str(mid))

def on_subscribe(client,obj,mid,granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client,obj,level,string):
    print(string)

client = mqtt.Client()
client.on_message = on_message
client.on_connect = on_connect
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.username_pw_set('xrxavxlq', 'hrZH1Htfj73s')

#Conectamos con el servidor
try:
    client.connect("m10.cloudmqtt.com",11129,60)
except:
    print("No se pudo conectar con el MQTT Broker...")
    print("Cerrando...")
    sys.exit()

print("Inicio")
placa.digital[rele1].write(valor)
placa.digital[rele2].write(valor)
placa.digital[rele3].write(valor)
placa.digital[rele4].write(valor)
client.subscribe("sala")
client.subscribe("dormitorio")
client.subscribe("patio")
client.subscribe("calle")

while True:
    rc = client.loop()
    if(topic=="sala"):
        placa.digital[rele1].write(valor)
    elif(topic=="dormitorio"):
        placa.digital[rele2].write(valor)
    elif(topic=="patio"):
        placa.digital[rele3].write(valor)
    elif(topic=="calle"):
        placa.digital[rele4].write(valor)
    time.sleep(0.5)
    topic=""
print("Fin")