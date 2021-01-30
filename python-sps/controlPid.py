#Control PID
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def series(sys1,sys2):
    if not isinstance(sys1,signal.lti):
        sys1 = signal.lti(*sys1)
    if not isinstance(sys2,signal.lti):
        sys2 = signal.lti(*sys2)
    num = np.polymul(sys1.num,sys2.num)
    den = np.polymul(sys1.den,sys2.den)
    sys = signal.lti(num,den)
    return sys

def feedback(plant,sensor=None):
    if not isinstance(plant,signal.lti):
        plant = signal.lti(*plant)
    if sensor is None:
        sensor = signal.lti([1],[1])
    elif not isinstance(sensor,signal.lti):
        sensor = signal.lti(*sensor)
    num = np.polymul(plant.num,sensor.den)
    den = np.polyadd(np.polymul(plant.den,sensor.den),np.polymul(plant.num ,sensor.num))
    sys = signal.lti(num,den)
    return sys

m = 1200
b = 75
sys_car = signal.lti(1,[m,b])
k = 1200
sys_pc = series(([k],[1]),sys_car)
sys_prop = feedback(sys_pc)
t=np.linspace(0,60,num=200)
t,y=signal.step2(sys_prop,T=t)
plt.plot(t,y)
plt.plot([0,t[-1]],[1]*2,'k--')
plt.grid(True)
plt.xlabel("Tiempo(s)")
plt.ylabel("(m/s)")
plt.title("Control proporcional: entrada escalon (K=1200)")
plt.show()