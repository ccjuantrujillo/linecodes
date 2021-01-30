import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

xs = np.arange(0.0,2,0.01)
ys = signal.sawtooth(2*np.pi*5*xs)

plt.xlabel("time")
plt.ylabel("amplitude")
plt.plot(xs,ys)
plt.show()