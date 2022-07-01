from tkinter import *
from View.Menu1 import Menu1
from View.Menu4_1 import Menu4_1
from View.Menu4_2 import Menu4_2
from View.Menu4_4 import Menu4_4
from Controller.ControlMenu4_1 import ControlMenu4_1
from Controller.ControlMenu4_2 import ControlMenu4_2

from Controller.ControlMenu4_4 import ControlMenu4_4

class ControlMenu4:
    def __init__(self, model, view, wd, other_control):
        self.model = model
        self.view = view
        self.wd = wd
        self.other_control = other_control

    def back_to_Menu1(self):
        self.wd.switch_frame(Menu1,self.other_control)

    def go_to_Menu4_1(self):
        self.wd.switch_frame(Menu4_1,ControlMenu4_1(None, None,self.wd,self))
        
    def go_to_Menu4_4(self):
        self.wd.switch_frame(Menu4_4,ControlMenu4_4(None, None,self.wd,self))