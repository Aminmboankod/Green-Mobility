
import json
import os

KEY = os.environ["APIKEY"]
URL_DELETE = os.environ["URL_DELETE"]

def deleteCRUD(payload):
    from db.mainCRUD import CRUD
    url = URL_DELETE

    payload = payload

    return CRUD(url, payload)

