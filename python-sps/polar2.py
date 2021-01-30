import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0,2*np.pi,1000)
r = np.cos(0.7*np.pi*np.cos(theta))
fig = plt.figure()
ax = fig.add_subplot(111,projection="polar")
ax.plot(theta,r,'r')

plt.show()