#Respuesta de frecuencia
from scipy import signal
import matplotlib.pyplot as plt

sys2 = signal.lti([1,2],[1,6,25])
w,H = signal.freqresp(sys2)
fig,(ax1,ax2) = plt.subplots(1,2,figsize=(8,4))
ax1.plot(H.real,H.imag)
ax1.plot(H.real,-H.imag)
plt.grid(True)
ax2.plot(sys2.zeros.real,sys2.zeros.imag,'o')
ax2.plot(sys2.poles.real,sys2.poles.imag,'x')
plt.grid(True)
plt.show()