import json
import requests
import os

key = os.environ["APIKEY"]

def dataBikes():
    
    url = os.environ["URL"]

    payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "filter": {}
        })

    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': key,
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
        GreenMobility = requests.post(url, headers=headers, data=payload)
        GreenMobility = GreenMobility.text
        jsonDocument = json.loads(GreenMobility)
        Bikelist = jsonDocument.get('documents')
    return Bikelist