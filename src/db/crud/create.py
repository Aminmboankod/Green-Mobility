
import json
import os

KEY = os.environ["APIKEY"]
URL_INSERT = os.environ["URL_INSERT"]

def insertCRUD(payload):
    from db.mainCRUD import CRUD
    
    
    url = URL_INSERT

    payload = payload

    return CRUD(url, payload)
    



