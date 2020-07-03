from tkinter import *

root=Tk()

varOpcion=IntVar()

Label(root,text="Genero: ").pack()

def imprimir():
    if varOpcion.get()==1:
        etiqueta.config(text="Has elegido masculino")
    elif varOpcion.get()==2:
        etiqueta.config(text="Has elegido femenino")
    #print(varOpcion.get())
    else:
        etiqueta.config(text="Has elegido otras opciones")
Radiobutton(root,text="Masculino",variable=varOpcion,value=1,command=imprimir).pack()
Radiobutton(root,text="Femenino",variable=varOpcion,value=2,command=imprimir).pack()
Radiobutton(root,text="Otras opciones",variable=varOpcion,value=3,command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()

root.mainloop()