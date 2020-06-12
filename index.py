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