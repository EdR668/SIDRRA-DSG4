from Model.Entidades.Alimento import Alimento
from datetime import datetime

class Inorganico(Alimento):  
    def __init__(self,cant,nombre,tipo,usoComun,caracteristicas,propiedadesNutricionales,imagen,fechaVencimiento):
        super().__init__(cant,nombre,tipo,usoComun,caracteristicas,propiedadesNutricionales,imagen)
        
        self.fechaVencimiento = datetime.strptime(fechaVencimiento,'%d/%m/%Y')
        self.tiempoCaducidad = (self.fechaVencimiento-self.fechaIngreso).days

    def getFechaVencimiento(self):
        return self.fechaVencimiento
    def setFechaVencimiento(self,fechaVencimiento):
        self.fechaVencimiento= fechaVencimiento

    def printAlimento(self):
        super().printAlimento()
        print(f"Fecha de vencimiento: {self.fechaVencimiento}.")
        print(f"Tiempo caducidad: {self.tiempoCaducidad}.")