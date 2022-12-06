import json
import requests
import os

KEY = os.environ["APIKEY"]
URL_FIND = os.environ["URL_FIND"]

def findBikes():
    
    url = URL_FIND

    payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "filter": {
            "name": "Prueba"
        }
        })

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
        print("Bike has been found successfully")
        GreenMobility = query.text
        jsonDocument = json.loads(GreenMobility)
        print(jsonDocument)
        Bike = jsonDocument.get('documents')
        print(Bike)
       
        

findBikes()
