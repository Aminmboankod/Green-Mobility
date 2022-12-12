from time import sleep
from db.crud.create import insertCRUD
from db.crud.delete import deleteCRUD
from db.crud.read import findCRUD
from db.crud.update import updateCRUD
import json
import os 
 
 ####### MÓDULO DE EJECUCIÓ PARA ADMINISTRADOR #######



def adminProgram():

    os.system("clear")

    print("------------ADMIN CRUD PROGRAM ------------")
    print("1: Insert the data of a bicycle")
    print("2: Update the data of a bicycle")
    print("3: Read data from a bicycle")
    print("4: Delete the data of a bicycle")
    print("5: Exit")
    print("-------------------------------------------")

    option = input("Type the number of the operation you want to perform: ")
    
    if option == "5":
        print("End of program")
    else:
        crudProgram(option)
    
def crudProgram(option):

    if option == "1":
        nombre = input("Escribe el nombre de la bicicleta que quieres añadir: ")
        category = input("Escribe la categoría: ")
        brand = input("Escribe la marca de la bicicleta: ")
        material = input("Escribe el material de la bicicleta. Ej. Carbon, Aluminum: ")
        frame_size = input("Escribe el tamaño de la bici (S, M, L o XL): ")
        weight = input("Escribe el peso de la bicicleta (puedes usar decimales): ")
        companyname = input("Escribe el nombre de la tienda donde se encuentra la bicicleta: ")
        imagen = input("Escribe la url de la imagen de la bici: ")
        price = input("Escribe el precio de alquiler/día de la bici: ")
        payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "document": {

            "name": nombre,
            "category": category,
            "brand": brand,
            "material": material,
            "frame_size": frame_size,
            "weight": weight,
            "company": {
                "company_name": companyname,
            },
            "image": imagen,
            "available": True,
            "price": price,
        }
        })
        insertCRUD(payload)
        print("Bike has been created"); sleep(1.5)
        
        adminProgram()

    elif option == "2":
        name = input("Type the name of the bike you want to update: ")
        updatename = input("Type the new bicycle name: ")
        payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "filter": {"name": name },
        "update": { "$set": { "name": updatename } } })
        updateCRUD(payload)
        print("The data has been updated successfully"); sleep(1.5)

        adminProgram()

    elif option == "3":
        find = input("Type the name of the bicycle you want to see: ")
        print("This is the updated bicycle data"); sleep(1.5)
        payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "filter": {"name": find}
        })
        findCRUD(payload)

        adminProgram()

    elif option == "4":
        deletename = input("Type the name of the bike you want to delete: ")
        payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "filter": {
            "name": deletename,
        }
        })
        deleteCRUD(payload)
        print("The data has been deleted from the database"); sleep(1.5)
        print("\n" + "You can view the page by clicking here https://aminmboankod.github.io/Green-Mobility/"), sleep(1.5)

        adminProgram()

    else:
        print("The entered character is not correct.")


