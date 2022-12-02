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
GreenMobility = requests.post(url, headers=headers, data=payload)
GreenMobility = GreenMobility.text
GreenMobility = json.loads(GreenMobility)
GreenMobility = GreenMobility["documents"]