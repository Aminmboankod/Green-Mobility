
import json
import os

KEY = os.environ["APIKEY"]
URL_DELETE = os.environ["URL_DELETE"]

def deleteCRUD():
    from db.mainCRUD import CRUD
    url = URL_DELETE

    payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "filter": {
            "name": "PruebaDeLaMuerte",
        }
        })

    return CRUD(url, payload)

