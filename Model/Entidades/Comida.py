class Comida :
    def getNumeroC(self):
        return self.getNumeroC
    def setNumeroC(self,numeroC):
        self.numeroC= numeroC
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre
    def getTiempoCaducidad(self):
        return self.tiempoCaducidad
    def setTiempoCaducidad(self,tiempoCaducidad):
        self.tiempoCaducidad= tiempoCaducidad
    def getTipo(self):
        return self.Tipo
    def setTipo(self,tipo):
        self.tipo=tipo
        
    def __init__(self,numeroC,nombre,tiempoCaducidad,tipo):
        self.numeroC= numeroC
        self.nombre = nombre
        self.tiempoCaducidad=tiempoCaducidad 
        self.tipo=tipo
        
    def toString(self):
        descrip1="El nombre de este alimento es : "+self.nombre
        descrip1+="\nTiene un tiempo de caducidad de : "+str(self.tiempoCaducidad)
        descrip1+="\nEsta clasificado como :"
        if (self.tipo==5):
            descrip1+="harinas , cereales , grano entero , pasta , arroz , legumbres:"
        if (self.tipo==4):
            descrip1+="verduras , hortalizas , frutas , aceite de oliva"
        if (self.tipo==3):
            descrip1+="lacteos , pescados , carnes magras , frutos secos , huevos "
        if (self.tipo==2):
            descrip1+="carnes rojas , procesados , embutidos "
        if (self.tipo==1):
            descrip1+="dulces , untables , snacks "
        return descrip1
    
    
    

    
    
    