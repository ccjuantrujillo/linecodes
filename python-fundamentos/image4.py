import matplotlib.pyplot as plt
from numpy.fft import *
from numpy import *

x,y = mgrid[-2:2:100j,-2:2:100j]
#Franha
z1 = abs(x+y)<1
A1 = fftshift(fft2(z1))
S1 = log(1+abs(A1))
#Cuadrado rotado
z2 = abs(x)+abs(y)<1
A2 = fftshift(fft2(z2))
S2 = log(1+abs(A2))
#Disco de radio 1
z3 = sqrt(x**2+y**2)<1
A3 = fftshift(fft2(z3))
S3 = log(1+abs(A3))
#Disco de radio 0.25
z4 = sqrt(x**2+y**2)<0.25
A4 = fftshift(fft2(z4))
S4 = log(1+abs(A4))

plt.figure()
plt.subplot(4,2,1)
plt.imshow(z1,cmap=plt.cm.Greys)
plt.axis("off")
plt.subplot(4,2,2)
plt.imshow(S1,cmap=plt.cm.Greys)
plt.axis("off")
plt.subplot(4,2,3)
plt.imshow(z2,cmap=plt.cm.Greys)
plt.axis("off")
plt.subplot(4,2,4)
plt.imshow(S2,cmap=plt.cm.Greys)
plt.axis("off")
plt.subplot(4,2,5)
plt.imshow(z3,cmap=plt.cm.Greys)
plt.axis("off")
plt.subplot(4,2,6)
plt.imshow(S3,cmap=plt.cm.Greys)
plt.axis("off")
plt.subplot(4,2,7)
plt.imshow(z4,cmap=plt.cm.Greys)
plt.axis("off")
plt.subplot(4,2,8)
plt.imshow(S4,cmap=plt.cm.Greys)
plt.axis("off")

plt.show()
