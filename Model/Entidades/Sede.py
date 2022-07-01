coor_cities = {"Bogotá":(238,370), "Medellin":(170,280), "Cali":(136,412), "Cartagena":(182,100), "Tunja":(285,310), "Quibdo":(123,306)}

class Sede:
    def __init__(self, id, nombre, ciudad, pais):
        self.id = id
        self.ady_list = []
        self.nombre = nombre
        self.ciudad = ciudad
        self.pais = pais
        self.inventario = []
        self.coordendas = [coor_cities[self.ciudad][0], coor_cities[self.ciudad][1]]

    def set_ady_list(self,new_ady_list):
        self.ady_list = new_ady_list
    def get_ady_list(self):
        return self.ady_list

    def set_nombre(self,new_nombre):
        self.nombre = new_nombre
    def get_nombre(self):
        return self.nombre

    def set_ciudad(self,new_ciudad):
        self.ciudad = new_ciudad
    def get_ciudad(self):
        return self.ciudad

    def set_pais(self,new_pais):
        self.pais = new_pais
    def get_pais(self):
        return self.pais

    def set_inventario(self,new_inventario):
        self.inventario = new_inventario
    def get_inventario(self):
        return self.inventario  

    def set_coordenadas(self,new_coordendas):
        self.coordendas = new_coordendas
    def get_coordenadas(self):
        return self.coordendas  
