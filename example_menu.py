from tkinter import *

root=Tk()


barraMenu=Menu(root)
root.config(menu=barraMenu,width=300, height=300)

archivoMenu=Menu(barraMenu,tearoff=0)

archivoMenu.add_command(label="Nuevo archivo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")

archivoEdicion=Menu(barraMenu,tearoff=0)

archivoEdicion.add_command(label="Copy")
archivoEdicion.add_command(label="Cut")
archivoEdicion.add_command(label="Paste")
archivoEdicion.add_separator()
archivoEdicion.add_command(label="Line")
archivoEdicion.add_command(label="Comment")


archivoHerramientas=Menu(barraMenu,tearoff=0)
archivoHerramientas.add_command(label="Dibujar")
archivoHerramientas.add_command(label="Poner")

archivoAyuda=Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de ..")
archivoHerramientas.add_separator()

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)



root.mainloop()