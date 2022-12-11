
import json
import os

KEY = os.environ["APIKEY"]
URL_FIND = os.environ["URL_FIND"]

def findCRUD(payload):
    from db.mainCRUD import CRUD
    url = URL_FIND

    payload = payload
    
    return CRUD(url, payload)

