from src.db.crud.listCategory import querylistcategory
import pytest

@pytest.mark.Query_List_Category
def test_listCategory():
    result = querylistcategory()
    assert type(result) == list