from gettext import find
from tkinter import END, TOP
from Model.MinHeap import MinHeap
from View.Menu1 import Menu1
from Model.Instanciaciones import todosLosIngredientes
from View.FichaAlimento import FichaAlimento
from Controller.ControlFichaAlimento import ControlFichaAlimento
from Model.DB import find_organic,find_inorganic,organicos_colletion,inorganicos_collection

class ControlMostrarAlimentos:
    def __init__(self, model, view, wd, other_control):
        self.model = model
        self.view = view
        self.wd = wd
        self.other_control = other_control
        self.min_h =MinHeap()

    def fill_min_heap(self):
        for item in find_organic(organicos_colletion,{},True):
            self.min_h.insert(item)

        for item_inor in find_inorganic(inorganicos_collection,{},True):
            self.min_h.insert(item_inor)

    def back_to_Menu1(self):
        self.wd.switch_frame(Menu1,self.other_control)

    def fill_alimentos(self):
        self.fill_min_heap()
        iterations = self.min_h.current_size
        for item in range(iterations):
            food = self.min_h.delete_min()
            ficha = FichaAlimento(self.view.frame4)
            control = ControlFichaAlimento(None, ficha, self.view.frame4, self, food)
            ficha.set_controller(control)
            ficha.pack(side=TOP)