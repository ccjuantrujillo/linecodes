import numpy as np

a = np.random.randint(1,5,(10,3))
print(a)
np.savetxt("data.txt",a,delimiter="\t")