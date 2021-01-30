import matplotlib.pyplot as plt
import numpy as np

Fs = 150.0;
Ts = 1.0/Fs;
freq=5;
t = np.arange(0,1,Ts)
y = np.sin(2*np.pi*freq*t)

n = len(y)
k = np.arange(n)
T = n/Fs
frq = k/T
frq = frq[range(int(n/2))]
Y = np.fft.fft(y)/n
Y = Y[range(int(n/2))]

fig,myplot = plt.subplots(2,1)
myplot[0].plot(t,y)
myplot[0].set_xlabel("Time")
myplot[0].set_ylabel("Amplitude")
myplot[1].plot(frq,abs(Y),'r')
myplot[1].set_xlabel("Freq(Hz)")
myplot[1].set_ylabel("|Y(freq)|")
plt.show()