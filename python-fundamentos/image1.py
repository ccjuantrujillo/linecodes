from pylab import *
from random import *
from PIL import Image,ImageDraw

def random_points(n,s=300):
    im = Image.new('L',(s,s),255)
    draw = ImageDraw.Draw(im)
    for k in range(n):
        p = randint(0,s)
        q = randint(0,s)
        draw.ellipse((p,q,p+20,q+20),fill=0)
    return im

random_points(51,400).show()

