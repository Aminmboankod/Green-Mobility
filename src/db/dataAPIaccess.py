import json
import requests

url = "https://data.mongodb-api.com/app/data-ijmfb/endpoint/data/v1/action/find"

payload = json.dumps(
    {
    "collection": "bikes",
    "database": "GreenMobility",
    "dataSource": "Cluster0",
    "filter": {

    }})

headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'Hc28jQ1d3AefiXjJ0Z8xWdaL8OWc93aTTm8L2RuuhCh0ZADccNe4Hr6zEOerBM5o',
    'Accept': 'application/json'
    }





query = requests.post(url, headers=headers, data=payload)
status = query.status_code
if status == 200:
    print("successful connection!")
    query = query.text
    query = json.loads(query)
    query = query["documents"]
    createJson = open("GreenMobility.json", "w+", encoding="UTF-8")
    
else:
    if status == 401:
        print("unauthorized user")
