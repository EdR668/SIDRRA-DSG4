class receta :
    pass
    def getNumeroR(self):
        return self.numeroR
    def setNumeroR(self,numeroR):
        self.numeroR= numeroR
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre= nombre
    def getPreparacion(self):
        return self.preparacion
    def setPreparacion(self,preparacion):
        self.preparacion=preparacion
    def getIngredientes(self):
        return self.ingredientes
    def setIngredientes(self,ingredientes):
        self.ingredientes=ingredientes
    def getCondimentos(self):
        return self.condimentos
    def setCondimentos(self,condimentos):
        self.condimentos=condimentos    
        
    def __init__(self,numeroR,nombre,preparacion,ingredientes,condimentos):
        self.numeroR= numeroR
        self.nombre = nombre
        self.preparacion=preparacion
        self.ingredientes=ingredientes
        self.especies=condimentos
    def toString(self):
        contador=1
        final=""
        for i in range(len(self.ingredientes)):
            if (i<len(self.ingredientes)-1):
                final+=self.ingredientes[i].getNombre()+" , "
            if (i==len(self.ingredientes)-1):
                final+=self.ingredientes[i].getNombre()
            if(len(final)>(90*contador)):
                final+="\n"
                contador+=1
        contador2=1
        final2="\nSe prepara siguiendo estos pasos: "
        for i in range(len(self.preparacion)):
            final2+=self.preparacion[i]
            if(len(final2)>(90*contador2) and self.preparacion[i]==" "):
                final2+="\n"
                contador2+=1
        
        descrip1="El nombre de esta receta es : "+self.nombre
        descrip1+="\nLos ingredientes son :"+final
        descrip1+="\nTambien vamos a usar los siguientes condimentos:"
        descrip1+=final2
        return descrip1
    