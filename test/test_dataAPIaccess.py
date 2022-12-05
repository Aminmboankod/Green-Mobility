from src.db.dataAPIaccess import dataBikes
import pytest

#Test para comprobar si se devuelve una lista de diccionarios.
def test_dataBikes():
    result = dataBikes()
    assert type(result) == list

#Test para saber si cada bici tiene un identificador.
def test_dataBikes2():
    result = dataBikes()
    assert '_id' in result[0]