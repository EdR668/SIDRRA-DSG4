from tkinter import END, TOP
from Model.MinHeap import MinHeap
from View.Menu1 import Menu1
from Model.Instanciaciones import todosLosIngredientes
from View.FichaSede import FichaSede
from Controller.ControlFichaSede import ControlFichaSede
from Model.DB import find_sede ,sede_collection

class ControlMostrarSedes:
    def __init__(self, model, view, wd, other_control):
        self.model = model
        self.view = view
        self.wd = wd
        self.other_control = other_control

    def back_to_Menu1(self):
        self.wd.switch_frame(Menu1,self.other_control)

    def fill_alimentos(self):
        sedes = find_sede(sede_collection, {}, True)
        for item in sedes:
            ficha = FichaSede(self.view.frame4)
            control = ControlFichaSede(None, ficha, self.view.frame4, self, item)
            ficha.set_controller(control)
            ficha.pack(side=TOP)