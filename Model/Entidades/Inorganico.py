from Model.Entidades.Alimento import Alimento
from datetime import datetime

class Inorganico(Alimento):  
    def __init__(self,id,cant,nombre,tipo,usoComun,caracteristicas,propiedadesNutricionales,imagen,fechaVencimiento,fechaIngreso):
        super().__init__(id,cant,nombre,tipo,usoComun,caracteristicas,propiedadesNutricionales,imagen,fechaIngreso)
        
        self.fechaVencimiento = datetime.strptime(datetime.strptime(fechaVencimiento,'%Y-%m-%d').strftime("%d-%m-%Y"),"%d-%m-%Y")
        self.tiempoCaducidad = int((self.fechaVencimiento-self.fechaIngreso).days)

    def getFechaVencimiento(self):
        return self.fechaVencimiento
    def setFechaVencimiento(self,fechaVencimiento):
        self.fechaVencimiento= fechaVencimiento

    def printAlimento(self):
        super().printAlimento()
        print(f"Fecha de vencimiento: {self.fechaVencimiento}.")
        print(f"Tiempo caducidad: {self.tiempoCaducidad}.")