## EN ESTE FICHERO INCLUIREMOS LAS FUNCIONES QUE YA ESTÉN TERMINADAS PARA EL ORDEN DE EJECUCIÓN ##




from db.dataAPIaccess import dataBikes     # importamos módulo que consulta extrae datos de mongodb
from logic.createIndexHTML import createContentIndex
from logic.createListcategory import listofBikesForCategory
from logic.createListBrand import listofBikesForBrand

if __name__=="__main__":


    # usamos datos del módulo de conexión a mongodb y los añadimos a una variable que usaremos como parámetro.
    listOfDictionaryBikes = dataBikes()  


    # Ejecutamos la fución que crea la página principal de acceso "Index.html"
    # createContentIndex()

    # Llamamos a la fución que crea listas de bici y le mandamos parámetros de la categoría a filtrar
    listofBikesForCategory(listOfDictionaryBikes, 'MTB')
    listofBikesForCategory(listOfDictionaryBikes, 'Road')
    listofBikesForCategory(listOfDictionaryBikes, 'City')
    listofBikesForCategory(listOfDictionaryBikes, 'E-Road')
    listofBikesForCategory(listOfDictionaryBikes, 'E-MTB')
    listofBikesForCategory(listOfDictionaryBikes, 'E-City')



    # Llamamos a la función que crea listas de bici y le madamos parámetros de la marca a filtrar
    listofBikesForBrand(listOfDictionaryBikes, 'Canyon')
    listofBikesForBrand(listOfDictionaryBikes, 'BH')
    listofBikesForBrand(listOfDictionaryBikes, 'Giant')
    listofBikesForBrand(listOfDictionaryBikes, 'Bianchi')
    listofBikesForBrand(listOfDictionaryBikes, 'Cannondale')
    listofBikesForBrand(listOfDictionaryBikes, 'Cube')




