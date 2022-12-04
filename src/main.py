## EN ESTE FICHERO INCLUIREMOS LAS FUNCIONES QUE YA ESTÉN TERMINADAS PARA EL ORDEN DE EJECUCIÓN ##




from db.dataAPIaccess import dataBikes     # importamos módulo que consulta extrae datos de mongodb

if __name__=="__main__":

    dictionaryBikes = dataBikes()          # usamos datos del módulo de conexión a mongodb y los añadimos a una variable que usaremos como parámetro.