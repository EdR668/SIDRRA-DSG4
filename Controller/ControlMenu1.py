from tkinter import *
from View.Menu2 import Menu2
from View.Menu3 import Menu3
from View.Menu4 import Menu4
from View.Menu4_2 import Menu4_2
from View.Menu5 import Menu5
from View.IngresarAlimentos import IngresarAlimentos
from View.IngresarSede import IngresarSede
from View.Rutas import Rutas
from View.MostrarAlimentos import MostrarAlimentos
from View.MostrarSedes import MostrarSedes
from Controller.ControlIngresarAlimento import ControlIngresarAlimentos
from Controller.ControlRutas import ControlRutas
from Controller.ControlIngresarSede import ControlIngresarSede
from Controller.ControlMostrarAlimentos import ControlMostrarAlimentos
from Controller.ControlMostrarSedes import ControlMostrarSedes
from Controller.ControlMenu2 import ControlMenu2
from Controller.ControlMenu3 import ControlMenu3
from Controller.ControlMenu4 import ControlMenu4
from Controller.ControlMenu5 import ControlMenu5
from Controller.ControlMenu4_2 import ControlMenu4_2

class ControlMenu1:
    def __init__(self, model, view, wd, control=None):
        self.model = model
        self.view = view
        self.wd = wd
        self.control = control

    def go_to_Menu2(self):
        self.wd.switch_frame(Menu2,ControlMenu2(None, None,self.wd,self))
    
    def go_to_Menu3(self):
        self.wd.switch_frame(Menu3,ControlMenu3(None, None,self.wd,self))
        
    def go_to_Menu4(self):
        self.wd.switch_frame(Menu4,ControlMenu4(None, None,self.wd,self))
    
    def go_to_Menu5(self):
        self.wd.switch_frame(Menu5,ControlMenu5(None, None,self.wd,self))

    def go_to_Mostrar_menu(self):
        self.wd.switch_frame(MostrarAlimentos,ControlMostrarAlimentos(None, None,self.wd,self))

    def go_to_Mostrar_ingreso(self):
        self.wd.switch_frame(IngresarAlimentos,ControlIngresarAlimentos(None, None,self.wd,self))

    def go_to_Mostrar_ingreso_sede(self):
        self.wd.switch_frame(IngresarSede,ControlIngresarSede(None, None,self.wd,self))

    def go_to_Mostrar_sedes(self):
        self.wd.switch_frame(MostrarSedes,ControlMostrarSedes(None, None,self.wd,self))

    def go_to_ruta(self):
        self.wd.switch_frame(Rutas,ControlRutas(None, None,self.wd,self))

    def go_to_Menu4_2(self):
        self.wd.switch_frame(Menu4_2,ControlMenu4_2(None, None,self.wd,self))