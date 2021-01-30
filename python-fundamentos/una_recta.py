from Tkinter import *

master = Tk()

w = Canvas(master)
w.pack()
w.create_line(0, 0, 200, 200)
w.create_oval(100,100,200,200)
w.create_rectangle(100,100,600,400,fill="blue")

mainloop()
