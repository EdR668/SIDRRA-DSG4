from Comida import *
from Instanciaciones import *
from Lacteos import *
from VerdurasYFtutas import *
from receta import *
from Model.funcionesN import *

def prepareElementsforboxIngredientes():
    ingredientes=organizaIngredientesAlfabetico(todosLosIngredientes())
    listafinal=[]
    for i in range(len(ingredientes)):
        listafinal.append(ingredientes[i].getNombre())
    return listafinal

def prepareElementsforboxRecetas():
    recetas=organizaIngredientesAlfabetico(todasLasRecetas())
    listafinal=[]
    for i in range(len(recetas)):
        listafinal.append(recetas[i].getNombre())
    return listafinal

def sayElementsSelectedIngrediente(lista):
    final="Los ingredientes selecionados son : "
    if len(lista)<=10:
        contador=1
        for i in range (len(lista)):
            if (i<len(lista)-1):
                final+=lista[i]+" , "
            if (i==len(lista)-1):
                final+=lista[i]
            if(len(final)>(60*contador)):
                final+="\n"
                contador+=1
        return final
    if len(lista)>10:
        aviso="Solo se pueden elegir hasta 10 ingredientes , por favor elimine unos ingredientes \n"
        contador=1
        for i in range (10):
            if (i<len(lista)-1):
                final+=lista[i]+" , "
            if (i==len(lista)-1):
                final+=lista[i]
            if(len(final)>(60*contador)):
                final+="\n"
                contador+=1
        return (aviso+"\n"+final)
    
def sayElementsSelectedReceta(lista):
    final="Las recetas selecionados son : "
    if len(lista)<=10:
        contador=1
        for i in range (len(lista)):
            if (i<len(lista)-1):
                final+=lista[i]+" , "
            if (i==len(lista)-1):
                final+=lista[i]
            if(len(final)>(60*contador)):
                final+="\n"
                contador+=1
        return final
    if len(lista)>10:
        aviso="Solo se pueden elegir hasta 10 recetas , por favor elimine unas recetas \n"
        contador=1
        for i in range (10):
            if (i<len(lista)-1):
                final+=lista[i]+" , "
            if (i==len(lista)-1):
                final+=lista[i]
            if(len(final)>(60*contador)):
                final+="\n"
                contador+=1
        return (aviso+"\n"+final)

def showBestRecipes(lista):
    lista_aux1=todosLosIngredientes()
    lista_aux2=[]
    for i in range(len(lista_aux1)):
        for j in range(len(lista)):
            if (lista[j])==(lista_aux1[i].getNombre()):
                lista_aux2.append(lista_aux1[i])
    lista_aux3=buscaReceta(lista_aux2,todasLasRecetas())
    final=""
    contador=1
    for i in range(len(lista_aux3)):
        if i==0:
            final+=str(i+1)+" )  "
        if i>0:
            final+="\n"+str(i+1)+" )  "
        final+=lista_aux3[i].toString()
        if(len(final)>(80*contador)):
            final+="\n"
            contador+=1
    return final

def mostrarDescripcionIngredientes(lista):
    lista_aux1=todosLosIngredientes()
    lista_aux2=[]
    for i in range(len(lista_aux1)):
        for j in range(len(lista)):
            if (lista[j])==(lista_aux1[i].getNombre()):
                lista_aux2.append(lista_aux1[i])
    final=""
    contador=1
    for i in range(len(lista_aux2)):
        if i==0:
            final+=str(i+1)+" )  "
        if i>0:
            final+="\n"+str(i+1)+" )  "
        final+=lista_aux2[i].toString()
        if(len(final)>(80*contador)):
            final+="\n"
            contador+=1
    return final

def mostrarDescripcionRecetas(lista):
    lista_aux1=todasLasRecetas()
    lista_aux2=[]
    for i in range(len(lista_aux1)):
        for j in range(len(lista)):
            if (lista[j])==(lista_aux1[i].getNombre()):
                lista_aux2.append(lista_aux1[i])
    final=""
    contador=1
    for i in range(len(lista_aux2)):
        if i==0:
            final+=str(i+1)+" )  "
        if i>0:
            final+="\n"+str(i+1)+" )  "
        final+=lista_aux2[i].toString()
        if(len(final)>(80*contador)):
            final+="\n"
            contador+=1
    return final

def mostrarDescripcionRecetasIngredientes(lista):
    lista_aux1=todasLasRecetas()
    lista_aux2=[]
    lista_aux3=[]
    for i in range(len(lista_aux1)):
        for j in range(len(lista)):
            if (lista[j])==(lista_aux1[i].getNombre()):
                lista_aux2.append(lista_aux1[i])
    for i in range(len(lista_aux2)):
        for j in range(len(lista_aux2[i].getIngredientes())):
            if len(lista_aux3)<=1:
                lista_aux3.append(lista_aux2[i].getIngredientes()[j])
            if len(lista_aux3)>1:
                contador=0
                contador_aux=0
                while(contador<len(lista_aux3)-1):
                    if(lista_aux3[contador]==lista_aux2[i].getIngredientes()[j]):
                        contador_aux+=1
                        break
                    contador+=1
                if contador_aux==0:
                    lista_aux3.append(lista_aux2[i].getIngredientes()[j])
    final=""
    contador=1
    for i in range(len(lista_aux3)):
        if i==0:
            final+=str(i+1)+" )  "
        if i>0:
            final+="\n"+str(i+1)+" )  "
        final+=lista_aux3[i].toString()
        if(len(final)>(80*contador)):
            final+="\n"
            contador+=1
    return final

def arreglaString(string1,numero):
    contador1=1
    final=""
    for i in range(len(string1)):
        final+=string1[i]
        if (len(final)>numero*contador1 and string1[i]==" "):
            final+="\n"
            contador1+=1
    return final
            