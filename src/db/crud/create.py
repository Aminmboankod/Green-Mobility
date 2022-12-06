from mainCRUD import CRUD
import json
import os

KEY = os.environ["APIKEY"]
URL_INSERT = os.environ["URL_INSERT"]

def insertCRUD():
    
    url = URL_INSERT

    payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "document": {

            "name": "Prueba",
            "category": "Road",
            "brand": "Canyon",
            "material": "Carbon",
            "frame_size": "M"
        }
        })

    CRUD(url, payload)
    
insertCRUD()


