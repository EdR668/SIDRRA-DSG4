from tkinter import *
from View.Menu1 import Menu1
from Model.funcionesGui import arreglaString

class ControlMenu5:
    def __init__(self, model, view, wd, other_control):
        self.model = model
        self.view = view
        self.wd = wd
        self.other_control = other_control

    def configure_text(self):
        self.view.label3.config(text=arreglaString(self.view.string2,90))
        self.view.label4.config(text=arreglaString(self.view.string3,90))
        self.view.label5.config(text=arreglaString(self.view.string4,90))

    def back_to_Menu1(self):
        self.wd.switch_frame(Menu1,self.other_control)
        