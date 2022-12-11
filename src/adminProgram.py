from time import sleep
from db.crud.create import insertCRUD
from db.crud.delete import deleteCRUD
from db.crud.read import findCRUD
from db.crud.update import updateCRUD
import json
 
 ####### MÓDULO DE EJECUCIÓ PARA ADMINISTRADOR #######

def adminProgram():

    print("¿Quiere insertar una nueva bicicleta? (Si/No)")
   
    respuesta_insert = input().upper()
        
    if respuesta_insert == "SI":
        nombre = input("Escribe el nombre de la bicicleta que quieres añadir: ")
        category = input("Escribe la categoría: ")
        brand = input("Escribe la marca de la bicicleta: ")
        material = input("Escribe el material de la bicicleta. Ej. Carbon, Aluminum: ")
        frame_size = input("Escribe el tamaño de la bici (S, M, L o XL): ")
        imagen = input("Escribe la url de la imagen de la bici: ")

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
            "image": imagen,
        }
        })
        insertCRUD(payload)
        print("Se ha creado la bicicleta"); sleep(1.5)
        print("¿Quiere actualizar el nombre de la bicicleta? (Si/No)"); sleep(1.5)
        respuesta_update = input().upper()
        
        if respuesta_update == "SI":
            updatename = input("Escribe el nuevo nombre de la bicicleta: ")
            payload = json.dumps(
            {
            "collection": "bikes",
            "database": "GreenMobility",
            "dataSource": "Cluster0",
            "filter": {"name": nombre },
            "update": { "$set": { "name": updatename } } })


            updateCRUD(payload)
            print("Los datos de han actualizado correctamente"); sleep(1.5)
            print("¿Quieres ver los datos actualizados? (Si/No)"); sleep(1.5)
            respuesta_find = input().upper()

            if respuesta_find == "SI":
                print("Estos son los datos de la bicicleta actualizados"); sleep(1.5)
                payload = json.dumps(
                {
                "collection": "bikes",
                "database": "GreenMobility",
                "dataSource": "Cluster0",
                "filter": {"name": updatename}
                })
                findCRUD(payload)
                print("¿Quieres eliminar los datos de la bicicleta previamente creada? (Si/No)"); sleep(1.5)
                respuesta_delete = input().upper()

                if respuesta_delete == "SI":
                    payload = json.dumps(
                    {
                    "collection": "bikes",
                    "database": "GreenMobility",
                    "dataSource": "Cluster0",
                    "filter": {
                        "name": updatename,
                    }
                    })
                    deleteCRUD(payload)
                    if deleteCRUD() == None:
                        print("La bicicleta que intentas borrar no existe en la base de datos"); sleep(1.5)
                    else:
                        print("Los datos han sido eliminados de la base de datos"); sleep(1.5)

                else:
                    print("Fin del programa"); sleep(1.5)
            
            else:
                print("¿Quieres eliminar los datos de la bicicleta previamente creada? (Si/No)"); sleep(1.5)

                if respuesta_delete == "SI":
                    deleteCRUD()
                    if deleteCRUD() == None:
                        print("La bicicleta que intentas borrar no existe en la base de datos"); sleep(1.5)
                    else:
                        print("Los datos han sido eliminados de la base de datos"); sleep(1.5)

                else:
                    print("Gracias por confiar en GreenMobility :)"); sleep(1.5)
                    print("Puedes ver la página pulsando aquí: https://aminmboankod.github.io/Green-Mobility/ ")
        else:
            print("¿Quieres eliminar los datos de la bicicleta previamente creada? (Si/No)"); sleep(1.5)
            respuesta_delete = input().upper()

            if respuesta_delete == "SI":
                payload = json.dumps(
                {
                "collection": "bikes",
                "database": "GreenMobility",
                "dataSource": "Cluster0",
                "filter": {
                    "name": nombre,
                }
                })
                deleteCRUD(payload)
                if deleteCRUD() == None:
                    print("La bicicleta que intentas borrar no existe en la base de datos"); sleep(1.5)
                else:
                    print("Los datos han sido eliminados de la base de datos"); sleep(1.5)

            else:
                print("Fin del programa"); sleep(1.5)
    else:
        print("Gracias por confiar en GreenMobility :)"); sleep(1.5)
        print("\n" + "Puedes ver la página pulsando aquí: https://aminmboankod.github.io/Green-Mobility/ ")
    