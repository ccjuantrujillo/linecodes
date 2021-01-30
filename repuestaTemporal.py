#Respuesta temporal
from scipy import signal
import matplotlib.pyplot as plt

m = 1200
b = 75
sys_car = signal.lti(1,[m,b])
t,y = signal.step2(sys_car)
plt.plot(t,2250*y)
plt.grid(True)
plt.xlabel("Tiempo(s)")
plt.ylabel("v(m/s)")
plt.title("Respuesta a escalon unitario",fontsize=13)
plt.text(5,7,"Hola")
plt.show()