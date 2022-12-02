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
    'api-key': '',
    'Accept': 'application/json'
    }
Query = requests.post(url, headers=headers, data=payload)
# aqui debemos controlar la conexión e implementar control de errores (try, except y finally)
Query = Query.text(json.loads(Query["documents"]))

createJson = open("GreenMobility.json", "w+", encoding="UTF-8")
createJson.write(Query)