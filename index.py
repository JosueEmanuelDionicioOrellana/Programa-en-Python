from tkinter import ttk
from tkinter import *

class Operaciones:
    #iniciamos la clase y le indicamos que debe de traer una ventana para poder iniciar
    def __init__(self, window):

        #valor de de ancho y alto de la ventana
        ancho = 400
        alto = 300

        self.wind = window
        self.wind.geometry(str(ancho)+'x'+str(alto))
        self.wind.columnconfigure(0, weight=1)
        self.wind.title('Examen Final de ingenieria en sistemas')

        #Creamos el contenedor de la aplicación

        frame = LabelFrame(self.wind, text = 'Examen final')
        frame.grid(row = 0, column = 0, columnspan = 10, pady = 50)

        Label(frame, text = 'Bienvenidos',font=("Times New Roman",30)).grid(row = 0,columnspan= 6)

        #nombramos la etiqueta del 1er input
        Label(frame, text = 'Nombre: ').grid(row = 1,columnspan = 3)
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1,columnspan = 6)

        #nombramos la etiqueta del 2do. input
        Label(frame, text = 'Apellido: ').grid(row = 2,columnspan = 3)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2,columnspan = 6)

        #nombramos la etiqueta del 3er input
        Label(frame, text = 'Dia: ').grid(row = 3,columnspan = 3)
        self.var3 = Entry(frame)
        self.var3.grid(row = 3, columnspan = 6)

        #nombramos la etiqueta del 4to input
        Label(frame, text = 'Mes: ').grid(row = 4,columnspan = 3)
        self.var4 = Entry(frame)
        self.var4.grid(row = 4, columnspan = 6)

        #nombramos la etiqueta del 5to. input
        Label(frame, text = 'Año: ').grid(row= 5,columnspan = 3 )
        self.var5 = Entry(frame)
        self.var5.grid(row = 5, columnspan = 6)

        #Creamos el boton para ejecutar la función
        ttk.Button(frame, text = 'Funcion 1', command = self.botton1).grid(row = 9, column = 1, sticky = W + E)
        ttk.Button(frame, text = 'Funcion 2', command = self.botton2).grid(row = 9, column = 2, sticky = W + E)
        ttk.Button(frame, text = 'Funcion 3', command = self.botton3).grid(row = 9, column = 3, sticky = W + E)
        ttk.Button(frame, text = 'Funcion 4', command = self.botton4).grid(row = 9, column = 4, sticky = W + E)
        ttk.Button(frame, text = 'Funcion 5', command = self.botton5).grid(row = 9, column = 5, sticky = W + E)

        #label donde veremos el resultado
        self.resultado = Label(self.wind, text = '', fg = 'black')
        self.resultado.grid(row = 1, column = 0, columnspan = 2, sticky = W + E)

    #primera validacion
    def validacion1(self):
        return len(self.var1.get()) != " " and len(self.var2.get()) != 0 and len(self.var3.get()) != " "

    #Segunda validacion
    def validacion2(self):
      return len(self.var3.get()) != 0 and len(self.var3.get()) != 0 and len(self.var3.get()) != 0 and len(self.var5.get()) != 0 and len(self.var3.get()) != 0

    #creamos la funcion del botton 1
    def botton1(self):
        if self.validacion2():
            dia=int(self.var3.get())
            mes=int(self.var4.get())
            año=int(self.var5.get())
            hdia= format(dia, "0x" )
            hmes= format(mes, "0x" ) 
            haño= format(año, "0x" )
            self.resultado['text'] = 'La fecha es: {}/{}/{} y  en binario es:{}/{}/{}'.format(dia,mes,año,hdia,hmes,haño)
        else:
            self.resultado['text'] = 'los campos son requeridos'

    #creamos la funcion del botton 2
    def botton2(self):
        if self.validacion2():
            dia=int(self.var3.get())
            mes=int(self.var4.get())
            año=int(self.var5.get())
            aaños= 2019 - año
            aañoss=24*(31*(aaños*12))
            mmeses=24*(31*mes)
            ddias=dia*24
            resultado= aañoss + mmeses + ddias
            self.resultado['text'] = 'Usted nacio {}/{}/{} y ha vivido {} horas'.format(dia,mes,año,resultado)
        else:
            self.resultado['text'] = 'los campos son requeridos'

    #creamos la funcion del botton 3
    def botton3(self): 
        if self.validacion1():
            nombre=str(self.var1.get())
            apellido=str(self.var2.get())
            numero_nombre=int(len(nombre))
            numero_apellido=int(len(apellido))
            sumatoria= numero_nombre + numero_apellido
            if sumatoria %2==0 :
               self.resultado['text'] = '{} {}, su nombre junto con su apellido es par'.format(nombre,apellido)
            else:
                self.resultado['text'] = '{} {}, su nombre junto con su apellido es impar'.format(nombre,apellido)
        else:
            self.resultado['text'] = 'los campos son requeridos'


#comprobamos si es el archivo principal
if __name__ == '__main__':
    #si la comprobovación de ventana principal es verdadero entonces 
    #entonces ejecutamos TK y lo guardamos en una ventana (window), que es la ventana principal de la aplicación
    window = Tk()

    # ejecutamos la clase Operaciones y llamamos la ventada dentro de la clase
    #guardamos la clase operaciones dentro de una varible para obtener los datos que pueda devolver
    ope = Operaciones(window)

    #ejecutamos o inicializamos la ventana
    window.mainloop()