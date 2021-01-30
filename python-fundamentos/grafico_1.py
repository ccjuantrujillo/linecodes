from tkinter import *
master = Tk()

listbox = Listbox(master)
listbox.pack()
    
listbox.insert(END, "a list entry")
    
for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)
label = Label(None, text='Edward Figueroa Maldonado')
label = Label(master)
mainloop()