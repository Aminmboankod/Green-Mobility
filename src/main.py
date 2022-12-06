




####### MÓDULO DE EJECUCIÓ DEL PROGRAMA PRINCIPAL #######


# Importamos todos los módulos y sus funciones
from db.QueryList import querylistcategory, querylistbrand  
from db.dataAPIaccess import dataBikes
from logic.createListcategory import listofBikesForCategory
from logic.createListBrand import listofBikesForBrand
from logic.createIndexHTML import createContentIndex
from logic.createShowBike import createShowBike
from autoGit import commit, push
from db.crud.create import insertCRUD
from db.crud.delete import deleteCRUD
from db.crud.read import findCRUD
from db.crud.update import updateCRUD
from time import sleep

if __name__=="__main__":


    # usamos datos del módulo de conexión a mongodb y los añadimos a una variable que usaremos como parámetro.
    listOfDictionaryBikes = dataBikes()  


    # Ejecutamos la fución que crea la página principal de acceso "Index.html"
    createContentIndex()

    commit("Se ha añadido la página principal") # Hacemos un commit para guardar los cambios
    push() # Los subimos al repositorio remoto


    # de una consulta que devuelve una lista de diccionarios con las categorías existentes
    # ejecuta la función que crea el contenido de la página de lista de bicis por cada categoría
    listadiccionariosGroup = querylistcategory()
    for category in listadiccionariosGroup:
        listofBikesForCategory(listOfDictionaryBikes, category['_id'])


    # de una consulta que devuelve una lista de diccionarios con las marcas existentes
    # ejecuta la función que crea el contenido de la página de lista de bicis por cada marca 
    listadiccionariosGroup = querylistbrand()
    for brand in listadiccionariosGroup:
        listofBikesForBrand(listOfDictionaryBikes, brand['_id'])

    commit("Se ha añadido las páginas con las listas de bicis") # Hacemos un commit para guardar los cambios
    push() # Los subimos al repositorio remoto

    # Ejecuta la función createShowBike para crear todas las paginas de las bicicletas
    createShowBike(listOfDictionaryBikes)

    commit("Se ha añadido la página con datos detallados de cada bici") # Hacemos un commit para guardar los cambios
    push() # Los subimos al repositorio remoto

    print("Todos las páginas han sido creadas correctamente.")


    ####### MÓDULO DE EJECUCIÓ PARA ADMINISTRADOR #######

    print("¿Quiere insertar una nueva bicicleta? (Si/No)")
    respuesta = input().capitalize

    if respuesta == "Si":
        insertCRUD()
        print("Se ha creado la bicicleta 'Prueba'"); sleep(1.5)
        print("¿Quiere actualizar los datos de la bicicleta? (Si/No)"); sleep(1.5)

        if respuesta == "Si":
            updateCRUD()
            print("Los datos de han actualizado correctamente"); sleep(1.5)
            print("¿Quieres ver los datos actualizados? (Si/No)"); sleep(1.5)

            if respuesta == "Si":
                print("Estos son los datos de la bicicleta actualizados"); sleep(1.5)
                findCRUD()
                print("¿Quieres eliminar los datos de la bicicleta previamente creada? (Si/No)"); sleep(1.5)

                if respuesta == "Si":
                    deleteCRUD()
                    if deleteCRUD() == None:
                        print("La bicicleta que intentas borrar no existe en la base de datos"); sleep(1.5)
                    else:
                        print("Los datos han sido eliminados de la base de datos"); sleep(1.5)

                else:
                    print("Gracias por confiar en GreenMobility :)"); sleep(1.5)
            
            else:
                print("¿Quieres eliminar los datos de la bicicleta previamente creada? (Si/No)"); sleep(1.5)

                if respuesta == "Si":
                    deleteCRUD()
                    if deleteCRUD() == None:
                        print("La bicicleta que intentas borrar no existe en la base de datos"); sleep(1.5)
                    else:
                        print("Los datos han sido eliminados de la base de datos"); sleep(1.5)

                else:
                    print("Gracias por confiar en GreenMobility :)"); sleep(1.5)
    else:
        print("Gracias por confiar en GreenMobility :)"); sleep(1.5)
    
       

    
    