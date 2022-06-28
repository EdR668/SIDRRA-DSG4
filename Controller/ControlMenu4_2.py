from tkinter import *
from View.Menu4 import Menu4

class ControlMenu4_2:
    def __init__(self, model, view, wd, other_control):
        self.model = model
        self.view = view
        self.wd = wd
        self.other_control = other_control

    def back_to_Menu4(self):
        self.other_control.view = None
        self.wd.switch_frame(Menu4,self.other_control)