from tkinter import *

class ControlFichaSede:
    def __init__(self, model, view, wd, other_control, sede):
        self.model = model
        self.view = view
        self.wd = wd
        self.other_control = other_control
        self.sede = sede

    def modify_ficha(self):
        self.view.l1.config(text=self.sede.nombre)
        self.view.l2.config(text=f'{str(self.sede.ciudad)}, {str(self.sede.pais)}')