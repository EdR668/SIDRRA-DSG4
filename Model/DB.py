import pymongo as mongo
from Model.Entidades.Organico import Organico
from Model.Entidades.Inorganico import Inorganico
from Model.Entidades.Sede import Sede


client = mongo.MongoClient("mongodb+srv://Sidrra_DSG4:dsg4@cluster0.waeycp2.mongodb.net/?retryWrites=true&w=majority")
db = client['Sidrra']
organicos_colletion = db['Organicos']
inorganicos_collection = db['Inorganicos']
sede_collection = db['Sedes']

def insert_document(collection, data):
    return collection.insert_one(data)

def find_document(collection, condition, multiple=False):
    if multiple:
        return collection.find(condition)

    else:
        return collection.find_one(condition)

def delete_document(collection, condition):
    collection.delete_many(condition)

def create_alimento(foodstuff):
    my_food = alimento_document(foodstuff=foodstuff)

    if str(type(foodstuff).__name__) == "Organico": 
        my_food["tiempoCaducidad"] =  foodstuff.tiempoCaducidad
        return my_food
    else:
        my_food["tiempoCaducidad"] =  foodstuff.tiempoCaducidad
        my_food["fechaVencimiento"] =  foodstuff.fechaVencimiento
        return my_food

def find_inorganic(collection, condition, multiple):
    results = find_document(collection, condition, multiple)
    inorganic = []

    if multiple:
        for item in results:
            new_food = Inorganico(item['_id'],float(item['cantidad']),item['nombre'],item['tipo'],item['usoComun'],item['caracteristicas'],item['propiedadesNutricionales'], item['imagen'], str(item['fechaVencimiento']).split(" ")[0], item['fechaIngreso'])
            inorganic.append(new_food)
    else:
        inorganic.append(results)
        
    return inorganic

def find_organic(collection, condition, multiple):
    results = find_document(collection, condition, multiple)
    organic = []

    if multiple:
        for item in results:
            new_food = Organico(item['_id'],float(item['cantidad']),item['nombre'],item['tipo'],item['usoComun'],item['caracteristicas'],item['propiedadesNutricionales'], item['imagen'], int(item['tiempoCaducidad']), item['fechaIngreso'])
            organic.append(new_food)
    else:
        organic.append(results)
        
    return organic

def find_sede(collection, condition, multiple):
    results = find_document(collection, condition, multiple)
    sede = []

    if multiple:
        for item in results:
            new_sede = Sede(item['_id'],item['nombre'],item['ciudad'],item['pais'])
            new_sede.set_ady_list(item['ady_list'])
            new_sede.set_inventario(item['inventario'])
            new_sede.set_coordenadas(item['coordendas'])
            sede.append(new_sede)
    else:
        sede.append(results)
        
    return sede

def alimento_document(foodstuff):
    my_food = {}
    my_food["_id"] =  foodstuff.id
    my_food["cantidad"] =  foodstuff.cantidad
    my_food["nombre"] =  foodstuff.nombre
    my_food["tipo"] =  foodstuff.tipo
    my_food["usoComun"] =  foodstuff.usoComun
    my_food["caracteristicas"] =  foodstuff.caracteristicas
    my_food["propiedadesNutricionales"] =  foodstuff.propiedadesNutricionales
    my_food["imagen"] =  foodstuff.imagen
    my_food["fechaIngreso"] =  foodstuff.fechaIngreso

    return my_food

def create_sede(sede):
    my_sede = {}
    my_sede['_id'] = sede.id
    my_sede['ady_list'] = sede.ady_list
    my_sede['nombre'] = sede.nombre
    my_sede['ciudad'] = sede.ciudad
    my_sede['pais'] = sede.pais
    my_sede['inventario'] = sede.inventario
    my_sede['coordendas'] = sede.coordendas

    return my_sede