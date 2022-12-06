from crud.mainCRUD import CRUD
import json
import os

KEY = os.environ["APIKEY"]
URL = os.environ["URL"]

def dataBikes():
    
    url = URL

    payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "filter": {}
        })
    
    CRUD(url, payload)


   
    









    #     print("Successful connection!")
    #     GreenMobility = requests.post(url, headers=headers, data=payload)
    #     GreenMobility = GreenMobility.text
    #     jsonDocument = json.loads(GreenMobility)
    #     Bikelist = jsonDocument.get('documents')
    # return Bikelist