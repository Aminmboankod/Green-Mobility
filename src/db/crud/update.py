
import json
import os

KEY = os.environ["APIKEY"]
URL_UPDATE = os.environ["URL_UPDATE"]

def updateCRUD(payload):
    from db.mainCRUD import CRUD
    url = URL_UPDATE

    payload = payload
    return CRUD(url, payload)
