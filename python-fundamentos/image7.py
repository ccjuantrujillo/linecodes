from PIL import Image,ImageDraw
from numpy.fft import *
from numpy import *
import matplotlib.pyplot as plt

im0 = Image.open('kodak-00.png')
im = im0.convert('L')
data = array(im.getdata())
print(data.shape)
print(im.size)
data.shape = im.size
print(data.shape)
w,h = data.shape
for j in arange(w):
    for k in arange(h):
        if (k+j)%10 == 0:
            data[j,k]=0
data.shape = w*h
im.putdata(data)
#im.show()

data = array(im.getdata())
data.shape = im.size
A = fftshift(fft2(data))
S = log(1+abs(A))
plt.imshow(S,cmap=plt.cm.Greys)
plt.axis("off")
plt.show()

