from tkinter import *
from View.Menu3 import Menu3
from Model.funcionesGui import mostrarDescripcionRecetasIngredientes
from Model.List import list

class ControlMenu3_2:
    def __init__(self, model, view, wd, other_control, items_selected):
        self.model = model
        self.view = view
        self.wd = wd
        self.other_control = other_control
        self.items_selected = items_selected

    def back_to_Menu3(self):
        self.other_control.view = None
        self.other_control.items_selected = list()
        self.wd.switch_frame(Menu3,self.other_control)

    def show_recipes_ingredients(self):
        self.view.label2.config(text=mostrarDescripcionRecetasIngredientes(self.items_selected))