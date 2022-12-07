from src.db.crud.listCategory import querylistcategory
from src.db.crud.listBrand import querylistbrand
import pytest
# test para comprobar si la consulta a la base de datos devuelve la lista que esperamos
@pytest.mark.data_Query_List
def test_listBrand():
    result = querylistcategory()
    assert isinstance(result, list), 'La lista debe ser una instancia de la clase list'

def test_listCategory():
    result = querylistbrand()
    assert isinstance(result, list), 'La lista debe ser una instancia de la clase list'