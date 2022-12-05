from src.db.QueryList import querylistcategory
import pytest
# test para comprobar si la consulta a la base de datos devuelve la lista que esperamos
def test_QueryList():
    result = querylistcategory()
    assert isinstance(result, list), 'La lista debe ser una instancia de la clase list'