from src.db.mainCRUD import CRUD

import json
import os


KEY = os.environ["APIKEY"]
URL_AGGREGATE = os.environ["URL_AGGREGATE"]

def querylistcategory():
    
    url = URL_AGGREGATE

    payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "pipeline": [{"$group": {"_id": "$category"}}]
        })
    
    return CRUD(url, payload)
