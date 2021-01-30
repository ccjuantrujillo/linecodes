# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))

s1 = np.cos(np.pi * t)

plt.psd(s1 ** 2, 512, 1. / dt, color="green")
plt.xlabel('Frequency')
plt.ylabel('PSD(db)')

plt.suptitle('matplotlib.pyplot.psd() function \
Example', fontweight="bold")

plt.show();