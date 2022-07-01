from tkinter import END, TOP

from zmq import ROUTER_BEHAVIOR
from Model.Grafo import Grafo
from View.Menu1 import Menu1
from Model.Instanciaciones import todosLosIngredientes
from View.FichaAlimento import FichaAlimento
from Controller.ControlFichaAlimento import ControlFichaAlimento
from Model.DB import find_sede,sede_collection

class ControlRutas:
    def __init__(self, model, view, wd, other_control):
        self.model = model
        self.view = view
        self.wd = wd
        self.other_control = other_control
        self.grafo = Grafo()
        self.data =find_sede(sede_collection,{},True)

    def fill_graph(self):
        for item in self.data:
            self.grafo.add_vert(item)
        self.draw_route(self.grafo.camino_mas_corto(0))

    def back_to_Menu1(self):
        self.wd.switch_frame(Menu1,self.other_control)

    def draw_route(self, route):
        print(route)
        for r in route:
            self.view.canva1.create_line(self.grafo.sedes[r[0]].coordendas[0],self.grafo.sedes[r[0]].coordendas[1],self.grafo.sedes[r[1]].coordendas[0], self.grafo.sedes[r[1]].coordendas[1], fill="blue", width=3)
        

    def place_sedes(self):
        for sede in self.data:
            self.create_circule(sede.coordendas[0], sede.coordendas[1], 4)

    def create_circule(self, x,y,r):
        x0 = x-r
        y0 = y-r
        x1 = x+r
        y1 = y+r
        self.view.canva1.create_oval(x0,y0,x1,y1, fill="red")