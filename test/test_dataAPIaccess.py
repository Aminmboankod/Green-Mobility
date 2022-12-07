from src.db.mainCRUD import CRUD
import pytest

#Test para comprobar si se devuelve una lista de diccionarios.
@pytest.mark.lista_bd
def test_dataBikes():
    result = CRUD()
    assert type(result) == list

#Test para comprobar si cada bici tiene un identificador.
@pytest.mark.existence_id
def test_dataBikes2():
    result = CRUD()
    assert '_id' in result[0]

#Test para comprobar si cada bici tiene una categoría que luego usaremos.
@pytest.mark.existence_category
def test_dataBikes3():
    result = CRUD()
    assert 'category' in result[2]

#Test para comprobar si cada bici tiene una marca que luego usaremos.
@pytest.mark.existence_brand
def test_dataBikes4():
    result = CRUD()
    assert 'brand' in result[3]

@pytest.mark.data_Query_List
def test_listBrand():
    result = CRUD()
    assert isinstance(result, list), 'La lista debe ser una instancia de la clase list'

def test_listCategory():
    result = CRUD()
    assert isinstance(result, list), 'La lista debe ser una instancia de la clase list'