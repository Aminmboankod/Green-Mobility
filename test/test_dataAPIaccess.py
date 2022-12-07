from src.db.crud.allBikes import dataBikes
import pytest

#Test para comprobar si se devuelve una lista de diccionarios.
@pytest.mark.lista_bd
def test_dataBikes():
    result = dataBikes()
    assert type(result) == list

#Test para comprobar si cada bici tiene un identificador.
@pytest.mark.existence_id
def test_dataBikes2():
    result = dataBikes()
    assert '_id' in result[0]

#Test para comprobar si cada bici tiene una categoría que luego usaremos.
@pytest.mark.existence_category
def test_dataBikes3():
    result = dataBikes()
    assert 'category' in result[2]

#Test para comprobar si cada bici tiene una marca que luego usaremos.
@pytest.mark.existence_brand
def test_dataBikes4():
    result = dataBikes()
    assert 'brand' in result[3]
