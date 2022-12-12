import json
import requests
import os

KEY = os.environ["APIKEY"]
URL = os.environ["URL"]
URL_INSERT = os.environ["URL_INSERT"]
URL_FIND = os.environ["URL_FIND"]
URL_UPDATE = os.environ["URL_UPDATE"]
URL_DELETE = os.environ["URL_DELETE"]
URL_AGGREGATE = os.environ["URL_AGGREGATE"]

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
    
    if url == URL_INSERT:
        print("Bike has been created successfully")

    elif url == URL_UPDATE:
        print("Bike has been updated successfully")

    elif url == URL_DELETE:
        print("Bike has been deleted successfully")


    elif url == URL_FIND:

        print("Bike has been found successfully")
        query = query.text
        jsonDocument = json.loads(query)
        Bike = jsonDocument.get('document')
        print(Bike)

    elif url == URL or URL_AGGREGATE:

        print("\n" + "Successful connection!")
        query = query.text
        jsonDocument = json.loads(query)
        Bikelist = jsonDocument.get('documents')
        return Bikelist



            
