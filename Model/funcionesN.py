from Comida import *
from Lacteos import *
from VerdurasYFtutas import *
from receta import *
from math import *
import Instanciaciones as Instanciaciones

def organizaIngredientesAlfabetico(ingredientes):
    lista=ingredientes
    n=len(lista)-1
    for i in range(n):
        for j in range(n):
            contador=0
            string1=lista[j].getNombre()
            string2=lista[j+1].getNombre()
            while (contador<=len(string1) and contador<=len(string2)):
                if contador==len(string1):
                    break
                if contador==len(string2):
                    auxiliar=lista[j+1]
                    lista[j+1]=lista[j]
                    lista[j]=auxiliar
                    break
                if (string1[contador]<string2[contador]):
                    break
                if (string1[contador]>string2[contador]):
                    auxiliar=lista[j+1]
                    lista[j+1]=lista[j]
                    lista[j]=auxiliar
                    break
                contador+=1 
        n-=1     
    return lista

def buscaReceta(ingredien,recetas):
    lista_usx=[]
    lista_recetas=[]
    for re_aux in range(len(recetas)):
        contador=0
        for in_aux in range(len(ingredien)):
            for in2_aux in range(len(recetas[re_aux].getIngredientes())):
                if(ingredien[in_aux].numeroC==recetas[re_aux].ingredientes[in2_aux].numeroC):
                    contador+=1
        lista_usx.append(contador)
    maximo=max(lista_usx)
    for number in range(len(lista_usx)):
        if(lista_usx[number]==maximo):
            lista_recetas.append(recetas[number])
    return lista_recetas

def imprimerecetas(recetas):
    for i in range(len(recetas)):
        ingredientes=""
        for x in range(len(recetas[i].getIngredientes())):
            ingredientes+=recetas[i].getIngredientes()[x].getNombre()+","
        print(recetas[i].description(ingredientes))