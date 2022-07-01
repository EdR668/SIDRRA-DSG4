from tkinter import *
from View.Menu1 import Menu1
from View.Menu3_1 import Menu3_1
from View.Menu3_2 import Menu3_2
from Controller.ControlMenu3_1 import ControlMenu3_1
from Controller.ControlMenu3_2 import ControlMenu3_2
from Model.funcionesGui import prepareElementsforboxRecetas, sayElementsSelectedReceta
from Model.List import list

class ControlMenu3:
    def __init__(self, model, view, wd, other_control):
        self.model = model
        self.view = view
        self.wd = wd
        self.other_control = other_control
        self.items_selected = list()

    def fill_recipes(self):
        for item in prepareElementsforboxRecetas():
            self.view.selecion.insert(END,item)

    def select_all(self):
        for item in self.view.selecion.curselection():
            self.items_selected.queue(self.view.selecion.get(item))
        self.view.label1.config(text=(sayElementsSelectedReceta(self.items_selected)))

    def delete_all(self):
        for item in reversed(self.view.selecion.curselection()):
            self.items_selected.remove(self.view.selecion.get(item))
        self.view.label1.config(text=(sayElementsSelectedReceta(self.items_selected)))  

    def back_to_Menu1(self):
        self.wd.switch_frame(Menu1,self.other_control)

    def go_to_Menu3_1(self):
        self.wd.switch_frame(Menu3_1,ControlMenu3_1(None,None,self.wd,self,self.items_selected))

    def go_to_Menu3_2(self):
        self.wd.switch_frame(Menu3_2,ControlMenu3_2(None,None,self.wd,self,self.items_selected))