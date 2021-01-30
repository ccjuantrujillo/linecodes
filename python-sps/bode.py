from scipy import signal
import matplotlib.pyplot as plt
k = 1
w0 = 1e3
sys1 = signal.lti([k],[1/w0,1])
w,mag,phase = signal.bode(sys1)
fig,(ax1,ax2)=plt.subplots(2,1,figsize=(6,6))
ax1.semilogx(w,mag)
ax2.semilogx(w,phase)
plt.show()