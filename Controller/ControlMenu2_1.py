from tkinter import *
from View.Menu2 import Menu2
from Model.funcionesGui import showBestRecipes
from Model.List import list


class ControlMenu2_1:
    def __init__(self, model, view, wd, other_control, items_selected):
        self.model = model
        self.view = view
        self.wd = wd
        self.other_control = other_control
        self.items_selected = items_selected

    def back_to_Menu2(self):
        self.other_control.view = None
        self.other_control.items_selected = list()
        self.wd.switch_frame(Menu2,self.other_control)

    def show_recipes(self):
        self.view.label2.config(text=showBestRecipes(self.items_selected))