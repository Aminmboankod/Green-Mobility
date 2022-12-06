from mainCRUD import CRUD
import json
import os

KEY = os.environ["APIKEY"]
URL_FIND = os.environ["URL_FIND"]

def findCRUD():
    
    url = URL_FIND

    payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "filter": {"name": "Prueba"}
        })
    
    CRUD(url, payload)

findCRUD()