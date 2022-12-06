import json
import requests
import os
from mainCRUD import CRUD

def deleteCRUD():

    KEY = os.environ["APIKEY"]
    URL_DELETE = os.environ["URL_DELETE"]

    url = URL_DELETE

    payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "filter": {
            "name": "Prueba",
        }
        })

    CRUD(url, payload)
    print("Bike has been deleted successfully")

deleteCRUD()