
class nodo():
    def __init__(self,nombre,calorias):
        self.nombre=nombre
        self.calorias=calorias
        self.siguiente=None

class ListaHash():
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.size=0
    def listaVacia(self):
        if self.primero==None:
            return True 
        else:
            return False
    def insertar(self,nombre,calorias):
        nuevo=nodo(nombre, calorias)
        if self.listaVacia():
            self.primero=self.ultimo=nuevo
        else:
            self.ultimo.siguiente=nuevo
            self.ultimo=nuevo
        self.size+=1
    def funcionHash(self,nombre):
        sumatoria=0
        for i in nombre:
            sumatoria+=(ord(i)-96)
        return sumatoria%15
    def find(self,nombre):
        temp=self.primero
        while temp:
            if temp.nombre==nombre:
                break 
            else:
                temp=temp.siguiente
        return temp
class TablaHash():
    def __init__(self):
        self.tabla=[]
        for i in range(15):
            self.tabla.append(ListaHash())
        h=ListaHash()
        
        clave=h.funcionHash("tomate")
        self.tabla[clave].insertar("tomate",18)
        
        clave=h.funcionHash("cebolla")
        self.tabla[clave].insertar("cebolla",34)        
 
        clave=h.funcionHash("papa")
        self.tabla[clave].insertar("papa",103)
        
        clave=h.funcionHash("pepino")
        self.tabla[clave].insertar("pepino",16)    
        
        clave=h.funcionHash("calabaza")
        self.tabla[clave].insertar("calabaza",45)
        
        clave=h.funcionHash("manzana")
        self.tabla[clave].insertar("manzana",52)  

        clave=h.funcionHash("zanahoria")
        self.tabla[clave].insertar("zanahoria",41)   

        clave=h.funcionHash("mandarina")
        self.tabla[clave].insertar("mandarina",53)  

        clave=h.funcionHash("aji")
        self.tabla[clave].insertar("aji",40)

        clave=h.funcionHash("apio")
        self.tabla[clave].insertar("apio",16)

        clave=h.funcionHash("cilantro")
        self.tabla[clave].insertar("cilantro",23)

        clave=h.funcionHash("maiz")
        self.tabla[clave].insertar("maiz",95)

        clave=h.funcionHash("ajo")
        self.tabla[clave].insertar("ajo",150)  

        clave=h.funcionHash("chili")
        self.tabla[clave].insertar("chili",101)

        clave=h.funcionHash("comino")
        self.tabla[clave].insertar("comino",375)

        clave=h.funcionHash("mostaza")
        self.tabla[clave].insertar("mostaza",66)    

        clave=h.funcionHash("pimienta")
        self.tabla[clave].insertar("pimienta",255)      

        clave=h.funcionHash("huevo")
        self.tabla[clave].insertar("huevo",155)

        clave=h.funcionHash("miel")
        self.tabla[clave].insertar("miel",304) 

        clave=h.funcionHash("aceitunas")
        self.tabla[clave].insertar("aceitunas",117)

        clave=h.funcionHash("queso")
        self.tabla[clave].insertar("queso",294)      

        clave=h.funcionHash("arroz")
        self.tabla[clave].insertar("arroz",130)        

        clave=h.funcionHash("azucar")
        self.tabla[clave].insertar("azucar",387)

        clave=h.funcionHash("jengibre")
        self.tabla[clave].insertar("jengibre",80)

        clave=h.funcionHash("limon")
        self.tabla[clave].insertar("limon",29)      

        clave=h.funcionHash("champiñones")
        self.tabla[clave].insertar("champiñones",22)

        clave=h.funcionHash("vinagre")
        self.tabla[clave].insertar("vinagre",18)  

        clave=h.funcionHash("avena")
        self.tabla[clave].insertar("avena",389)

        clave=h.funcionHash("pan")
        self.tabla[clave].insertar("pan",266)

        clave=h.funcionHash("frijoles")
        self.tabla[clave].insertar("frijoles",151)  

        clave=h.funcionHash("lechuga")
        self.tabla[clave].insertar("lechuga",14)

        clave=h.funcionHash("perejil")
        self.tabla[clave].insertar("perejil",36)  

        clave=h.funcionHash("pollo")
        self.tabla[clave].insertar("pollo",195)   

        clave=h.funcionHash("res")
        self.tabla[clave].insertar("res",288) 

        clave=h.funcionHash("cerdo")
        self.tabla[clave].insertar("cerdo",242) 

        clave=h.funcionHash("mariscos")
        self.tabla[clave].insertar("mariscos",108)

        clave=h.funcionHash("pato")
        self.tabla[clave].insertar("pato",132)  

        clave=h.funcionHash("salsatomate")
        self.tabla[clave].insertar("salsatomate",97)

        clave=h.funcionHash("mayonesa")
        self.tabla[clave].insertar("mayonesa",390)        

        clave=h.funcionHash("sal")
        self.tabla[clave].insertar("sal",0)
        
    def buscar(self,ingrediente):
        h=ListaHash()
        clave=h.funcionHash(ingrediente)
        cal= self.tabla[clave].find(ingrediente)
        return cal.calorias
        
                                                                                      
if __name__ == '__main__':
    a=TablaHash()
    b=a.buscar("mariscos")
    print(b)
