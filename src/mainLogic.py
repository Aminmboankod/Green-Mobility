
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
from autoGit import commitPush
from time import sleep
import os

####### MÓDULO DE EJECUCIÓ DEL PROGRAMA PRINCIPAL #######

if __name__=="__main__":

    os.system("clear")

    listOfDictionaryBikes = dataBikes()                                                   # Usamos datos del módulo de conexión a mongodb y los añadimos a una variable que usaremos como parámetro.

    createContentIndex()                                                                  # Ejecutamos la fución que crea la página principal de acceso "Index.html
    createContentContact()                                                                # Ejecutamos la fución que crea la página de contacto
                                                                               

    listadiccionariosGroup = querylistcategory()                                          # de una consulta que devuelve una lista de diccionarios con las categorías existentes         
    for category in listadiccionariosGroup:                                               # ejecuta la función que crea el contenido de la página de lista de bicis por cada categoría
        listofBikesForCategory(listOfDictionaryBikes, category['_id'])

 
    listadiccionariosGroup = querylistbrand()                                             # de una consulta que devuelve una lista de diccionarios con las marcas existentes 
    for brand in listadiccionariosGroup:                                                  # ejecuta la función que crea el contenido de la página de lista de bicis por cada marca
        listofBikesForBrand(listOfDictionaryBikes, brand['_id'])
                                                                        

   
    createShowBike(listOfDictionaryBikes)                                                 # Ejecuta la función createShowBike para crear todas las paginas de las bicicletas

    commitPush("Se han añadido todas las paginas de bicicletas y listas de marcas y categorias")                   
                                                                                
    print("\n" + "All pages have been created successfully")

    print("\n" + "You can view the page by clicking here https://aminmboankod.github.io/Green-Mobility/"), sleep(1.5)

    




    ####### MÓDULO DE EJECUCIÓ PARA ADMINISTRADOR #######


    print("\n" + "You want to run the program as administrator?")
    respuesta = input().upper()

    if respuesta == "SI":
        adminProgram()
        commitPush("Actualización después del adminCRUD")

    else: 
        print("\n" + "End of program")
       

    
    