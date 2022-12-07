import json
import os


KEY = os.environ["APIKEY"]
URL_AGGREGATE = os.environ["URL_AGGREGATE"]


def querylistbrand():
    from db.mainCRUD import CRUD
    url = URL_AGGREGATE

    payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "pipeline": [{"$group": {"_id": "$brand"}}]
        })

    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': KEY,
        'Accept': 'application/json'
        }

    return CRUD(url, payload)