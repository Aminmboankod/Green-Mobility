from src.db.mainCRUD import CRUD
import pytest
import os
import json

@pytest.mark.datalist
def test_databikes():

    url = URL = os.environ["URL"]

    # Payload devolverá todo el contenido de la base de datos
    payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "filter": {}, 
        })

    result = CRUD(url, payload)
   
    assert type(result) == list     # Para saber si con una conexión exitosa devuelve una lista

@pytest.mark.CompleteBikesData
def test_databikes():

    url = URL = os.environ["URL"]

    # Payload devolverá todo el contenido de la base de datos
    payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "filter": {}, 
        })

    result = CRUD(url, payload) 
    assert '_id' in result[0]       # Test para comprobar si cada bici tiene un identificador.
    assert 'category' in result[2]  # Test para comprobar si cada bici tiene una categoría que luego usaremos.
    assert 'brand' in result[3]     # Test para comprobar si cada bici tiene una marca que luego usaremos.

