from PIL import Image,ImageDraw
import matplotlib.pyplot as plt
from numpy.fft import *
from numpy import *

im = Image.open("kodak-00.png")
im.size = (768,512)
im.info = {'gamma':0.45455000000000001,'source':'Kodak PCD0992'}
im.mode = 'RGB'
im.format = 'PNG'
im.filename = 'kodad-00.png'
im.getbands = ('R','G','B')
im.show()
