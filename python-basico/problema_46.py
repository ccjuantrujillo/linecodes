from Tkinter import *

master = Tk()

w = Canvas(master)
w.pack()
w.create_line(10, 10, 200, 200)
w.create_line(10, 10, 200, 10)
w.create_line(10, 10, 10, 200)
w.create_line(200, 10, 10, 200)
w.create_line(200, 10, 200, 200)
w.create_line(10, 200, 200, 200)


mainloop()