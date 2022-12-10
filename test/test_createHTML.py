from src.logic.createHTML import createFile
import pytest

@pytest.mark.createHTML
def test_createHTML():
    # assert createFile("prueba.html", "prueba", "docs/", "docs/prueba.html") == "prueba.html has been created in docs/"
    assert createFile("prueba2.html", 1, "docs/", "docs/prueba.html") == None

