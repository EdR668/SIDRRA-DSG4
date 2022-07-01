from tkinter import *
from View.Menu1 import Menu1
from View.Menu2_1 import Menu2_1
from View.Menu2_2 import Menu2_2
from Controller.ControlMenu2_1 import ControlMenu2_1
from Controller.ControlMenu2_2 import ControlMenu2_2
from Model.funcionesGui import prepareElementsforboxIngredientes, sayElementsSelectedIngrediente
from Model.List import list


class ControlMenu2:
    def __init__(self, model, view, wd, other_control):
        self.model = model
        self.view = view
        self.wd = wd
        self.other_control = other_control
        self.items_selected = list()

    def back_to_Menu1(self):
        self.wd.switch_frame(Menu1,self.other_control)

    def go_to_Menu2_1(self):
        self.wd.switch_frame(Menu2_1,ControlMenu2_1(None,None,self.wd,self,self.items_selected))

    def go_to_Menu2_2(self):
        self.wd.switch_frame(Menu2_2,ControlMenu2_2(None,None,self.wd,self,self.items_selected))

    def fill_food(self):
        for item in prepareElementsforboxIngredientes():
            self.view.selecion.insert(END,item)

    def select_all(self):
        for item in self.view.selecion.curselection():
            self.items_selected.queue(self.view.selecion.get(item))
        self.view.label1.config(text=(sayElementsSelectedIngrediente(self.items_selected)))

    def delete_all(self):
        for item in reversed(self.view.selecion.curselection()):
            self.items_selected.remove(self.view.selecion.get(item))        
        self.view.label1.config(text=(sayElementsSelectedIngrediente(self.items_selected)))