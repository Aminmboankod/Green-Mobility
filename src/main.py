## EN ESTE FICHERO INCLUIREMOS LAS FUNCIONES QUE YA ESTÉN TERMINADAS PARA EL ORDEN DE EJECUCIÓN ##




from db.dataAPIaccess import dataBikes     # importamos módulo que consulta extrae datos de mongodb
from logic.createListcategory import listofBikesForCategory
from logic.createListBrand import listofBikesForBrand

if __name__=="__main__":

    dictionaryBikes = dataBikes()          # usamos datos del módulo de conexión a mongodb y los añadimos a una variable que usaremos como parámetro.


    # Llamamos a la fución que crea listas de bici y le mandamos parámetros de la categoría a filtrar
    listofBikesForCategory(dictionaryBikes, 'MTB')
    listofBikesForCategory(dictionaryBikes, 'Road')
    listofBikesForCategory(dictionaryBikes, 'City')
    listofBikesForCategory(dictionaryBikes, 'E-Road')
    listofBikesForCategory(dictionaryBikes, 'E-MTB')
    listofBikesForCategory(dictionaryBikes, 'E-City')



    # Llamamos a la función que crea listas de bici y le madamos parámetros de la marca a filtrar

    listofBikesForBrand(dictionaryBikes, 'Canyon')
    listofBikesForBrand(dictionaryBikes, 'BH')
    listofBikesForBrand(dictionaryBikes, 'Giant')
    listofBikesForBrand(dictionaryBikes, 'Bianchi')
    listofBikesForBrand(dictionaryBikes, 'Cannondale')
    listofBikesForBrand(dictionaryBikes, 'Cube')




