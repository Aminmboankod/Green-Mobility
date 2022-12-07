import json
import os

from db.mainCRUD import CRUD
KEY = os.environ["APIKEY"]
URL_AGGREGATE = os.environ["URL_AGGREGATE"]

def querylistcategory():

    #from db.mainCRUD import CRUD
    
    url = URL_AGGREGATE

    payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "pipeline": [{"$group": {"_id": "$category"}}]
        })
    
    return CRUD(url, payload)
