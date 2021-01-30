from Tkinter import *
import math

num = float(raw_input('Ingrese un numero'))

print num**2

ventana = Tk()
W=800
H=600
cv=Canvas(ventana,width=W,height=H,bg="white")
cv.pack()

cv.create_line(0,H/2,W,H/2)
cv.create_line(W/2,0,W/2,H)
ho=0; vo=0

x = -2*math.pi

while x <=2*math.pi:
    y = math.sin(x) 
    h = (W*(x+2*math.pi)/(4*math.pi))
    v = H-(H*(y+1)/2)
    cv.create_line(ho,vo,h,v)
    ho=h
    vo=v
    x=x+0.1
    
ventana.mainloop()