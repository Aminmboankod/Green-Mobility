from src.db.crud.listBrand import querylistbrand
from src.db.crud.listCategory import querylistcategory
import pytest

@pytest.mark.Query_List_Brand
def test_listBrand():
    result = querylistbrand()
    assert type(result) == list

@pytest.mark.Query_List_Category
def test_listCategory():
    result = querylistcategory()
    assert type(result) == list