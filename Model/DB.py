import pymongo as mongo
from Model.Entidades.Organico import Organico


client = mongo.MongoClient("mongodb+srv://Sidrra_DSG4:dsg4@cluster0.waeycp2.mongodb.net/?retryWrites=true&w=majority")
db = client['Sidrra']
organicos_colletion = db['Organicos']
inorganicos_collection = db['Inorganicos']

def insert_alimento(collection, data):
    return collection.insert_one(create_document(data))

def find_document(collection, condition, organ=True, multiple=False):
    if multiple:
        results = collection.find(condition)
        if organ:
            return making_object(results)

    else:
        return collection.find_one(condition)

def delete_document(collection, condition):
    collection.delete_many(condition)

def create_document(foodstuff):
    my_food = alimento_document(foodstuff=foodstuff)

    if str(type(foodstuff).__name__) == "Organico": 
        my_food["tiempoCaducidad"] =  foodstuff.tiempoCaducidad
        return my_food
    else:
        my_food["tiempoCaducidad"] =  foodstuff.tiempoCaducidad
        my_food["fechaVencimiento"] =  foodstuff.fechaVencimiento
        return my_food

def making_object(results):
    organic = []
    for item in results:
        new_food = Organico(item['cantidad'],item['nombre'],item['tipo'],item['usoComun'],item['caracteristicas'],item['propiedadesNutricionales'], item['imagen'], item['tiempoCaducidad'])
        new_food.setId(item['_id'])
        new_food.setFechaIngreso(item['fechaIngreso'])
        organic.append(new_food)
    return organic



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






new_foodstuff = {"id":0, "name": "Papas"}
# print(insert_alimento(alimentos_colletion, new_foodstuff))
# print(find_document(alimentos_colletion, {}, True))
