import json
import os

KEY = os.environ["APIKEY"]
URL = os.environ["URL"]

###### Función que acumula en varaible TODAS las bicicletas de la base de datos #####

def dataBikes():
    from db.mainCRUD import CRUD
    url = URL

    payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "filter": {}
        })
    
    return CRUD(url, payload)
