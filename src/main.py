




####### MÓDULO DE EJECUCIÓ DEL PROGRAMA PRINCIPAL #######


# Importamos todos los módulos y sus funciones
from db.dataAPIaccess import dataBikes     
from logic.createIndexHTML import createContentIndex
from logic.createListcategory import listofBikesForCategory
from logic.createListBrand import listofBikesForBrand
from db.QueryList import querylistcategory, querylistbrand
from logic.createShowBike import createShowBike
from autoGit import commit, push

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

