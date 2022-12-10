
import json
import os

KEY = os.environ["APIKEY"]
URL_INSERT = os.environ["URL_INSERT"]

def insertCRUD():
    from db.mainCRUD import CRUD
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
            "frame_size": "M",
        }
        })

    return CRUD(url, payload)
    



