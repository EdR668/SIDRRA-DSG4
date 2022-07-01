from Model.Entidades.Comida import *
class Harinas(Comida):
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
    
    def __init__(self,numeroC,nombre,tiempoCaducidad,tipo,usoComun,caracteristicas,propiedadesNutricionales):
        Comida.__init__(self,numeroC,nombre,tiempoCaducidad,tipo)
        self.usoComun=usoComun
        self.caracteristicas=caracteristicas
        self.propiedadesNutricionales=propiedadesNutricionales
        
    def toString(self):
        contador1=1
        final1="\nEste alimento se suele usar :"
        for i in range(len(self.usoComun)):
            final1+=self.usoComun[i]
            if(len(final1)>(90*contador1) and self.usoComun[i]==" "):
                final1+="\n"
                contador1+=1
        contador2=1
        final2="\nSus caracteristicas son :"
        for i in range(len(self.caracteristicas)):
            final2+=self.caracteristicas[i]
            if(len(final2)>(90*contador2) and self.caracteristicas[i]==" "):
                final2+="\n"
                contador2+=1
        contador3=1
        final3="\nSus propiedades nutricionales son :"
        for i in range(len(self.propiedadesNutricionales)):
            final3+=self.propiedadesNutricionales[i]
            if(len(final3)>(90*contador3) and self.propiedadesNutricionales[i]==" "):
                final3+="\n"
                contador3+=1
        descrip2=super().toString()
        descrip2+=final1
        descrip2+=final2
        descrip2+=final3
        return descrip2
