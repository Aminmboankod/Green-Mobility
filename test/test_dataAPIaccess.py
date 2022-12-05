from src.db.dataAPIaccess import dataBikes
import pytest

#Test para comprobar si se devuelve una lista de diccionarios.
def test_dataBikes():
    result = dataBikes()
    assert type(result) == list

#Test para comprobar si cada bici tiene un identificador.
def test_dataBikes2():
    result = dataBikes()
    assert '_id' in result[0]

#Test para comprobar si cada bici tiene una categoría que luego usaremos.
def test_dataBikes3():
    result = dataBikes()
    assert 'category' in result[2]

#Test para comprobar si cada bici tiene una marca que luego usaremos.
def test_dataBikes4():
    result = dataBikes()
    assert 'brand' in result[3]
