import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("interpolacion_data.txt",dtype=np.double,delimiter="\t",skiprows=0)
(x,y) = np.transpose(data)

#Plot data
plt.ylabel("x")
plt.xlabel("y")
plt.plot(x,y,'ko',label='Data')
plt.legend(loc='best')
plt.show()