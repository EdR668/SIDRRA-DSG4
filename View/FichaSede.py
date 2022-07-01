from tkinter import *

class FichaSede(Frame):
    def __init__(self, padre):
        super().__init__(padre,bg="#E1E1E1")

        self.config(width=570,height=110,relief="sunken", bd=10)
        self.l1 = Label(self,bg="#E1E1E1", text="Nombre del alimento",font=("Little Comet Bubling Demo Version",18,"bold"))
        self.l1.place(x=25,y=5)
        self.l2 = Label(self,bg="#E1E1E1", text="365 días",font=("Little Comet Bubling Demo Version",12))
        self.l2.place(x=125,y=50)
        self.l3 = Label(self,bg="#E1E1E1", text="Ubicación:",font=("Little Comet Bubling Demo Version",12, "bold"))
        self.l3.place(x=25,y=50)

        self.pack()

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller
        self.modify_ficha()

    def modify_ficha(self):
        self.controller.modify_ficha()