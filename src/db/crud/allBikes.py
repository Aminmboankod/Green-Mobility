
import json
import os

KEY = os.environ["APIKEY"]
URL = os.environ["URL"]

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
