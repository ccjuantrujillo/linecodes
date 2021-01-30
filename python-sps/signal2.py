import matplotlib.pyplot as plt
import numpy as np
xs = np.arange(0.0,2,0.01)
ys = np.sin(2*np.pi*xs)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.plot(xs,ys)
plt.show()