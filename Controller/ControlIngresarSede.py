from tkinter import *
from tkinter import filedialog
from View.Menu1 import Menu1
from Model.Entidades.Sede import Sede
from Model.Images import save_image
from Model.DB import insert_document, sede_collection, create_sede
import uuid

class ControlIngresarSede:
    def __init__(self, model, view, wd, other_control):
        self.model = model
        self.view = view
        self.wd = wd
        self.other_control = other_control

    def back_to_Menu1(self):
        self.wd.switch_frame(Menu1,self.other_control)

    def obtain_data(self):
        nombre = self.view.var_nombre.get()
        ciudad = self.view.var_ciudad.get()
        pais = self.view.var_pais.get()

        if self.confirm(nombre, pais, ciudad):
            new_sede = Sede(uuid.uuid1().hex, nombre, ciudad, pais)
            insert_document(sede_collection, create_sede(new_sede))
            self.blank_fields()    
    
    def blank_fields(self):
        self.view.var_nombre.set("")
        self.view.var_ciudad.set("")
        self.view.var_pais.set("")

    def confirm(self, nombre, ciudad, pais):
        return nombre != "" and ciudad != "" and pais != ""