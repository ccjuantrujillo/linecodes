import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi,np.pi,21)
y = np.sin(x)

plt.ylabel("amplitude")
plt.xlabel("time")
plt.plot(x,y)
plt.show()

