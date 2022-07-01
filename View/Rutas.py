from tkinter import *
from tkinter import ttk
from Model.Images import re_size
from PIL import Image, ImageTk

class Rutas(Frame):
    def __init__(self, inicio):
        inicio.geometry("600x900")
        super().__init__(inicio)

        top1=PhotoImage(file="Images\\Otras\\top1.png")
        back=PhotoImage(file='Images\\Botones\\botonVolver.png')
        under1=PhotoImage(file="Images\\Otras\\under1.png")
        mapa = Image.open('Images\\Fondos\\map_col.png')
        mapa=ImageTk.PhotoImage(mapa)
        
        self.place(x=0,y=0) 
        self.config(bg='white',width=600,height=900)

        self.canva1=Canvas(self,width=600,height=800,bg="white")
        self.canva1.place(x=0, y=80)
        self.canva1.create_image(0,0,image=mapa, anchor=NW)
        self.canva1.image=mapa

        self.top1_label=Label(self,image=top1)
        self.top1_label.image=top1
        self.top1_label.place(x=0,y=-15)
        
        
        self.label1=Label(self,text="A continuación se mostrara la lista de los \nalimentos en su orden de fecha de caducidad ",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
        self.label1.place(x=20,y=20)   
        
        self.buttonB=Button(self,image=back,borderwidth=0,command=self.back_to_Menu1)
        self.buttonB.image = back
        self.buttonB.place(x=440,y=20)
        
        self.under1_label=Label(self,image=under1)
        self.under1_label.image = under1
        self.under1_label.place(x=0,y=870)

        # self.create_circule(123, 306, 4)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller
        self.controller.fill_graph()
        self.place_sedes()
        self.controller.grafo.printGraph()


    def fill_alimentos(self):
        self.controller.fill_graph()

    def back_to_Menu1(self):
        self.controller.back_to_Menu1()

    def place_sedes(self):
        self.controller.place_sedes()

    # def create_circule(self, x,y,r):
    #     x0 = x-r
    #     y0 = y-r
    #     x1 = x+r
    #     y1 = y+r
    #     self.canva1.create_oval(x0,y0,x1,y1, fill="red")
