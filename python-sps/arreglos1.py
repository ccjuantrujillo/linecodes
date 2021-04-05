import numpy as np

x = np.array([2,1,0,-1,-2])
y = np.array([0,1,2,1,0])

#Transpuesta de una matriz
m = np.array([x.tolist(),y.tolist()])
m = np.transpose(m)

#Coordenadas polares
r  = np.sqrt(np.power(x,2) + np.power(y,2))
th = np.arctan2(y, x) * 180 / np.pi
print(r,th)