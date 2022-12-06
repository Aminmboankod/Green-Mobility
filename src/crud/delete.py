from mainCRUD import CRUD
import json
import os

KEY = os.environ["APIKEY"]
URL_DELETE = os.environ["URL_DELETE"]

def deleteCRUD():

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

    CRUD(url, payload)

deleteCRUD()