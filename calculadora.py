from tkinter import *
root = Tk()
miFrame=Frame(root)
miFrame.pack()
operacion="" # variable global de cadena vacia
resultado=0
reset_pantalla=False

#-----------------pantalla-----------------------
numeroPantalla=StringVar()

pantala=Entry(miFrame,textvariable=numeroPantalla)
pantala.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantala.config(background="black", fg="#03f943", justify="right")
#---------------Pulsaciones de teclado--------------------

def numeroPulsado(num):
    global operacion
    global reset_pantalla
    if reset_pantalla!=False:
        numeroPantalla.set(num)
        reset_pantalla=False
    
    else:
        numeroPantalla.set(numeroPantalla.get()+num)
#-------------coma---------------------
def comaPulsada():
    numeroPantalla.set(".")
#----------------funcion suma----------------------------

def suma(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado+=float(num)
    operacion="suma"
    reset_pantalla=True
    numeroPantalla.set(resultado)
    
#----------------funcion resta----------------------------
num1=0
contador_resta=0
def resta(num):
    global operacion
    global resultado
    global reset_pantalla
    global num1
    global contador_resta
    if contador_resta==0:
        num1=float(num)
        resultado=num1
    else:
        if contador_resta==1:
            resultado=num1-float(num)
        else:
            resultado=resultado-float(num)

        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()
    contador_resta=contador_resta+1
    operacion="resta"
    reset_pantalla=True

#------------------Funcion multiplicacion-----------------------------------
contador_mult=0
def multiplica(num):
    global operacion
    global resultado
    global reset_pantalla
    global num1
    global contador_mult
    if contador_mult==0:
        num1=float(num)
        resultado=num1
    else:
        if contador_resta==1:
            resultado=num1*float(num)
        else:
            resultado=resultado*float(num)
        
        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()
    contador_mult=contador_mult+1
    operacion="multiplicacion"
    reset_pantalla=True
#---------------------Funcion division------------------------------
contador_div=0
def div(num):
    global operacion
    global resultado
    global reset_pantalla
    global num1
    global contador_div
    if contador_div==0:
        num1=float(num)
        resultado=num1
    else:
        if contador_resta==1:
            resultado=num1/float(num)
        else:
            resultado=resultado/float(num)
        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()
    contador_div=contador_div+1
    operacion="division"
    reset_pantalla=True

contador=0


#---------------------- El Resutado Total-------------------------

def elResultado():
    global operacion
    global resultado
    global reset_pantalla
    global contador_div
    global contador_mult
    global contador_resta

    if operacion=="suma":
        numeroPantalla.set(float(resultado)+float(numeroPantalla.get()))
        resultado=0
    elif operacion=="resta":
        numeroPantalla.set(float(resultado)-float(numeroPantalla.get()))
        resultado=0
        contador_resta=0
    elif operacion=="multiplicacion":
        numeroPantalla.set(float(resultado)*float(numeroPantalla.get()))
        resultado=0
        contador_mult=0
    elif operacion=="division":
        numeroPantalla.set(float(resultado)/float(numeroPantalla.get()))
        resultado=0
        contador_div=0
  
#--------------fila 1-----------------------------
boton7=Button(miFrame,text="7",width=3,command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=1)
boton7.config(background="gray", fg="#03f943", justify="right")
boton8=Button(miFrame,text="8",width=3,command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2)
boton8.config(background="gray", fg="#03f943", justify="right")
boton9=Button(miFrame,text="9",width=3,command=lambda:numeroPulsado("9"))
boton9.grid(row=2,column=3)
boton9.config(background="gray", fg="#03f943", justify="right")
botonDiv=Button(miFrame,text="/",width=3, command=lambda:div(numeroPantalla.get()))
botonDiv.grid(row=2,column=4)
botonDiv.config(background="gray", fg="#03f943", justify="right")
#--------------fila 2 (row)-----------------------------
boton4=Button(miFrame,text="4",width=3,command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=1)
boton4.config(background="gray", fg="#03f943", justify="right")
boton5=Button(miFrame,text="5",width=3,command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2)
boton5.config(background="gray", fg="#03f943", justify="right")
boton6=Button(miFrame,text="6",width=3,command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=3)
boton6.config(background="gray", fg="#03f943", justify="right")
botonMult=Button(miFrame,text="*",width=3, command=lambda:multiplica(numeroPantalla.get()))
botonMult.grid(row=3,column=4)
botonMult.config(background="gray", fg="#03f943", justify="right")
#--------------fila 3 (row)-----------------------------
boton1=Button(miFrame,text="1",width=3,command=lambda:numeroPulsado("1"))
boton1.grid(row=4,column=1)
boton1.config(background="gray", fg="#03f943", justify="right")
boton2=Button(miFrame,text="2",width=3,command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2)
boton2.config(background="gray", fg="#03f943", justify="right")
boton3=Button(miFrame,text="3",width=3,command=lambda:numeroPulsado("3"))
boton3.grid(row=4,column=3)
boton3.config(background="gray", fg="#03f943", justify="right")
botonResta=Button(miFrame,text="-",width=3,command=lambda:resta(numeroPantalla.get()))
botonResta.grid(row=4,column=4)
botonResta.config(background="gray", fg="#03f943", justify="right")
#--------------fila 4 (row)-----------------------------
boton0=Button(miFrame,text="0",width=3,command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=1)
boton0.config(background="gray", fg="#03f943", justify="right")
botonComa=Button(miFrame,text=".",width=3,command=lambda:numeroPulsado("."))
botonComa.grid(row=5,column=2)
botonComa.config(background="gray", fg="#03f943", justify="right")
botonIgual=Button(miFrame,text="=",width=3,command=lambda:elResultado())
botonIgual.grid(row=5,column=3)
botonIgual.config(background="gray", fg="#03f943", justify="right")
botonSuma=Button(miFrame,text="+",width=3,command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=5,column=4)
botonSuma.config(background="gray", fg="#03f943", justify="right")



root.mainloop()