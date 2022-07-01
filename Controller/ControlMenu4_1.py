from tkinter import *
from View.Menu4 import Menu4
from Model.funcionesGui import arreglaString

class ControlMenu4_1:
    def __init__(self, model, view, wd, other_control):
        self.model = model
        self.view = view
        self.wd = wd
        self.other_control = other_control

    def back_to_Menu4(self):
        self.other_control.view = None
        self.other_control.items_selected = []
        self.wd.switch_frame(Menu4,self.other_control)

    def configure_text(self):
        self.view.label3.config(text=arreglaString(self.view.string2,45))
        self.view.label4.config(text=arreglaString(self.view.string3,40))
        self.view.label5.config(text=arreglaString(self.view.string4,40))
        self.view.label6.config(text=arreglaString(self.view.string5,40))
