import uuid
from datetime import datetime

class Alimento:  
    def __init__(self,cantidad,nombre,tipo,usoComun,caracteristicas,propiedadesNutricionales,imagen):
        self.id = uuid.uuid1().hex
        self.cantidad = cantidad
        self.nombre = nombre
        self.tipo = tipo
        self.usoComun=usoComun
        self.caracteristicas=caracteristicas
        self.propiedadesNutricionales=propiedadesNutricionales
        self.imagen = imagen
        self.fechaIngreso = datetime.strptime(str(datetime.today().strftime('%d/%m/%Y')),'%d/%m/%Y')

    def getId(self):
        return self.id
    def setId(self,id):
        self.id= id

    def getFechaIngreso(self):
        return self.id
    def setFechaIngreso(self,id):
        self.id= id
    
    def getCantidad(self):
        return self.cantidad
    def setCantidad(self,cantidad):
        self.cantidad= cantidad

    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre

    def getTipo(self):
        return self.tipo
    def setTipo(self,tipo):
        self.tipo=tipo

    def getUsoComun(self):
        return self.usoComun
    def setUsoComun(self,usoComun):
        self.usoComun= usoComun

    def getCaracteristicas(self):
        return self.caracteristicas
    def setCaracteristicas(self,caracteristicas):
        self.caracteristicas=caracteristicas

    def getPropiedadesNutricionales(self):
        return self.propiedadesNutricionales
    def setPropiedadesNutricionales(self,propiedadesNutricionales):
        self.propiedadesNutricionales=propiedadesNutricionales
    
    def getImagen(self):
        return self.imagen
    def setImagen(self,imagen):
        self.imagen= imagen

    def printAlimento(self):
        print(f"id: {self.id}.")
        print(f"Nombre: {self.nombre}.")
        print(f"Fecha ingreso: {self.fechaIngreso}.")
        print(f"Cantidad: {self.cantidad}.")
        print(f"Tipo: {self.tipo}.")
        print(f"Uso comun: {self.usoComun}.")
        print(f"Caracteristicas: {self.caracteristicas}.")
        print(f"Propiedades nutricionales: {self.propiedadesNutricionales}.")
        print(f"Imagen: {self.imagen}.")