from time import sleep
from db.crud.create import insertCRUD
from db.crud.delete import deleteCRUD
from db.crud.read import findCRUD
from db.crud.update import updateCRUD
import json
 
 ####### MÓDULO DE EJECUCIÓ PARA ADMINISTRADOR #######

def adminProgram():

    print("------------ADMIN CRUD PROGRAM ------------")
    print("1: Insertar los datos de una bicicleta")
    print("2: Actualizar los datos de una bicicleta")
    print("3: Leer los datos de una bicicleta")
    print("4: Borrar los datos de una bicicleta")
    print("-------------------------------------------")

    opcion = input("Escribe el número de la operación que deseas realizar: ")
    crudProgram(opcion)
    
def crudProgram(opcion):

        

    if opcion == "1":
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
        print("Se ha creado la bicicleta"); sleep(1.5)
        
        adminProgram()

    elif opcion == "2":
        name = input("Escribe el nombre de la bici que quieres actualizar: ")
        updatename = input("Escribe el nuevo nombre de la bicicleta: ")
        payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "filter": {"name": name },
        "update": { "$set": { "name": updatename } } })
        updateCRUD(payload)
        print("Los datos de han actualizado correctamente"); sleep(1.5)

        adminProgram()

    elif opcion == "3":
        buscar = input("Escribe el nombre de la bicicleta que quieres ver: ")
        print("Estos son los datos de la bicicleta actualizados"); sleep(1.5)
        payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "filter": {"name": buscar}
        })
        findCRUD(payload)

        adminProgram()

    elif opcion == "4":
        deletename = input("Escribe el nombre de la bici que quieres eliminar: ")
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
        print("Los datos han sido eliminados de la base de datos"); sleep(1.5)
        print("\n" + "Puedes ver la página pulsando aquí: https://aminmboankod.github.io/Green-Mobility/ ")

        adminProgram()

    else:
        print("El carácter introducido no es correcto.")
