
# Importamos todos los módulos y sus funciones

from db.crud.listCategory import querylistcategory
from db.crud.listBrand import querylistbrand 
from db.crud.allBikes import dataBikes
from logic.createListcategory import listofBikesForCategory
from logic.createContactHTML import createContentContact
from logic.createListBrand import listofBikesForBrand
from logic.createIndexHTML import createContentIndex
from logic.createShowBike import createShowBike
from adminProgram import adminProgram
from autoGit import commit, push

####### MÓDULO DE EJECUCIÓ DEL PROGRAMA PRINCIPAL #######

if __name__=="__main__":


    listOfDictionaryBikes = dataBikes()                                                   # Usamos datos del módulo de conexión a mongodb y los añadimos a una variable que usaremos como parámetro.

 
    createContentIndex()                                                                  # Ejecutamos la fución que crea la página principal de acceso "Index.html
    createContentContact()                                                                # Ejecutamos la fución que crea la página de contacto

    commit("Se ha añadido la página principal y la de contacto")                          # Hacemos un commit para guardar los cambios
    push()                                                                                # Los subimos al repositorio remoto

    print("\n" + "Puedes ver la página pulsando aquí: https://aminmboankod.github.io/Green-Mobility/ ")



    listadiccionariosGroup = querylistcategory()                                          # de una consulta que devuelve una lista de diccionarios con las categorías existentes         
    for category in listadiccionariosGroup:                                               # ejecuta la función que crea el contenido de la página de lista de bicis por cada categoría
        listofBikesForCategory(listOfDictionaryBikes, category['_id'])


 
    listadiccionariosGroup = querylistbrand()                                             # de una consulta que devuelve una lista de diccionarios con las marcas existentes 
    for brand in listadiccionariosGroup:                                                  # ejecuta la función que crea el contenido de la página de lista de bicis por cada marca
        listofBikesForBrand(listOfDictionaryBikes, brand['_id'])

    commit("Se ha añadido las páginas con las listas de bicis")                           
    push()                                                                                

    print("\n" + "Puedes ver la página pulsando aquí: https://aminmboankod.github.io/Green-Mobility/ ")

   
    createShowBike(listOfDictionaryBikes)                                                 # Ejecuta la función createShowBike para crear todas las paginas de las bicicletas

    commit("Se ha añadido la página con datos detallados de cada bici")                   
    push()                                                                                

    print("\n" + "Todos las páginas han sido creadas correctamente.")

    print("\n" + "Puedes ver la página pulsando aquí: https://aminmboankod.github.io/Green-Mobility/ ")

    




    ####### MÓDULO DE EJECUCIÓ PARA ADMINISTRADOR #######


    print("\n" + "¿Quieres ejecutar el programa de administrador?")
    respuesta = input().upper()

    if respuesta == "SI":
        adminProgram()
    else: 
        print("\n" + "Final del programa")
       

    
    