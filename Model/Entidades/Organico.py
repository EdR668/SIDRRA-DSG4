from Model.Entidades.Alimento import Alimento

class Organico(Alimento):  
    def __init__(self,cant,nombre,tipo,usoComun,caracteristicas,propiedadesNutricionales,imagen,tiempoCaducidad):
        super().__init__(cant,nombre,tipo,usoComun,caracteristicas,propiedadesNutricionales,imagen)
        
        self.tiempoCaducidad = tiempoCaducidad

    def getTiempoCaducidad(self):
        return self.tiempoCaducidad
    def setTiempoCaducidad(self,tiempoCaducidad):
        self.tiempoCaducidad= tiempoCaducidad

    def printAlimento(self):
        super().printAlimento()
        print(f"Tiempo caducidad: {self.tiempoCaducidad}.")
