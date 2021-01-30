from pyfirmata import Arduino,util
import time

placa = Arduino("COM6")

print("Inicio")

while True:
    placa.digital[13].write(1)
    time.sleep(1)
    placa.digital[13].write(0)
    time.sleep(1)

print("Fin")

