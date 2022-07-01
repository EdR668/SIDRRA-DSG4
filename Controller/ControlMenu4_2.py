from tkinter import *
from View.Menu1 import Menu1
from Model.TablaHash import *

class ControlMenu4_2:
    def __init__(self, model, view, wd, other_control):
        self.model = model
        self.view = view
        self.wd = wd
        self.other_control = other_control
        self.contador=0
        self.listaing=["tomate","cebolla","papa","pepino","calabaza","manzana","zanahoria","mandarina","aji","apio","cilantro","maiz","ajo","chili","comino","mostaza","pimienta","huevo","miel","aceitunas","queso","arroz","azucar","jengibre","limon","champiñones","vinagre","avena","pan","frijoles","lechuga","perejil","pollo","res","cerdo","mariscos","pato","salsatomate","mayonesa","sal"]

    def back_to_Menu1(self):
        self.wd.switch_frame(Menu1,self.other_control)

    def boton(self):
        if self.view.ingrediente.get() in self.listaing:
                self.view.label6=Label(self.view,text="                                                                                                                                 ",font=("Little Comet Bubling Demo Version",12),bg="white",justify="left")
                self.view.label6.place(x=100,y=500)
                a=TablaHash()
                caloria=a.buscar(self.view.ingrediente.get())
                self.contador+=caloria
                self.view.label4=Label(self.view,text=self.contador,font=("Little Comet Bubling Demo Version",12),bg="white",justify="left")
                self.view.label4.place(x=355,y=600)
            
        else:
            self.view.label5=Label(self.view,text="Lo sentimos, este ingrediente no se encuentra en la base de datos",font=("Little Comet Bubling Demo Version",12),bg="white",justify="left")
            self.view.label5.place(x=100,y=500)
