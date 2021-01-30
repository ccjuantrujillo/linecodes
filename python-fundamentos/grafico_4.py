from Tkinter import *   
  
def sel():
   selection = "You selected the option " + str(var.get())
   label2.config(text = selection)



root = Tk()
var = IntVar()

root.title('Edward Figueroa Maldonado')

frame = Frame(root)   
frame.pack()   
label2 = Label(frame, text="Hola mundo...")  
label = Label(frame, text="Hola mundo")   
c1 = Checkbutton(frame, text="Uno")   
c2 = Checkbutton(frame, text="Dos")   
entry = Entry(frame)   
button = Button(frame, text="Aceptar",bg='red')
R1 = Radiobutton(root, text="Opcion 1", variable=var, value=1,command=sel)
R2 = Radiobutton(root, text="Opcion 2", variable=var, value=2,command=sel)
R3 = Radiobutton(root, text="Opcion 3", variable=var, value=3,command=sel)
listbox = Listbox(frame)
variable = StringVar(root)
variable.set("one")
w = OptionMenu(root, variable, "one", "two", "three")


label.pack()   
label2.pack()
c1.pack()   
c2.pack()   
entry.pack()   
button.pack()   
listbox.pack()
R1.pack( anchor = W )
R2.pack( anchor = W )
R3.pack( anchor = W )


listbox.insert(END, "a list entry")
    
for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

w.pack()

root.mainloop() 