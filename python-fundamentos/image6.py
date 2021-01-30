from PIL import Image,ImageDraw
import matplotlib.pyplot as plt
from numpy.fft import *
from numpy import *

im = Image.open("kodak-00.png")
mode = im.mode
w,h = im.size
im1 = Image.new(mode,(4*w,h))
#im1.show()

R,G,B = im.split()
chs = [R,G,B,im]
for k in arange(4):
    imag = chs[k]
    pos = (k*w,0)
    im1.paste(imag,pos)
im1.show()

