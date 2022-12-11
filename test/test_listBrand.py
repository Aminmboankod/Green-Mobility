from src.db.crud.listBrand import querylistbrand
import pytest


@pytest.mark.Query_List_Brand
def test_listBrand():
    result = querylistbrand()
    assert type(result) == list