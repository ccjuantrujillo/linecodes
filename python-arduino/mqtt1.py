import paho.mqtt.client as mqtt
import sys

def on_connect(client,userdata,flags,rc):
    print("Conectado - codigo de resultado:" +str(rc))

def on_message(client,userdata,msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

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

try:
    client.username_pw_set('xrxavxlq', 'hrZH1Htfj73s')
    client.connect("m10.cloudmqtt.com",11129,60)
    client.subscribe("test")
except:
    print("No se pudo conectar con el MQTT Broker...")
    print("Cerrando...")
    sys.exit()

try:
    client.loop_forever()
except KeyboardInterrupt:  # precionar Crtl + C para salir
    print("Cerrando...")