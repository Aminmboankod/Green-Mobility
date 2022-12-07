from time import sleep
from db.crud.create import insertCRUD
from db.crud.delete import deleteCRUD
from db.crud.read import findCRUD
from db.crud.update import updateCRUD
 
 ####### MÓDULO DE EJECUCIÓ PARA ADMINISTRADOR #######

def adminProgram():

    print("¿Quiere insertar una nueva bicicleta? (Si/No)")
   
    respuesta_insert = input().upper()
        
    if respuesta_insert == "SI":
        insertCRUD()
        print("Se ha creado la bicicleta 'Prueba'"); sleep(1.5)
        print("¿Quiere actualizar los datos de la bicicleta? (Si/No)"); sleep(1.5)
        respuesta_update = input().upper()
        
        if respuesta_update == "SI":
            updateCRUD()
            print("Los datos de han actualizado correctamente"); sleep(1.5)
            print("¿Quieres ver los datos actualizados? (Si/No)"); sleep(1.5)
            respuesta_find = input().upper()

            if respuesta_find == "SI":
                print("Estos son los datos de la bicicleta actualizados"); sleep(1.5)
                
                findCRUD()
                print("¿Quieres eliminar los datos de la bicicleta previamente creada? (Si/No)"); sleep(1.5)
                respuesta_delete = input().upper()

                if respuesta_delete == "SI":
                    deleteCRUD()
                    if deleteCRUD() == None:
                        print("La bicicleta que intentas borrar no existe en la base de datos"); sleep(1.5)
                    else:
                        print("Los datos han sido eliminados de la base de datos"); sleep(1.5)

                else:
                    print("Gracias por confiar en GreenMobility :)"); sleep(1.5)
            
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
        print("Gracias por confiar en GreenMobility :)"); sleep(1.5)
        print("\n" + "Puedes ver la página pulsando aquí: https://aminmboankod.github.io/Green-Mobility/ ")
    