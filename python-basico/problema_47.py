from Tkinter import *

master = Tk()

w = Canvas(master)
w.pack()
w.create_line(50,10,50,100)
w.create_line(50,10,50,100)
w.create_line(10,50,100,50)
w.create_oval(35,35,65,65,fill='cyan')
w.create_oval(25,25,75,75)
w.create_oval(15,15,85,85)

mainloop()