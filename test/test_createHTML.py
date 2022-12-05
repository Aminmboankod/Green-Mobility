from src.logic.createHTML import createFile
import pytest

def test_createHTML():
    assert createFile(filename="prueba.html", content="prueba", directory="docs/", path="docs/prueba.html") == "prueba.html has been created in docs/"
    assert createFile(filename="prueba2.html", content=1, directory="docs/", path="docs/prueba.html") == None

