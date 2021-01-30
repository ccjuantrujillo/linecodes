#prueba
from Tkinter import *

def quit():
    print 'Edward Figueroa Maldonado'
    import sys; sys.exit()

widget = Button(None,text='Hola evento mundo',command=quit)
widget.pack()
widget.mainloop()
