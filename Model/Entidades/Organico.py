from Model.Entidades.Alimento import Alimento

class Organico(Alimento):  
    def __init__(self,id,cant,nombre,tipo,usoComun,caracteristicas,propiedadesNutricionales,imagen,tiempoCaducidad,fechaIngreso):
        super().__init__(id,cant,nombre,tipo,usoComun,caracteristicas,propiedadesNutricionales,imagen,fechaIngreso)
        
        self.tiempoCaducidad = tiempoCaducidad

    def getTiempoCaducidad(self):
        return self.tiempoCaducidad
    def setTiempoCaducidad(self,tiempoCaducidad):
        self.tiempoCaducidad= tiempoCaducidad

    def printAlimento(self):
        super().printAlimento()
        print(f"Tiempo caducidad: {self.tiempoCaducidad}.")
