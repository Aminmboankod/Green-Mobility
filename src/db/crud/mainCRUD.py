import json
import requests
import os

KEY = os.environ["APIKEY"]
URL = os.environ["URL"]
URL_INSERT = os.environ["URL_INSERT"]
URL_FIND = os.environ["URL_FIND"]
URL_UPDATE = os.environ["URL_UPDATE"]
URL_DELETE = os.environ["URL_DELETE"]

def CRUD(url, payload):
    
    url = url

    payload = payload

    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': KEY,
        'Accept': 'application/json'
        }
    
    try:
        query = requests.post(url, headers=headers, data=payload)
        status = query.status_code
        query.raise_for_status()
        
    except requests.exceptions.HTTPError:

        if status == 400:
            print("The query isn't correct")

        if status == 401:
            print("Unauthorized user tries to connect!")
        
        if status == 404:
            print("HTTP not found!")

        if status == 500:
            print("Internal server error")
    
    else:

        print("Successful connection!")

        if url == URL:

            print("Successful connection!")
            GreenMobility = requests.post(url, headers=headers, data=payload)
            GreenMobility = GreenMobility.text
            jsonDocument = json.loads(GreenMobility)
            Bikelist = jsonDocument.get('documents')
            return Bikelist

        elif url == URL_INSERT:

            print("Bike has been created successfully")

        elif url == URL_FIND:

            print("Bike has been found successfully")
            GreenMobility = query.text
            jsonDocument = json.loads(GreenMobility)
            Bike = jsonDocument.get('document')
            print(Bike)

        elif url == URL_UPDATE:

            print("Bike has been updated successfully")
        
        elif url == URL_DELETE:

            print("Bike has been deleted successfully")
        
        
        
