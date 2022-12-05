from src.db.QueryList import querylistcategory
import pytest

def test_QueryList():
    result = querylistcategory()
    assert isinstance(result, list), 'La lista debe ser una instancia de la clase list'