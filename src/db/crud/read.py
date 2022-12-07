
import json
import os

KEY = os.environ["APIKEY"]
URL_FIND = os.environ["URL_FIND"]

def findCRUD():
    from db.mainCRUD import CRUD
    url = URL_FIND

    payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "filter": {"name": "PruebaDeLaMuerte"}
        })
    
    return CRUD(url, payload)

